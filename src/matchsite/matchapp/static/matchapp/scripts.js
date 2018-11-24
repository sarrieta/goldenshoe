
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

///password regesxvalidation ends

//when user logs in the profile page displays
$(document).ready(function(){ 

$(".profile").click(function(event){
	event.preventDefault();
	$.ajax({
		type: "GET",
		url: "/displayProfile", 
		success: 
		console.log("test")

	})
	
});

})

