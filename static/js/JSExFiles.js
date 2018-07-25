window.onload = function() {
  init();
}

function init() {
  document.getElementById("magic").onmouseover = function() {
    this.className = "highlight";
  }
  document.getElementById("magic").onmouseout = function() {
    this.className = "";
  }
}
