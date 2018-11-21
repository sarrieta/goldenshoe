
///password validation starts
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

$(function() {
    $('#profile-image1').on('click', function() {
    $('#profile-image-upload').click();
    });
});

$('#psw, #psw-rep').on('keyup', function () {

        if ($('#psw').val() == $('#psw-rep').val()) {
          $('#message').html('Password match').css('color', 'green');
        } else {
          $('#message').html('Passwords do not match').css('color', 'red');
        }

});

///password regesxvalidation ends
