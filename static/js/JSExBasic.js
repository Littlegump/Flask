window.onload = init;


function init() {
  document.getElementById('btn1').onclick = changeN;


}

function changeN() {
  // var str = "asdfasdfadsfasdf";
  // console.log(str)
  // var a = ["apple","pea","good","asdfasdf"]
  // for (var i = 0; i < a.length; i++){
  //   console.log(a[i])
  // }
  // for (var i in a) {
  //   console.log("ppp_style:" + a[i])
  // }
  // for (var item of a) {
  //   console.log("context: " + item)
  // }
  // var fruits = ['apple', 'orange', 'banana'];
  // fruits.forEach( function(item) {
  //    console.log('processing item: ' + item);
  // });
  var a = ['1', '2', '3']
  rslt = a.map(function(item){
   return item + 'a'
  });
  console.log(rslt)
  // var fruits = ['apple', 'orange', 'banana'];
  // fruits.forEach( function(item) {
  //    console.log('processing item: ' + item);
  // });
  // console.log(a.length)
  // console.log(a.join("-"))
  // b = console.log(a.concat("asdf", "asdf"))
  // console.log(b)
}
