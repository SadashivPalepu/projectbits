
const cnameEl = document.querySelector('#cname');
const durationEl = document.querySelector('#Duration');
const feeEl = document.querySelector('#Fee');

const form = document.querySelector('#signup');

/*
else if (!isBetween(username.length, min, max)) {
        showError(cnameEl, `CourseName must be between ${min} and ${max} characters.`)
    } 
*/
const checkUsername = (ele) => {

    let valid = false;

    const min = 3,
        max = 25;

    const username = ele.value.trim();

    if (!isRequired(username)) {
        showError(ele, ele.id +' cannot be blank.');
    } else if ( !isAlphabets(username)) 
	{
		showError(ele, ele.id + ' must be alphabets');
	}
	else if (!isBetween(username.length, min, max)) {
        showError(ele, ele.id +` must be between ${min} and ${max} characters.`)
    } 	
	else {
        showSuccess(ele);
        valid = true;
    }
    return valid;
};

const checkFee = (ele) => {

    let valid = false;

    const min = 3,
        max = 8;

    const username = ele.value.trim();

    if (!isRequired(username)) {
        showError(ele, ele.id +' cannot be blank.');
    } else if ( !isNumber(username)) 
	{
		showError(ele, ele.id + ' must be number');
	}
	else if (!isBetween(username.length, min, max)) {
        showError(ele, ele.id +` must be between ${min} and ${max} digits.`)
    } 	
	else {
        showSuccess(ele);
        valid = true;
    }
    return valid;
};






const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;
const isAlphabets = (name,min,max) => {
	const re = /^[a-zA-Z ]*$/;
	return re.test(name);
} 
const isNumber = (name,min,max) => {
	const re = /^[0-9]*$/;
	return re.test(name);
} 
const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    // add the error class
    formField.classList.remove('success');
    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}


form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();

    // validate fields
    let isCNameValid = checkUsername(cnameEl);
    let isFeeValid = checkFee(feeEl);
    let isFormValid = isCNameValid && isFeeValid;
   console.log(isCNameValid);	
    // submit to the server if the form is valid
    if (isFormValid) {
		
		form.submit();
    }
});


const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'cname':
            checkUsername(e.target);
            break;
        case 'fee':
            checkFee(e.target);
            break;
    }
}));



