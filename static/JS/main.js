$('table').hide()
$('#back').hide()

// ajax for N5 Voc
function table(value){
    $('#N5_list').hide()
    $('table').show()
    $('#back').show()
    $('#home').hide()
    
    $.ajax({
        url: value,
        type: "GET",
        dataType: "json",
        success: function(response) {
            for(i in response){
                $("#voc_table").append(`<tr><td><button class="button-30" role="button">${response[i].nihongo}</button></td>
                <td><button class="button-30" role="button">${response[i].english}</button></td>
                <td><button class="button-30" role="button">${response[i].bangla}</button></td><tr>`)
            }
        },
        error: function(xhr, status, error) {
          console.log(xhr.responseText);
        }
      });
};


// ajax for N5 Voc list
$.ajax({
    url: "/N5/list/",
    type: "GET",
    dataType: "json",
    success: function(response) {
        for (i in response){
            $("#N5_list").append(`<br><br><br><a><button onclick="table('/N5/list/${response[i].list_number}')" class="button-30" role="button">List ${response[i].list_number}</button></a>`);
        };
    },
    error: function(xhr, status, error) {
        console.log(xhr.responseText);
    }
});