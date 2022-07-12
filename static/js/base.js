// When user click search button, search field will be displayed.
$(document).ready(function(){
    $(".btn-like-not-signed-in").click(function(){
    alert('You need to sign in to like posts');
    });
  
    $("#btn-search").click(function(){
      
      if ($("#textbox-search").hasClass('collapse')){
        $("#textbox-search").removeClass('collapse');
           }
      else {
        // If textbox is empty while visible, hide on next click
        if ($("#textbox-search").val() == ""){
          $("#textbox-search").addClass('collapse');

        } else {
          $("#btn-search").prop("type", "submit");

        }
      }
      
    });
    return false;

  });


