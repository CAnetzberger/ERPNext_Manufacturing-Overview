from frappe import _

app_name = "manufacturing_overview"
app_title = "Manufacturing Overview"
app_publisher = "CAnetzberger Design"
app_description = "Dashboard Overview for Sales Orders Items to be manufactured"
app_icon = "fa fa-th"
app_color = "grey"
app_email = "admin@canetzberger.design"
app_license = "MIT"
required_apps = ["erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/manufacturing_overview/css/manufacturing_overview.css"
app_include_js = "/assets/manufacturing_overview/js/manufacturing_overview.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/manufacturing_overview/css/manufacturing_overview.css"
# web_include_js = "/assets/manufacturing_overview/js/manufacturing_overview.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "manufacturing_overview/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "manufacturing_overview.install.before_install"
# after_install = "manufacturing_overview.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "manufacturing_overview.uninstall.before_uninstall"
# after_uninstall = "manufacturing_overview.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "manufacturing_overview.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"manufacturing_overview.tasks.all"
# 	],
# 	"daily": [
# 		"manufacturing_overview.tasks.daily"
# 	],
# 	"hourly": [
# 		"manufacturing_overview.tasks.hourly"
# 	],
# 	"weekly": [
# 		"manufacturing_overview.tasks.weekly"
# 	]
# 	"monthly": [
# 		"manufacturing_overview.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "manufacturing_overview.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "manufacturing_overview.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "manufacturing_overview.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"manufacturing_overview.auth.validate"
# ]
