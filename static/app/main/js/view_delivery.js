function view_delivery(id){
            document.cookie = "order_id="+id+";Path=/";
            window.location = "/delivery/view_delivery";
        };