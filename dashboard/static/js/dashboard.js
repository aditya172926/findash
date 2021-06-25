function processData(dataset) {
    var result = []
    dataset = JSON.parse(dataset);
    dataset.forEach(item => result.push(item.fields));
    return result;
}
$.ajax({
    url: $('#pivot-table-container').attr('data-url'),
    dataType: 'json',
    success: function (data) {
        new Flexmonster({
            container: "#pivot-table-container",
            componentFolder: "https://cdn.flexmonster.com/",
            width: "100%",
            height: 430,
            toolbar: true,
            report: {
                dataSource: {
                    type: 'json',
                    data: processData(data),
                    mapping: {
                        "product_category": {
                            "caption": "Product Category",
                            "type": "string"
                        },
                        "payment_method": {
                            "caption": "Payment Method",
                            "type": "string"
                        },
                        "shipping_cost": {
                            "caption": "Shipping Cost",
                            "type": "number"
                        },
                        "unit_price": {
                            "caption": "Unit Price",
                            "type": "number"
                        }
                    }
                },
                slice: {}
            }
        });
        new Flexmonster({
            container: "#pivot-chart-container",
            componentFolder: "https://cdn.flexmonster.com/",
            width: "100%",
            height: 430,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data),
                    mapping: {
                        "product_category": {
                            "caption": "Product Category",
                            "type": "string"
                        },
                        "payment_method": {
                            "caption": "Payment Method",
                            "type": "string"
                        },
                        "shipping_cost": {
                            "caption": "Shipping Cost",
                            "type": "number"
                        },
                        "unit_price": {
                            "caption": "Unit Price",
                            "type": "number"
                        }
                    }
                },
                slice: {},
                "options": {
                    "viewType": "charts",
                    "chart": {
                        "type": "pie"
                    }
                }
            }
        });

    }
});

