// JavaScript Document
$(document).ready(function () {
    //展开和关闭
    $(".dispaly h4").each(function (index) {
        $(this).click(function () {
            if ($(".content_hide").eq(index).css("display") == "none") {
                $(".content_hide").eq(index).show();
                $(".content_hide").eq(index).addClass("show_it");
                $(".dispaly img").eq(index).attr("src", "../static/2_03.png");
            } else {
                $(".content_hide").eq(index).hide();
                $(".dispaly img").eq(index).attr("src", "../static/1_03.png");
            }
        });
    });

    //获取API详情 div片段
    api_details = function (api_id) {
        //alert(api_id);
        $.ajax({
            type: "GET",
            url: "api/" + api_id,
            contentType: "application/x-www-form-urlencoded;",
            success: function (data) {
                $("#api_details").html(data);
            }
        });
    };
});
