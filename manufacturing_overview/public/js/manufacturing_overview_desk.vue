<template>
  <div class="col-12 col-lg-4 layout-main-section-wrapper">
    <div class="layout-main-section">
      <div class="widget links-widget-box" style="height: auto">
        <div class="widget-head">
          <div>
            <div class="widget-subtitle"></div>
          </div>
          <div class="widget-control"></div>
        </div>
        <div class="widget-body">
          <manufacturing-overview-row
            v-for="so in salesorderData"
            :key="so.name"
            v-bind:qty="so.qty"
            v-bind:item_name="so.item_name"
            v-bind:item_code="so.item_code"
            v-bind:customer="so.customer"
            v-bind:delivery_date="so.delivery_date"
            v-bind:status="so.status"
            v-bind:link="so.link"
            v-bind:reference="so.parent"
            v-bind:due_in="so.due_in"
          >
          </manufacturing-overview-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ManufacturingOverviewRow from "./manufacturing_overview_row.vue";

export default {
  components: {
    ManufacturingOverviewRow,
  },
  data() {
    return {
      salesorderData: [
        {
          customer: "",
          delivery_date: "",
          link: "",
          name: "",
          item_name: "Loading...",
          item_code: "",
          qty: "",
          sales_order: "",
          status: "Unknown",
          due_in: 0,
        },
      ],
      timer: "",
      origin: window.location.origin,
      userPermissions: {},
    };
  },
  created() {
    this.fetchEventsList();
    this.timer = setInterval(this.fetchEventsList, 30000);
  },
  methods: {
    fetchEventsList() {
      let self = this;
      frappe.call({
        method:
          "manufacturing_overview.manufacturing_overview.api.getSalesorderOverviewList",
        async: true,
        args: {},
        callback: function (r) {
          if (r.message) {
            self.salesorderData = r.message;
          }
        },
      });
    },
    cancelAutoUpdate() {
      clearInterval(this.timer);
    },
    beforeDestroy() {
      clearInterval(this.timer);
    },
  },
};
</script>

<style>
</style>