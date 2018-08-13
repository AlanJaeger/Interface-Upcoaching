/*script carousel*/

$('.carousel2').slick({
    centerMode: false,
    centerPadding: '5px',
    slidesToShow: 4,
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

/*script footer*/

$(function() {
    var tabs = $('#features > nav a');
    var tabsContent = $('#features > article > section');

    tabs.click(function(e) {
        e.preventDefault();

        var that = $(this);

        tabs.removeClass('is-selected');
        that.addClass('is-selected');
        tabsContent.removeClass('is-selected');

        tabsContent
            .filter((i, tab) => $(tab).data('id') === that.data('id'))
            .addClass('is-selected');
    });
});

/*JS Navbar*/

$(function() {
    $(document).scroll(function() {
        var $nav = $(".navbar-fixed-top");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});