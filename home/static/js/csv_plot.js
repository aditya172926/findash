var send_data = {}

function getApiPlot() {
    let url = 'read_data';
    let name = 'tesla.csv';
    send_data['name'] = name;
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        success: function(result) {
            $("#plot_csv").html("");
            $("#plot_csv").append(result);
        },
        error: function(response) {
            console.log('error');
            console.log(response);
        }
    })
}