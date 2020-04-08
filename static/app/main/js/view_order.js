function make_payment(id){
            document.cookie = "order_id="+id+";Path=/";
            window.location = "/order/previous/view/make_payment";
        };

