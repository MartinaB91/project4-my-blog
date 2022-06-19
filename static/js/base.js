// When user click search button, search field will be displayed.
$(document).ready(function(){
  
    $("#btn-search").click(function(){
      
      if ($("#textbox-search").hasClass('collapse')){
        $("#textbox-search").removeClass('collapse');
     

      }
      else {
        $("#btn-search").prop("type", "submit");
      }
      
    });
    return false;

  });


