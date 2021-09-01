function send_value(){

    $.ajax({
    url: '/target_view/',
    method : 'POST',
    data: {quantity: $('#theInput').val()},
    beforeSend: function() {
     // things to do before submit
    },
    success: function(response) {

     alert(response)
     }
     });
}