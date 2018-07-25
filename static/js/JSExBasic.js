window.onload = init;


function init() {
  // document.getElementById('btn1').onclick = changeN;
  // document.getElementsByTagName('input').onclick = changeI;
  // document.getElementById('btn1').onclick = changeI;
  // document.body.onload = printNode(document.body);
  // document.getElementById('btn1').onclick = changElement;
  // var elm = document.getElementById('mg');
  // alert(elm.innerHTML);
  // document.body.childNodes[1].removeChild(elm);
  // var elm_suibian = document.getElementById('suibian');
  // alert("是否要更改:")
  // elm_suibian.innerHTML = "kaiqi 年薪2毛钱";
  // elm_suibian.style.color='red';
  var elms = document.getElementsByName("skills");
  // for (var elm in elms) {
  //   alert(elms[elm].value);
  // }
  // for (var i = 0; i < elms.length; i++) {
  //   alert(elms[i].value)
  // }
  var fruits = [];
  fruits[0] = 'apple'
  fruits[1] = 'apple1'
  fruits[2] = 'apple2'
  fruits[3] = 'apple3'
  for (var elm in fruits) {
    console.log("loop_seperator")
    console.log(fruits[elm])
    console.log(fruits[elm].value);
  }
  // for (var elm in elms) {
  //   console.log("loop_seperator")
  //   console.log(elms[elm])
  //   console.log(elms[elm].value);
  // }
}

function myHandler(message) {
  alert(message)
}

function changElement() {
  alert(document.getElementById('mg').innerHTML);
  var newElm = document.createElement('p');
  newElm.appendChild(document.createTextNode('Hello, again'));
  document.body.appendChild(newElm);
}

function printNode(node) {
  document.writeln("nodeName=" + node.nodeName + "; nodeType=" + node.nodeType + "; nodeValue=" + node.nodeValue + "<br>")
  if (node.hasChildNodes()) {
    var childs = node.childNodes;
    for (var i=0; i<childs.length; i++) {
      printNode(childs[i]);
    }
  }
}

function changeI() {
  var elm = document.getElementById('mg');
  alert(elm.innerHTML)
  elm.innerHTML = "good ada"
  alert(elm.innerHTML)
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
  // var a = ['1', '2', '3']
  // rslt = a.map(function(item){
  //  return item + 'a'
  // });
  // console.log(rslt)
  // var fruits = ['apple', 'orange', 'banana'];
  // fruits.forEach( function(item) {
  //    console.log('processing item: ' + item);
  // });
  // console.log(a.length)
  // console.log(a.join("-"))
  // b = console.log(a.concat("asdf", "asdf"))
  // console.log(b)
  // -- oo
  // var objectName = {
  //   name: "Alex",
  //   age: 21,
  //   88: "hel",
  //   'myname': "peter",
  //   "font-size": '14px',
  // }
  // console.log(objectName)
  //
  // var request = {
  //   type: "POST",
  //   url: 'apple.php'
  // };
  //
  // console.log(request.type);
  // console.log(request.url);
  //
  // request.url = "orange.php"
  // console.log(request.url);
  //
  // console.log(request['type']);
  // console.log(request['url']);
  //
  // var key = 'url'
  // console.log(request[key])
  //
  // console.log(request.hasOwnProperty('type'))

  // var myCircle = {
  //   redius: 5.5,
  //   created: new Date(),
  //   getArea: function() {
  //     return this.redius * this.redius * Math.PI;
  //   },
  //   toString: toString
  // };
  //
  // console.log("type: " + typeof myCircle);
  // console.log(myCircle instanceof Object);
  //
  //
  // function toString() {
  //   return "cirCle {radius: " + this.redius + ", created: " + this.created + "}";
  // };
  //
  // console.log(myCircle.getArea())
  // console.log(myCircle.toString)
  //
  // var str1 = 'hello';
  // var l1 = ['hello'];
  // console.log(str1 instanceof String);
  // console.log(str1 instanceof Object);
  // console.log("type: " + typeof l1[0])

  function Circle(radius) {
    this.radius = radius || 1;      // Default is 1, if radius evaluates to false (e.g., undefined)
    this.dateCreated = new Date();  // Assign an object
    this.getArea = function() {     // Assign a function object via an inline function
       return this.radius * this.radius * Math.PI;
    };
    this.toString = toString; //uAssign a function object via a named function
  }

  // Define the function toString()
  function toString() {
    return "Circle {radius: " + this.radius
          + ", dateCreated: " + this.dateCreated + "}";
  };
  circle2 = new Circle(1.5);
  alert(circle2.radius);
  alert(circle2.toString());



}
