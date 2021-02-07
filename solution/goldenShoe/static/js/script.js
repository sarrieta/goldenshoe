jQuery(function ($) {

    'use strict';

    // -------------------------------------------------------------
    //
    // -------------------------------------------------------------

    (function () {

    }());


    // -------------------------------------------------------------
    //  Sticky Menu
    // -------------------------------------------------------------

    (function () {

        $('#menu-wrapper').removeClass('sticky-menu');
        $(window).on('scroll', function () {
            if ($(document).scrollTop() > 150) {
                $('#menu-wrapper').addClass('sticky-menu');
            } else {
                $('#menu-wrapper').removeClass('sticky-menu');
            }
        });

    }());


    // -------------------------------------------------------------
    //  Sticky Menu Action
    // -------------------------------------------------------------

    (function () {


        $('#main-slider').waypoint(function (direction) {

            var $active = $(this);

            if (direction === 'up') {
                var id = $active.attr('id');

                $('#menu > ul > li').removeClass('active');
                $('#menu > ul > li').find('a[href="#' + id + '"]').parent().addClass('active');

            }


        }, {
            offset: -($.waypoints('viewportHeight'))
        });


        $('#body-wrapper > div').waypoint(function (direction) {

            var $active = $(this);

            if (direction === "up") {
                $active = $active.prev();
            }

            var id = $active.attr('id');

            if (typeof(id) !== 'undefined') {
                $('#menu > ul > li').removeClass('active');
                $('#menu > ul > li').find('a[href="#' + id + '"]').parent().addClass('active');

            }

        }, {
            offset: 100 // Apply "stuck" when element 30px from top
        });


        // $('#menus > .nav > li > a, .content-nav > a').on('click', function (e) {
        //
        //
        //     e.preventDefault();
        //     e.stopImmediatePropagation();
        //
        //     var href = $(this).attr('href');
        //
        //     if (href) {
        //
        //         $(this).closest('.nav').find('>li').removeClass('active');
        //         $(this).parent().addClass('active');
        //
        //         $('html, body').animate({
        //             scrollTop: $(href).offset().top - ($('#menu-wrapper').outerHeight() + 5)
        //         }, 800);
        //     }
        //
        // });

        $('#menu-wrapper').removeClass('sticky-menu');
        $(window).on('scroll', function () {
            if ($(document).scrollTop() > 150) {
                $('#menu-wrapper').addClass('sticky-menu');
            } else {
                $('#menu-wrapper').removeClass('sticky-menu');
            }
        });

    }());


    // -------------------------------------------------------------
    //  Nice Scroll
    // -------------------------------------------------------------

    (function () {

        $("html").niceScroll({
            horizrailenabled: false
        });


    }());


    // -------------------------------------------------------------
    //   Folding Setup
    // -------------------------------------------------------------
    (function () {

        var $bodyWrapper = '#body-wrapper';

        $($bodyWrapper).find('>div').addClass('top-indent').each(function (index) {
            $(this).css('z-index', index);
        });

        // because loop start with zero index :)
        $($bodyWrapper).find('>div:odd').addClass('left-top-fold even').find('>div').addClass('wraper-shadow-right');
        $($bodyWrapper).find('>div:even').addClass('right-top-fold odd').find('>div').addClass('wraper-shadow-left');

        // remove wrapper shadow from first item
        $($bodyWrapper).find('>div:first>div').removeClass('wraper-shadow-left');


    }());

    // -------------------------------------------------------------
    //   Menu Setup for 3D
    // -------------------------------------------------------------

    (function () {
        var $menuWrapper = '#menu';
        $($menuWrapper).find('>ul>li').each(function () {
            var $text = $.trim($(this).find('a').text());
            $(this).find('a').attr('data-title', $text);
        });
    }());


    // -------------------------------------------------------------
    // Portfolio Slider
    // -------------------------------------------------------------

    (function () {


        var $portfolioSlide = $('#portfolio-items').bxSlider({
            minSlides   : 2,
            maxSlides   : 5,
            slideWidth  : 228,
            slideMargin : 0,
            pager       : false,
            infiniteLoop: false,
            useCSS      : false,
            controls    : false,
            easing      : 'easeOutBounce',
            speed       : 1200
        });


        $('.portfolio-directions > .prev-items').on('click', function () {
            $portfolioSlide.goToPrevSlide();
            return false;
        });

        $('.portfolio-directions > .next-items').on('click', function () {
            $portfolioSlide.goToNextSlide();
            return false;
        });

    }());

    // -------------------------------------------------------------
    // Team Slider
    // -------------------------------------------------------------

    (function () {


        var $teamSlide = $('#team-items').bxSlider({
            minSlides   : 2,
            maxSlides   : 4,
            slideWidth  : 280,
            slideMargin : 5,
            pager       : false,
            infiniteLoop: false,
            useCSS      : false,
            controls    : false,
            easing      : 'easeInOutCirc',
            speed       : 500
        });


        $('.team-directions > .prev-items').on('click', function () {
            $teamSlide.goToPrevSlide();
            return false;
        });

        $('.team-directions > .next-items').on('click', function () {
            $teamSlide.goToNextSlide();
            return false;
        });

    }());


    // -------------------------------------------------------------
    // Defining Skill progress
    // -------------------------------------------------------------

    (function () {
        $('.skill-progress').hippoSkillPercentage({
            width     : 130,
            background: 'rgba(255,255,255,0.05)',
            font      : '14px verdana',
            fontColor : '#ffffff'
        });
    }());

    // -------------------------------------------------------------
    // Blog Tabs
    // -------------------------------------------------------------

    (function () {

        $('.blog-posts-list >li >a:first').tab('show');


        var $blogListSlide = $('.blog-posts-list').bxSlider({
            mode        : 'vertical',
            slideWidth  : null,
            minSlides   : 5,
            slideMargin : 0,
            pager       : false,
            infiniteLoop: false,
            useCSS      : false,
            controls    : false,
            easing      : 'easeInOutCirc',
            speed       : 500

        });

        $('.blog-directions > .prev-items').on('click', function () {
            $blogListSlide.goToPrevSlide();
            return false;
        });

        $('.blog-directions > .next-items').on('click', function () {
            $blogListSlide.goToNextSlide();
            return false;
        });


    }());




    // -------------------------------------------------------------
    //  Modal Window
    // -------------------------------------------------------------



    // ------------
    //  Modal
    // ------------



    // -------------------------------------------------------------
    // Goto Top



});
