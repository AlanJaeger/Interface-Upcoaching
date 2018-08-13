/*script carousel*/

$('.carousel2').slick({
    centerMode: false,
    centerPadding: '5px',
    slidesToShow: 3,
    responsive: [{
        breakpoint: 768,
        settings: {
            arrows: true,
            centerMode: false,
            centerPadding: '5px',
            slidesToShow: 2
        }
    }, {
        breakpoint: 475,
        settings: {
            arrows: true,
            centerMode: false,
            centerPadding: '5px',
            slidesToShow: 1
        }
    }]
});