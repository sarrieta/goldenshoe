
///password validation starts
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

$(function () {
    $('#profile-image1').on('click', function () {
        $('#profile-image-upload').click();
    });
});

///password regesxvalidation ends

//when user logs in the profile page displays
/*$(document).ready(function () {

    $(".profile").click(function (event) {
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/displayProfile",
        })

    });

})*/

$(document).ready(function () {

    $("#update_button").click(function (event) {
        event.preventDefault();
        email = $('#email').text()
        dob = $('#dob').text()
        gender = $('#gender').text()
        hobbies = $('#hobbies').text()


        $.ajax({
            type: "PUT",
            data:
            {
                email: email,
                dob: dob,
                gender: gender,
                hobbies: hobbies,

            },
            url: "/editProfile/",
            dataType: 'application/json',
            success: function (data) {
                data = JSON.stringify(data)
                data = JSON.parse(data)
                $("#email").html(data.email)
                $("#dob").html(data.dob)
                $("#gender").html(data.gender)
                $("#hobbies").html(data.hobbies)
            }

        })

    });

})

//Save image file via ajax request
$(document).ready(function () {
    formdata = new FormData();
    //$("#profile-image-upload").on("change", function()
    $("#update_button").click(function (event) {
        event.preventDefault();

        //get file from form
        var file = this.files;
        //var image = new FormData($('#profile-image-upload')[0]);

        if(formdata){
            formdata.append("image", file);
            $.ajax({
                url: "/editProfile/",
                type: "PUT",
                data: formdata,
                processData: false,
                contentType: false,
                success: function (data) {
                    console.log(data)
                },
                error: console.log("file is not in server")
            })

        }
        //send file with ajax
        ////instagram like matches swiping
        $('#carouselExample').on('slide.bs.carousel', function(e) {

                var $e = $(e.relatedTarget);
                var idx = $e.index();
                var itemsPerSlide = 4;
                var totalItems = $('.carousel-item').length;

                if (idx >= totalItems - (itemsPerSlide - 1)) {
                    var it = itemsPerSlide - (totalItems - idx);
                    for (var i = 0; i < it; i++) {
                        // append slides to end
                        if (e.direction == "left") {
                            $('.carousel-item').eq(i).appendTo('.carousel-inner');
                        } else {
                            $('.carousel-item').eq(0).appendTo('.carousel-inner');
                        }
                    }
                }
            });

            $('#carouselExample').carousel({
                interval: 2000
            });


        ///instgram like matches swiping


    });

})
