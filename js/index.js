// 初始时间与文章内容
T_date = "2022年12月13号"
T_content = "今日无状况"

$(document).ready(function(){
    // 获取时间与文章内容
    $.get("../php/index.php",function(data){
        xx = $.parseJSON(data);
        T_date = xx["date"];
        T_content = xx["content"];
        $("#T_date").children("p").first().text(T_date);
        $("#T_content").children("p").first().text(T_content);
    });
    // 设置样式
    $("#top").addClass("center_text");
    $("#T_title").addClass("center_text");
    $("#T_date").addClass("right_text");
    $("#T_content").addClass("indet_text");
    
    
    // $("#T_content").load("../store/2022-01-03-5666185.txt");
    

    L2Dwidget.init({
        "model": { "jsonPath":"https://unpkg.com/live2d-widget-model-miku@1.0.5/assets/miku.model.json", "scale": 1, "hHeadPos":0.5, "vHeadPos":0.618 },
        "display": { "position": "right", "width": 100, "height": 200, "hOffset": 0, "vOffset": 0 },
        "mobile": { "show": true, "scale": 0.5 },
        "react": { "opacityDefault": 0.7, "opacityOnHover": 0.2 }
      });

})

