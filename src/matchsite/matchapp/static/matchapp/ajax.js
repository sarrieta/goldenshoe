$.ajax({
		
		type: "POST",
		data: {
			  
			  'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
			   
			  // username: $("#username").val()
		       
		      // password: $("#psw").val()

		      // gender: $("input[name='gender']:checked").val();

   		      // image: //need value of image

		       email: $("#email").val()

		   	  },

		//https://www.youtube.com/watch?v=H1sHOvc8au0
		success: function (response) {
        	if (response.success == true) {
        		alert("hey")
        	}

        	else {
        		alert("no")
        	}

        }
	 });