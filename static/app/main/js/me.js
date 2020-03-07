$(function () {

    $("#not_login").click(function () {
        window.open('/user/login/', target="_self");
    });

    $("#register").click(function () {
        window.open('/user/register/', target='_self');
    })
});
