$(function(){
    $('#title').focus(function() {
        if ($(this).val()=='给您的推荐地点取一个拉风的名字吧') {
            $(this).val('')
        }
    })
    $('#title').blur(function(){
        if($(this).val()=='') {
            $(this).val('给您的推荐地点取一个拉风的名字吧')
        }
    })
    $('#suggest').focus(function() {
        if ($(this).val()=='写一段简介来介绍以下一个推荐地点吧。'){
            $(this).val('')
        }
    });
    $('#suggest').blur(function(){
        if($(this).val()=='') {
            $(this).val('写一段简介来介绍以下一个推荐地点吧。')
        }
    });
    $('#place_2').focus(function() {
        if ($(this).val()=='点击选择地点'){
            $(this).val('')
        }
    })
    $('#place_2').blur(function(){
        if($(this).val()=='') {
            $(this).val('点击选择地点')
        }
    })
    $('#money_2').focus(function() {
        if ($(this).val()=='人均消费'){
            $(this).val('')
        }
    })
    $('#money_2').blur(function(){
        if($(this).val()=='') {
            $(this).val('人均消费')
        }
    })
    $('#bottom_1').focus(function() {
        if ($(this).val()=='说点什么...'){
            $(this).val('')
        }
    })
    $('#bottom_1').blur(function(){
        if($(this).val()=='') {
            $(this).val('说点什么...')
        }
    })

    $('#book_1').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).css({'color':'black'})
            }
    })
    $('#book_2').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
            }
    })
    $('#book_3').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
            }
    })
    $('#book_4').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().css({'color':'black'})
            }
    })
    $('#book_5').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().prev().css({'color':'black'})
            }
    })
    $('#home_1').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).css({'color':'black'})
            }
    })
    $('#home_2').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
            }
    })
    $('#home_3').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
            }
    })
    $('#home_4').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().css({'color':'black'})
            }
    })
    $('#home_5').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().prev().css({'color':'black'})
            }
    })
    $('#sit_1').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).css({'color':'black'})
            }
    })
    $('#sit_2').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
            }
    })
    $('#sit_3').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
            }
    })
    $('#sit_4').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().css({'color':'black'})
            }
    })
    $('#sit_5').click(function(){
        if($(this).css('color')=='rgb(0, 0, 0)'){
            $(this).css({'color':'red'}).prev().prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().prev().css({'color':'red'})
            $(this).css({'color':'red'}).prev().css({'color':'red'})
        }
        else{
        $(this).css({'color':'black'}).prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().css({'color':'black'})
        $(this).css({'color':'black'}).prev().prev().prev().prev().css({'color':'black'})
            }
    })
    $('#delete_1').click(function(){
        $("#boss_1").hide()
    })
    $("#send_1").click(function(){
        $('#boss_1').hide()
    })
    // $("#delete_1").mouseenter(function(){
    //     $("#delete_1").css("background-color","red")
    // });
    // $("#delete_1").mouseleave(function(){
    //     $("#delete_1").css("background-color","none")
    // });


})