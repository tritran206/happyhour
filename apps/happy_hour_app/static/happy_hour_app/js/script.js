$( document ).ready(function() {
  $('#search-rest').on('submit', function(event){
    // event.preventDefault();
    console.log("form submitted!")  // sanity check
    var data = $('#address_location').val();
    console.log('data = ' + data);
    get_restaurants(data)

    });

    // AJAX for posting
function get_restaurants(data) {
    console.log("restuarnt search is working!") // sanity check
    console.log($('#address_location').val())

    console.log("restuarnt search is working!") // sanity check

    $.ajax({
        url : "/search_results", // the endpoint
        type: "get",
        data : data, // data sent with the post request


        // handle a successful response
        success : function(json) {
            $('#andGo').html('<h1>working</h1>'); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
          console.log("error");
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
});
