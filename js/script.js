jQuery(function ($) {

    var jcarousel = $('.jcarousel');
    var pageWrap = $('.jcarousel-wrapper');

    jcarousel
        .jcarousel({
            animation: {
                duration: 1000,
                speed: 1000,
                easing: 'linear',
                complete: function () {
                }
            }
        })
        .jcarouselAutoscroll({
            interval: 5000,
            target: '+=1',
            autostart: true,
        })
        .on('mouseover', function (e) {
            $(this).jcarouselAutoscroll('stop');
        })
        .on('mouseout', function (e) {
            $(this).jcarouselAutoscroll('start');
        });

    jcarousel
        .on('jcarousel:reload jcarousel:create', function () {
            var carousel = $(this),
                width = pageWrap.innerWidth() - 15;

            if (width >= 990) {
                width = width / 8;
            } else if (width >= 768) {
                width = width / 6;
            } else if (width >= 500) {
                width = width / 5;
            } else if (width >= 300) {
                width = width / 4;
            } else {
                width = width / 3;
            }


            carousel.jcarousel('items').css('width', Math.ceil(width) + 'px');
        })
        .jcarousel({
            wrap: 'circular'
        });

    $('.jcarousel-control-prev')
        .jcarouselControl({
            target: '-=1'
        });

    $('.jcarousel-control-next')
        .jcarouselControl({
            target: '+=1'
        });

    $('.jcarousel-pagination')
        .on('jcarouselpagination:active', 'a', function () {
            $(this).addClass('active');
        })
        .on('jcarouselpagination:inactive', 'a', function () {
            $(this).removeClass('active');
        })
        .on('click', function (e) {
            e.preventDefault();
        })
        .jcarouselPagination({
            perPage: 1,
            item: function (page) {
                return '<a href="#' + page + '">' + page + '</a>';
            }
        });


// Equal height column
    $('.sc_price_item_title').matchHeight({
        byRow: true,
        property: 'height',
        target: null,
        remove: false
    });

// Mobile Header Menu
    $(".mobile-menu-button").click(function () {
        $(this).closest("header").find(".header-nav-menu").slideToggle('medium');
        // console.log($(this).closest("header").find(".header-nav-menu-ul"));
    });

// Mobile Footer Menu
    $(".dropdown-toggle").click(function () {
        $(this).siblings('.dropdown-menu').slideToggle('medium');
    });
});
