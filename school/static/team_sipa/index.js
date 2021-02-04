let navbar = $(".navbar");

$(window).scroll(function () {
  // get the complete hight of window
  let oTop = $(".aboutsection").offset().top - window.innerHeight;
  if ($(window).scrollTop() > 100) {
    navbar.addClass("sticky");
    $(".nav-link").hover(function(){
      $(this).css("color", "#616161");
    }, function(){
      $(this).css("color", "#fff");
    });
  }else {
    navbar.removeClass("sticky");
  }
});