
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
    $("#profile-image-upload").on("change", function(){
        //event.preventDefault();

        //get file from form
        var file = $('#profile-image-upload')[0].files[0];
        //var image = new FormData($('#profile-image-upload')[0]);

        //if(formdata){
            //formdata.append("image", file);
            $.ajax({
                url: "/editProfile/",
                type: "PUT",
                data: file,
                // Tell jQuery not to process data or worry about content-type
                cache: false,
                processData: false,
                contentType: false,
                success: function (data) {
                    console.log(data)
                },
                error: console.log($('#profile-image-upload'))
            })

<<<<<<< HEAD
        }
        //send file with ajax
      

=======
>>>>>>> bd7a171caf3ef31bc97762b0dee7a382125cb709

    
    });

});

