var send_data = {};
var graph_divs = {};
send_data['compare'] = false;

$(document).ready(function() {
    $(document).on('click', '#graph_type', function(e) {
        e.preventDefault();
        var gt = $(this).val();
        console.log(gt);
        send_data['graph_type'] = gt;
        if (send_data['name'] != null) {
            if (graph_divs[gt] == null) {
                getApiPlot();
            }
            else {
                $("#plot_csv").html("");
                $("#plot_csv").append(graph_divs[gt]);
            }
        }
    });
    $(document).on('click', '#stock_name', function(e) {
        e.preventDefault();
        var name = $(this).val();
        console.log(name);
        send_data['name'] = name;
        if (send_data['graph_type'] != null) {
            if (graph_divs['name'] != name) {
                getApiPlot();
                graph_divs = {};
                graph_divs['name'] = name;
            }
            else {
                $("#plot_csv").html("");
                $("#plot_csv").append(graph_divs[send_data['graph_type']]);
            }
        }
    });
});

function getApiPlot() {
    let url = 'read_data';
    console.log(send_data);
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        success: function(result) {
            $("#plot_csv").html("");
            $("#plot_csv").append(result);
            graph_divs[send_data['graph_type']] = result;
            console.log(graph_divs);

        },
        error: function(response) {
            console.log('error');
            graph_divs = {};
            console.log(response);
        }
    })
}