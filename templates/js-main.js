<script type="text/javascript">
  
	var flag = true;
	
	function login(){
	
		if(flag == true)
		{
			
			setTimeout(function(){ $("#loggin-form").fadeIn(500); }, 1000);
			$("#just").fadeOut(500);
			$("#desc").fadeOut(500);
			$("#login").fadeOut(500);
			flag = false;
		}
		
	}
	
	$(document).mouseup(function (e) { 
			if ($(e.target).closest("#register-form").length 
							=== 0 && (flag == false)) { 
				$("#loggin-form").fadeOut(500);
				setTimeout(function(){ $("#just").fadeIn(1500); }, 1000);
				setTimeout(function(){ $("#desc").fadeIn(1500); }, 1000);
				$("#login").fadeIn(500);
				flag = true;
			} 
	});
	
	var flag1 = true;
	
	function register(){
	
		if(flag1 == true)
		{
			
			setTimeout(function(){ $("#register-form").fadeIn(500); }, 1000);
			$("#just").fadeOut(500);
			$("#desc").fadeOut(500);
			flag1 = false;
		}
	
	}
	
	
		$(document).mouseup(function (e) { 
			if ($(e.target).closest("#register-form").length 
							=== 0 && (flag1 == false)) { 
				$("#register-form").fadeOut(500);
				setTimeout(function(){ $("#just").fadeIn(1500); }, 1000);
				setTimeout(function(){ $("#desc").fadeIn(1500); }, 1000);
				flag1 = true;
			} 
		});
	
  </script>