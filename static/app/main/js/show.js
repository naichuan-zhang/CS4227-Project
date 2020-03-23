$(function () {

    $(".plus").click(function () {
        console.log("plus clicked");

        let $plus = $(this);
        // access any attributes
        let itemId = $plus.attr("itemId");
        console.log("itemId = " + itemId);
        $.get('/order/addtocart/', {'itemId': itemId}, function (data) {
            // data is accessed as a JSON
            console.log(data);
            if (data['status'] === 302) {
                window.open('/user/login/', '_self');
            } else if (data['status'] === 200) {
                $plus.prev('span').html(data['num']);
            }
        });
    });

    $(".minus").click(function () {
        console.log("minus clicked");

        let $minus = $(this);
        // access any attributes
        let itemId = $minus.attr("itemId");
        console.log("itemId = " + itemId);
        $.get('/order/removefromcart/', {'itemId': itemId}, function (data) {
            // data is accessed as a JSON
            console.log(data);
            if (data['status'] === 302) {
                window.open('/user/login/', '_self');
            } else if (data['status'] === 200) {
                $minus.next('span').html(data['num']);
            }
        });
    });
});