
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
$(document).ready(function () {

    $(".profile").click(function (event) {
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/displayProfile",
        })

    });

})

$(document).ready(function () {

    $("#update_button").click(function (event) {
        event.preventDefault();
        username = $('#username').text()
        email = $('#email').text()
        dob = $('#dob').text()
        gender = $('#gender').text()
        hobbies = $('#hobbies').text()
        console.log(username)
        $.ajax({
            type: "PUT",
            data:
            {
                username: username,
                email: email,
                dob: dob,
                gender: gender,
                hobbies: hobbies
            },
            url: "/editProfile/",
            dataType: 'application/json',
            success: function (data) {
                data = JSON.stringify(data)
                data = JSON.parse(data)
                $("#username").html(data.username)
                $("#email").html(data.email)
                $("#dob").html(data.dob)
                $("#gender").html(data.gender)
                $("#hobbies").html(data.hobbies)
            }

        })

    });

})

