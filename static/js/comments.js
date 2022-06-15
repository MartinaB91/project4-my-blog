// When user click comment button icon, comment field will be displayed/hidden.
$(document).ready(function () {
  $('.btn-comments').click(function () {
    let commentWrapper = $(this).parent().parent().parent().siblings().first();
    if (commentWrapper.hasClass('collapse')) {
      commentWrapper.removeClass('collapse');
    } else {
      commentWrapper.addClass('collapse');
    }
  });
});
