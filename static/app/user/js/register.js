$(function () {

    let $username = $("#username_input");

    $username.change(function () {
        let username = $username.val().trim();
        if (username.length) {
            $.getJSON('/user/checkuser/', {'username': username}, function (data) {
                console.log(data);
                let $username_msg = $("#username_msg");
                if (data["status"] === 200) {
                    $username_msg.html("Valid username").css("color", "green");
                } else if (data["status"] === 901) {
                    $username_msg.html("Username already exists!").css("color", "red");
                }
            });
        }
    });
});

function checkSubmit() {
    let $username = $("#username_input");
    let username = $username.val().trim();
    if (!username) {
        return false;
    }
    let msg_color = $("#username_msg").css("color");
    console.log(msg_color);
    if (msg_color === 'rgb(255, 0, 0)') {
        return false;
    }
    return true;
}
