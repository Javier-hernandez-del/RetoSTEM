function myFunction1() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "movsteamlogo.png";
  } else {
    x.style.display = "none";
  }
}

function myFunction2() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function myFunction3() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


function showPicture() {
  var sourceOfPicture = "IM1.png";
  var img = document.getElementById('image')
  img.src = sourceOfPicture.replace('30x30', '30x30');
  img.style.display = "block";
} 

function showPicture2() {
  var sourceOfPicture = "/static/IM2.png";
  var img = document.getElementById('image')
  img.src = sourceOfPicture.replace('30x30', '30x30');
  img.style.display = "block";
}

function showPicture3() {
  var sourceOfPicture = "/static/IM3.png";
  var img = document.getElementById('image')
  img.src = sourceOfPicture.replace('30x30', '30x30');
  img.style.display = "block";
}

function openForm() {
    document.getElementById("popupForm").style.display = "block";
}
      
function closeForm() {
    document.getElementById("popupForm").style.display = "none";
}
