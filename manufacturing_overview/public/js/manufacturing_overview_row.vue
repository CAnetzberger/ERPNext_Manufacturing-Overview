<template>
  <a
    @click="pushRoute(link)"
    class="row link-item text-wrap ellipsis onbpoard-spotlight"
    type="Link"
  >
    <div class="col col-xs-8">
      <span
        class="indicator-pill no-margin"
        v-bind:class="{
          red: status === 'No Work Order',
          blue: status === 'Partially Delivered',
          green: status === 'In Warehouse',
          yellow: status === 'To Produce',
          grey: status === 'Unknown',
        }"
      ></span>
      <span class="widget-subtitle">{{ qty }}</span> -
      <span class="widget-title">{{ item_name }}</span>
      <div>
        <small v-if="customer && item_code" class="color-secondary"
          >{{ customer }} -
          <a @click="pushRoute('/app#Form/Item/' + item_code)" type="Link">{{
            item_code
          }}</a></small
        >
        <small v-else-if="customer" class="color-secondary">{{
          customer
        }}</small>
        <small v-else-if="item_code" class="color-secondary">{{
          item_code
        }}</small>
      </div>
      <div>
        <small class="color-secondary">{{ reference }}</small>
      </div>
    </div>

    <div
      v-if="due_in < 0"
      class="text-muted ellipsis color-secondary col col-xs-4 text-right"
    >
      <b style="color: red">{{ delivery_date }}</b>
    </div>
    <div
      v-else-if="due_in === 0"
      class="text-muted ellipsis color-secondary col col-xs-4 text-right"
    >
      <b style="color: black">{{ delivery_date }}</b>
    </div>
    <div
      v-else
      class="text-muted ellipsis color-secondary col col-xs-4 text-right"
    >
      {{ delivery_date }}
    </div>
  </a>
</template>

<script>
export default {
  name: "ManufacturingOverviewRow",
  props: [
    "qty",
    "item_name",
    "item_code",
    "customer",
    "delivery_date",
    "status",
    "link",
    "reference",
    "due_in",
  ],
  methods: {
    pushRoute(link) {
      frappe.router.push_state(link);
    },
  },
};
</script>

<style>
</style>