
///password validation starts

$('#psw, #psw-rep').on('keyup', function () {
  if ($('#psw').val() == $('#psw-rep').val()) {
    $('#message').html('Passwords match').css('color', 'green');
  } else
    $('#message').html('Passwords do not match').css('color', 'red');
});


var check = function() {
  if (document.getElementById('psw').value ==
    document.getElementById('psw-rep').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
  }
}
///password regesxvalidation ends
