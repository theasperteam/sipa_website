AOS.init({
    offset: 300, // offset (in px) from the original trigger point
    delay: 0, // values from 0 to 3000, with step 50ms
    duration: 1000 // values from 0 to 3000, with step 50ms
});
//script for image slider
$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll < 300) {
        $('.fixed-top').css('background', 'transparent');
    } else {
        $('.fixed-top').css('background', 'black');
    }
});