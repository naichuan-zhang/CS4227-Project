$(function () {

   $("#make-order").click(function () {
      $.getJSON('/order/makeorder/', function (data) {
         console.log(data);
      });
   });

   $(".minus").click(function () {
      console.log("minus clicked");
      let $minus = $(this);
      let $td = $minus.parents("td");
      let cartid = $td.attr("cartid");
      $.getJSON('/order/minusitem/', {'cartid': cartid}, function (data) {
         console.log(data);
         if (data['status'] === 200) {
            if (data['num'] > 0) {
               let $span = $minus.next("span");
               $span.html(data['num']);
               $("#total-price").html(data['total_price']);
            } else {
               $td.remove();
               $("#total-price").html(0)
            }
         }
      });
   });

   $(".plus").click(function () {
      console.log("plus clicked");
      let $plus = $(this);
      let $td = $plus.parents("td");
      let cartid = $td.attr("cartid");
      $.getJSON('/order/plusitem/', {'cartid': cartid}, function (data) {
         console.log(data);
         if (data['status'] === 200) {
            let $span = $plus.prev("span");
            $span.html(data['num']);
            $("#total-price").html(data['total_price']);
         }
      });
   });
});