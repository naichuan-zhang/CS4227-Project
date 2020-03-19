$(function () {

    $(".minus").click(function () {
        console.log("minus clicked");

    });

    $(".plus").click(function () {
        console.log("plus clicked");

        let $plus = $(this);
        // access any attributes
        let itemId = $plus.attr("itemId");
        console.log("itemId = " + itemId);
        $.get('/order/addtoorder/', {'itemId': itemId}, function (data) {
            // data is accessed as a JSON
            if (data['status'] === 302) {
                window.open('/user/login/', '_self');
            }
        });
    });
});