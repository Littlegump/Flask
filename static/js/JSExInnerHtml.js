window.onload = init;

function init() {
  document.getElementById("btn1").onclick = changeH1;
  document.getElementById("btn2").onclick = changeH2;
  document.getElementById("btn3").onclick = changeP;
}

function changeH1() {
  var elm = document.getElementById("heading1");
  elm.innerHTML = "hello";
}

function changeH2() {
  var elms = document.getElementsByTagName("h2");
  for (var i = 0; i < elms.length; i++) {
    elms[i].innerHTML = "Hello again!";
  }
}

function changeP() {
  //var elms = document.getElementsByClassName("para");
  //for (var i=0; i<elms.length; i++) {
  //  elms.innerHTML = "hello from grah";
  //}
  confirm("Yourname is ")
  window.open(window.location.origin + "/abc")
}
