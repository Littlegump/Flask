window.onload = init;

function init() {
  document.getElementById("myLink").onclick = showWarning;
}

function showWarning() {
  return confirm("Warning! Proceed with care!")
}
