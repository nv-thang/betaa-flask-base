const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container_signup_signin');

function signUpValidateForm() {
	var x = document.forms["sign-up-form"]["sign-up-name"].value;
	if (x == "") {
		//   alert("'Name' không được để trống!!");
		asAlertMsg({
			type: "error",
			title: "Trường trống",
			message: "'Tên' không được để trống!!",

			button: {
				title: "Close Button",
				bg: "Cancel Button"
			}
		});
		return false;
	}
	x = document.forms["sign-up-form"]["sign-up-email"].value;
	if (x == "") {
		//   alert("'Email' không được để trống!!");
		asAlertMsg({
			type: "error",
			title: "Trường trống",
			message: "'E-mail' không được để trống!!",

			button: {
				title: "Close Button",
				bg: "Cancel Button"
			}
		});
		return false;
	}
	x = document.forms["sign-up-form"]["sign-up-passwd"].value;
	if (x == "") {
		//   alert("'Password' không được để trống!!");
		asAlertMsg({
			type: "error",
			title: "Trường trống",
			message: "'Mật khẩu' không được để trống!!",

			button: {
				title: "Close Button",
				bg: "Cancel Button"
			}
		});
		return false;
	}
}

function signInValidateForm() {

	x = document.forms["sign-in-form"]["sign-in-email"].value;
	if (x == "") {
		//   alert("'Email' không được để trống!!");
		asAlertMsg({
			type: "error",
			title: "Trường trống",
			message: "'E-mail' không được để trống!!",

			button: {
				title: "Close Button",
				bg: "Cancel Button"
			}
		});
		return false;
	}
	x = document.forms["sign-in-form"]["sign-in-passwd"].value;
	if (x == "") {
		//   alert("'Password' không được để trống!!");
		asAlertMsg({
			type: "error",
			title: "Trường trống",
			message: "'Password' không được để trống!!",

			button: {
				title: "Close Button",
				bg: "Cancel Button"
			}
		});
		return false;
	}
}

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});