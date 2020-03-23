$(function () {

   $("#checkout").click(function () {
      $.getJSON('/order/makeorder/', function (data) {
         console.log(data);
         document.cookie = "order_id="+data["order_id"]+";Path=/";
         window.location = "/order/previous/view/";
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
               $("#total-price").html(data['total_price'])
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