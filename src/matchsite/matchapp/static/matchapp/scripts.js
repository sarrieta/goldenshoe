
///password validation starts

$('#psw, #psw-rep').on('keyup', function () {

        if ($('#psw').val() == $('#psw-rep').val()) {
          $('#message').html('Password match').css('color', 'green');
        } else {
          $('#message').html('Passwords do not match').css('color', 'red');
        }

});

///password regesxvalidation ends
