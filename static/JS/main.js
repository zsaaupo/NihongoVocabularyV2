$(document).ready(function() {

    
    // ajax for N5 Voc list
    $.ajax({
      url: "/N5/list/",
      type: "GET",
      dataType: "json",
      success: function(response) {
          for (i in response){
              $("#N5_list").append(`<br><br><br><button class="button-30" role="button">List ${response[i].list_number}</button>`);
          };
      },
      error: function(xhr, status, error) {
        console.log(xhr.responseText);
      }
    });


});