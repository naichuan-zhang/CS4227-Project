function paypal(){
            document.cookie = "order_id="+id+";Path=/";
            window.location = "/order/paymentcomp";
        };

function show(x, y){
        if(document.getElementById(x).style.display == "none" && document.getElementById(y).style.display != "none"){
            document.getElementById(x).style.display = "block";
            document.getElementById(y).style.display = "none";
        }
        else if(document.getElementById(x).style.display == "none") {
            document.getElementById(x).style.display = "block";
        }
        else{
            document.getElementById(x).style.display = "none";
        }
    };

