function func(x) {
  var z = 8

  return function(y) {
    console.log(x+y+z)

  }
}

var n1 = new Number(32)
var a1 = func(n1)
a1(2)