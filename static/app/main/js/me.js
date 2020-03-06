$(function () {

    $("#not_login").click(function () {
        window.open('/app/login/', target="_self");
    });

    $("#register").click(function () {
        window.open('/app/register/', target='_self');
    })
});
