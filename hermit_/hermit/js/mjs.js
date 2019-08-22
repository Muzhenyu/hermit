


$(function () {
    // alert("haaaaa")
    // 初始
    // $(".body-nav ul li:first-child").css({"background":"rgb(230, 227, 227)"});
    // 待筛选
    var choose = $(".body-nav ul li");
    choose.mouseover(function () {
        $(this).addClass('lisetcolor-green');
        $(this).removeClass('lisetcolor-black');
    });
    choose.mouseout(function () {
        $(this).removeClass('lisetcolor-green');
        $(this).addClass('lisetcolor-black');
    });

    // 点击筛选
    choose.click(function () {
        $(this).siblings().removeClass('liChoosed');
        $(this).addClass('liChoosed');
    });

    // 随机每日一读
    function soup() {
        var soup_num = Math.floor(Math.random()*10+1);
        var str_soup = "#chicken-soup-";
        str_soup += soup_num;
        $(str_soup).show().siblings('div').hide();
        // $(str_soup).animate({
        //     'margin-top': '-=90px'
        // }, 1000)

    }
    //每日一读初始
    $("#chicken-soup-1").show().siblings('div').hide();
    setInterval(soup, 5000);

    //登录
    $("#login-link").click(function () {
        $("#login-box").show();
        $("#shadow").show();
    });
    //关闭登录框
    $("#close-login-btn").click(function () {
        $("#login-box").hide();
        $("#shadow").hide();
    });


    // $(".login-register-link").click(function(){
    //     $("#set_1").css({'display':'none'})
    //     $("#boss_2").hide()
    //     $("#user_1").css({"display":"inline-block"})
    //     $("#lgin_1").show()
    //     // $(".login-register-link").hide()
    //
    //     // $("#user_1").show()
    //
    // });
    // $("#bye_1").click(function(){
    //     $("#user_1").css({"display":"none"});
    //     $("#set_1").css({'display':'inline-block'})
    //     // $("#user_1").hide()
    //     // $("#set_1").show()
    //
    //
    // });
    //  $(function () {
    //     $('#image1').click(function () {
    //         $('#lgin_1').hide();
    //         $('#boss_2').show();
    //         $("#user_1").css({"display":"none"});
    //         $("#set_1").css({'display':'inline-block'})
    //     });
    //     var phonenum = $('.input1');
    //      phonenum.focus(function () {
    //     $('#null').hide();
    //     $('#erro').hide()
    //     });
    //    phonenum.blur(function () {
    //         var ret=ret =/^1[3,4,5,7,8,][0-9]{9}$/;
    //         if (phonenum.val()=='') {
    //             $('#null').show()
    //
    //         }
    //     else if(ret.test(phonenum.val())){
    //
    //     }
    //     else { $('#erro').show()}
    // })
    //  });
    // $("#btn").click(function() {
    //     // $("#lgin_1").css({"display":"none"})
    //     $("#lgin_1").hide()
    //     // $("#set_1").css({'display':'inline-block'})
    //     $("#boss_2").show()
    // })

    $("#new_1").click(function(){
        $("#boss_1").show();
    })

    
    
});