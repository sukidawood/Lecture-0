//event listeners for removing error after text input filled
document.querySelector('#firstName').addEventListener("blur", function(){
    if(this.value !== ""){
        firstNameWarning.innerHTML = "";
    }
});

//event listeners for removing error after text input filled
document.querySelector('#lastName').addEventListener("blur", function(){
    if(this.value !== ""){
        lastNameWarning.innerHTML = "";
    }
});

//event listeners for removing error after text input filled
document.querySelector('#year').addEventListener("click", function(){
    if(this.value == ""){
        experienceWarning.innerHTML = "";
    }

});

//event listeners for removing error after option selected
document.querySelector('#positionWarning').addEventListener("change", function(){
    if(application.positionType[0].checked == true){
        positionWarning.innerHTML = "";
    }

});

//call function validateProfile to execute whem submit is pressed
document.application.addEventListener("submit", validateProfile);
