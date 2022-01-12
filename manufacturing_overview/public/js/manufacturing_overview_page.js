import ManufacturingOverviewDesk from "./manufacturing_overview_desk.vue";

$(document).ready(function () {
    $(".layout-main-section-wrapper").after('<div class="col-4 layout-main-section-wrapper" id="manufacturing-overview-body"></div>');
    var pod = new Vue({
        el: "#manufacturing-overview-body",
        render(h) {
            return h(ManufacturingOverviewDesk, {});
        }
    });
});