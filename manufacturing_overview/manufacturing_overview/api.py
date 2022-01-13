import frappe
from functools import reduce
from datetime import date


def clearCache(doc, event):
    frappe.cache().delete_value("production_overview")


@frappe.whitelist()
def getUserPermissions():
    return frappe.get_doc('Production Overview User Mapping', frappe.session.user)


def formatDate(d):
    return frappe.utils.formatdate(
        d, 'dd.MM.yyyy')


def getDueInDays(d):
    delta = d - date.today()
    return delta.days


def getWorkOrders(soname):
    return frappe.get_all("Work Order", filters={
        'sales_order': soname}, fields=['name'])


def getAmountInWarehouses(item_code):
    bins = frappe.get_all("Bin", fields=["actual_qty"], filters=[
                          ["actual_qty", ">", 0], ["item_code", "=", item_code]])
    return reduce(lambda x, y: x + y,
                  map(lambda b: b["actual_qty"], bins), 0)


def shortenCustomerName(customer):
    shortName = frappe.get_value(
        'Customer', customer, 'short_name')
    if shortName is not None:
        return shortName
    else:
        return customer


def calculateSalesOrderStatus(item, warehouseamount, workorders):
    if item.delivered_qty >= item.qty:
        return "Fully Delivered"
    elif item.delivered_qty < item.qty and item.delivered_qty > 0:
        return "Partially Delivered"
    elif item.qty <= warehouseamount:
        return "In Warehouse"
    elif len(workorders) <= 0:
        return "No Work Order"
    elif len(workorders) > 0 and item.qty > warehouseamount:
        return "To Produce"
    else:
        return "Unknown"


def generateProductionOverviewCache():
    salesOrderItems = frappe.db.sql(
        """
        SELECT
            `tabSales Order Item`.name,
            `tabSales Order Item`.item_name,
            `tabSales Order Item`.item_group,
            `tabSales Order Item`.qty,
            `tabSales Order Item`.actual_qty,
            `tabSales Order Item`.delivered_qty,
            `tabSales Order Item`.delivery_date,
            `tabSales Order Item`.item_code,
            `tabSales Order Item`.parent,
            `tabSales Order`.status as parentStatus
        FROM
            `tabSales Order Item`
        INNER JOIN `tabSales Order`
            ON
                `tabSales Order Item`.parent = `tabSales Order`.name
        WHERE
        delivered_qty < qty and
        status = 'To Deliver and Bill' and
        item_group = "Produkte"
        ORDER BY
        delivery_date
        """, as_dict=1)

    for soItem in salesOrderItems:
        soItem.due_in = getDueInDays(soItem.delivery_date)

        soItem.customer = shortenCustomerName(frappe.get_value(
            'Sales Order', soItem.parent, 'customer'))
        soItem.wos = frappe.get_all('Work Order', filters=[
                                    ['sales_order', '=', soItem.parent], ['production_item', '=', soItem.item_code], ['status', '!=', "Cancelled"]])

        soItem.delivery_date = formatDate(soItem.delivery_date)
        soItem.warehouseamount = getAmountInWarehouses(soItem.item_code)

        if soItem.warehouseamount >= soItem.qty:
            soItem.status = 'In Warehouse'
        elif len(soItem.wos) != 0:
            soItem.status = 'To Produce'
        else:
            soItem.status = 'No Work Order'

        soItem.qty = soItem.qty - soItem.delivered_qty

        soItem.link = '/app#Form/Sales%20Order/' + soItem.parent

    frappe.cache().set_value("production_overview", salesOrderItems)


@frappe.whitelist()
def getSalesorderOverviewList():
    salesOrderItems = frappe.cache().get_value(
        "production_overview", generateProductionOverviewCache())

    return salesOrderItems
