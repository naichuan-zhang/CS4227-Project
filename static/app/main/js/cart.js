$(function () {

   $("#make-order").click(function () {
      $.getJSON('/order/makeorder/', function (data) {
         console.log(data);
      });
   });
});