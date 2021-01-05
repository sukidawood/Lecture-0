//function to validate form
function validateProfile(e){

//prevent submit button from refreshing with empty fields
    e.preventDefault();

    var valid=true;

    //warning error displayed if firstName is not entered
    if(application.firstName.value === ""){
        document.querySelector('#firstNameWarning').innerHTML= "*Please enter a First Name*";
          valid = false;
    }

    //warning error displayed if lastName is not entered
    if(application.lastName.value === ""){
        document.querySelector('#lastNameWarning').innerHTML= "*Please enter a Last Name*";
          valid=false;
    }

    //warning error displayed if yearsExperience is not entered
    if(application.year.value === ""){
        document.querySelector('#experienceWarning').innerHTML="*Please specify your years of experience*";
          valid = false;
    }

    //warning error displayed if one radio option not selected
    if((application.positionType[0].checked == false) && (application.positionType[1].checked == false)
        && (application.positionType[2].checked == false)){
          valid=false;
          document.querySelector('#positionWarning').innerHTML="*Please choose your preferred position*";
    }

    return(valid);
  };

//display user information when submit is clicked
document.getElementById("submit").addEventListener("click", function(){
  document.getElementById("displayFirstName").innerHTML = document.getElementById("firstName").value;
  document.getElementById("displayLastName").innerHTML = document.getElementById("lastName").value;
  document.getElementById("displayAge").innerHTML = document.getElementById("birth").value;
  document.getElementById("displayPhone").innerHTML = document.getElementById("phoneNumber").value;

});


//module that holds list of products with corresponding prices
  var Module = (function(){
      var drinks = [{drink: "americano",
                     price:2.00},
                     {drink:"tea",
                      price: 1.50},
                     {drink:"caramel",
                      price:2.55},
                    ];

      //add total number of coffees
      return{addAmericanos: function(i){
        var formerAmericano = document.getElementById("americanoAmount").innerHTML
        var formerQuantity = Number(formerAmericano)
        document.getElementById("americanoAmount").innerHTML = formerQuantity+1
      },

      //add total price of coffees
        addAmericanoPrice: function(i){
          let formerAmericanoPrice = Number(document.getElementById("americanoSubtotal").innerHTML)
          let currentAmericanoPrice = drinks[0].price
          let newAmericanoPrice = formerAmericanoPrice + currentAmericanoPrice
          document.getElementById("americanoSubtotal").innerHTML = newAmericanoPrice
      },

      //add total number of teas
      addTeas: function(i){
        var formerTea = document.getElementById("teaAmount").innerHTML
        var formerQuantity = Number(formerTea)
        document.getElementById("teaAmount").innerHTML = formerQuantity+1

      },

      //add total price of teas
      addTeaPrice: function(i){
        let formerTeaPrice = Number(document.getElementById("teaSubtotal").innerHTML)
        let currentTeaPrice = drinks[1].price
        let newTeaPrice = formerTeaPrice + currentTeaPrice
        document.getElementById("teaSubtotal").innerHTML = newTeaPrice

      },

      //add total amount of caramel drink
      addCaramels: function(i){
        var formerCaramel = document.getElementById("caramelAmount").innerHTML
        var formerQuantity = Number(formerCaramel)
        document.getElementById("caramelAmount").innerHTML = formerQuantity+1
      },

      //add total price of caramel drink
      addCaramelPrice: function(i){
        let formerCaramelPrice = Number(document.getElementById("caramelSubtotal").innerHTML)
        let currentCaramelPrice = drinks[2].price
        let newCaramelPrice = formerCaramelPrice + currentCaramelPrice
        document.getElementById("caramelSubtotal").innerHTML = newCaramelPrice
      },

      //display americano drink
      displayAmericano: function(i){
         var currentDrink = drinks[0].drink
         document.getElementById("noOfAmericanos").innerHTML = currentDrink;
      },

      //display tea drink
      displayTea: function(i){
         var currentDrink = drinks[1].drink
         document.getElementById("noOfTeas").innerHTML = currentDrink;
      },

      //display caramel drink
      displayCaramel: function(i){
         var currentDrink = drinks[2].drink
         document.getElementById("noOfCaramels").innerHTML = currentDrink;
      },

      //display total of items selected
      displayTotal: function(){
        var totalAmount = newAmericanoPrice + newTeaPrice + newCaramelPrice;
        document.getElementById("total").innerHTML = totalAmount;
      },

      //clear user input
      clear: function(){
          var x=0
          document.getElementById("americanoSubtotal").innerHTML = 0
          document.getElementById("americanoAmount").innerHTML = 0
          document.getElementById("teaSubtotal").innerHTML = 0
          document.getElementById("teaAmount").innerHTML = 0
          document.getElementById("caramelSubtotal").innerHTML = 0
          document.getElementById("caramelAmount").innerHTML = 0
          document.getElementById("noOfAmericanos").innerHTML = ""
          document.getElementById("noOfTeas").innerHTML = ""
          document.getElementById("noOfCaramels").innerHTML = ""

      },

      };
  })();

//call function when coffee image is clicked
  document.getElementById("americano").addEventListener("click",function(){
      Module.addAmericanos(0)
      Module.addAmericanoPrice(0)
      Module.displayAmericano(0)});


//call function when tea image is clicked
  document.getElementById("tea").addEventListener("click",function(){
      Module.addTeas(1)
      Module.addTeaPrice(1)
      Module.displayTea(1)});


//call function when caramel image is clicked
  document.getElementById("caramel").addEventListener("click",function(){
      Module.addCaramels(2)
      Module.addCaramelPrice(2)
      Module.displayCaramel(2)});


//call function when submit button hit and add subtotals
document.getElementById("submitItems").addEventListener("click", function(){
      Module.displayTotal()
});

//call function when reset button hit and clear input
document.getElementById("refresh").addEventListener("click",function(){
      Module.clear()});
