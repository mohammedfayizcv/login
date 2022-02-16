console.log('heyyyyyyyy');
$(document).ready(function () {
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    let qntYears = 70;
    let selectYear = $("#year");
    let selectMonth = $("#month");
    let selectDay = $("#day");
    let currentYear = new Date().getFullYear();

    for (var y = 0; y < qntYears; y++) {
        let date = new Date(currentYear);
        let yearElem = document.createElement("option");
        yearElem.value = currentYear
        yearElem.textContent = currentYear;
        selectYear.append(yearElem);
        currentYear--;
    }

    for (var m = 0; m < 12; m++) {
        let month = monthNames[m];
        let monthElem = document.createElement("option");
        monthElem.value = m;
        monthElem.textContent = month;
        selectMonth.append(monthElem);
    }

    var d = new Date();
    var month = d.getMonth();
    var year = d.getFullYear();
    var day = d.getDate();

    selectYear.val(year);
    selectYear.on("change", AdjustDays);
    selectMonth.val(month);
    selectMonth.on("change", AdjustDays);

    AdjustDays();
    selectDay.val(day)

    function AdjustDays() {
        var year = selectYear.val();
        var month = parseInt(selectMonth.val()) + 1;
        selectDay.empty();

        //get the last day, so the number of days in that month
        var days = new Date(year, month, 0).getDate();

        //lets create the days of that month
        for (var d = 1; d <= days; d++) {
            var dayElem = document.createElement("option");
            dayElem.value = d;
            dayElem.textContent = d;
            selectDay.append(dayElem);
        }
    }
});


// validation 

function validation() {

  var username=document.getElementById('name').value;
  var phonenumber=document.getElementById('phone').value;
  var email=document.getElementById('email').value;
  var password=document.getElementById('password').value;
  var password2=document.getElementById('password2').value;
  var gender=document.getElementById('gender').value;


  var nameRx=/^[A-Za-z. ]{3,30}$/;
  var phonRx=/^[6-9]{1}[0-9]{9}$/;
  var emailRx=/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var passRx= /^[a-zA-Z\-0-9]{6,15}$/;

  if(nameRx.test(username)){
    document.getElementById('nameError').innerHTML=" ";

  }else{
    document.getElementById('nameError').innerHTML="*Name is Invalid ";
    return false;

  }
  if(phonRx.test(phonenumber)){
    document.getElementById('phonError').innerHTML=" ";

  }else{
    document.getElementById('phonError').innerHTML="*Phone number is Invalid ";
    return false;

  }
  if(emailRx.test(email)){
    document.getElementById('emailError').innerHTML=" ";

  }else{
    document.getElementById('emailError').innerHTML="*Invalid Email Address ";
    return false;

  }




  if(passRx.test(password)){
    document.getElementById('passError').innerHTML=" ";

  }else{
    document.getElementById('passError').innerHTML="*Password is Invalid, minimum 6 character please  includes and number eg:ab3cd1";
    return false;

  }
  if(password2.match(password)){
    document.getElementById('conpassError').innerHTML=" ";

  }else{
    document.getElementById('conpassError').innerHTML="*Password not matching";
    return false;
  }


  
}







