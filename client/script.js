
function onPredict() {
    var area = $("#area-inp").val();
    var furnishing = $("#furnishing-inp").find(':selected').val();
    var bhk = $("#bhk-inp").val();
    var location = $("#location-inp").find(':selected').text();
    var type = $("#type-inp").find(':selected').text();
    var url = 'http://127.0.0.1:5000/predict';
    $.post(url, {
        area: area,
        furnishing: furnishing,
        bhk: bhk,
        location: location,
        type: type
    }, function(data,status) {
        console.log(data.price);
        $('.prediction').css('visibility','visible');
        $('#price').text(data.price.toString() + " Lakhs");
        console.log(status);
    })
}


function pageOnLoad() {
    console.log("Document loaded.");
    var url_location = 'http://127.0.0.1:5000/get-locations';
    $.get(url_location, function(data,status) {
        console.log('Got respose from get-location request.');
        if(data) {
            var locations = data.locations;
            $('#location-inp').empty();
            var opt = new Option("Please select the Location", "", true, true);
            opt.disabled = true;
            opt.hidden = true;
            $("#location-inp").append(opt);
            for(var i in locations) {
                var opt = new Option(locations[i], locations[i]);
                $('#location-inp').append(opt);
            }
        }
    })
}

window.onload = pageOnLoad;