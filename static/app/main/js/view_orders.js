function view_order(id){
            document.cookie = "order_id="+id+";Path=/";
            window.location = "/order/previous/view/";
        };