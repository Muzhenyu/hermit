function uuid() {
    /* 这是生成uuid的函数*/
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
};

// var prefix_id = ''
var current_id = '';


function getImageCodeforUser() {
       // 这个函数生成新的uuid，并且在前端中将验证码对应的src替换掉
    var uuid_data = uuid();
    current_id = uuid_data
    $('#img_code img').attr('src','http://127.0.0.1:8000/imgcode/'+uuid_data+'/')
}

function getImageCodeforlibrary() {
       // 这个函数生成新的uuid，并且在前端中将验证码对应的src替换掉
    var uuid_data = uuid();
    current_id = uuid_data
    $('#lib_img_code img').attr('src','http://127.0.0.1:8000/libraries/captcha_aquired/?image_id='+uuid_data)
}

function registerbox(){
    $('#userregister').click(function () {
        $(this).css('border','1px red solid')
        $(this).siblings().css('border','none')
        $('#register-container').html(
            '<div class="form-item">\n' +
        '                <label for="username">用户名</label>\n' +
        '                <input type="text" id="username" name="username" placeholder="用户名">\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <label for="password">密码</label>\n' +
        '                <input type="password" id="password" name="password" placeholder="密码">\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <label for="username">确认密码</label>\n' +
        '                <input type="password" id="cpassword" name="cpassword" placeholder="确认密码">\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <label for="phone">手机号码</label>\n' +
        '                <input type="text" id="phone" name="phone" placeholder="手机号码">\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <label for="email">邮箱</label>\n' +
        '                <input type="text" id="email" name="email" placeholder="邮箱">\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <label for="checkcode">验证码</label>\n' +
        '                <input style="width: 150px" type="text" id="checkcode" name="code" placeholder="验证码">\n' +
        '                <button style="width: 110px;" type="button" class="code-btn" id="code-btn">获取验证码</button>\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <label for=\'msg_code\'>phone验证码</label>\n' +
        '                <input style="width: 150px" type="text" id="msg_code" name="code" placeholder="验证码">\n' +
        '            </div>\n' +
        '            <div id="img_code" class="form-item">\n' +
        '                <img src="#">\n' +
        '            </div>\n' +
        '            <div class="form-item">\n' +
        '                <input type="checkbox" id="checkbox1">\n' +
        '                <span>clicking means you accept user protocal and security protocal</span>\n' +
        '            </div>\n' +
        '\n' +
        '            <div class="form-item">\n' +
        '                <button type="button" class="sub-btn" id="sub-btn">立 即 注 册</button>\n' +
        '            </div>'
        )
        getImageCodeforUser()
         $('#code-btn').click(function () {
        var image_id = current_id

        var image_text  = $('#checkcode').val()
        var phone = $('#phone').val()

        // 2) 将获取到的数据进行正则的校验
        var reg_uuid = /^[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}$/
        var reg_text = /^[\w]{4}$/
        var reg_phone = /^1[3456789]\d{9}$/

        console.log(reg_uuid.exec(image_id))
        console.log(reg_uuid.test(image_id))


        // 3) 利用正则进行校验，如果校验不通过，则返回弹窗
        if(!reg_uuid.test(image_id)){
            alert('图片校验未通过')
        }

        if(!reg_text.test(image_text)){
            alert('验证码校验未通过')
        }

        if(!reg_phone.test(phone)){
            alert('手机号校验未通过')
        }
        msg_url = 'http://127.0.0.1:8000/users/msg_code/?image_id='+image_id+'&image_text='+image_text+'&phone='+phone
        $.ajax({
            url:msg_url,
            method:'GET',
            contentType:'application/json',
            success:function (data) {
                console.log(data)
            },
            error:function (data) {
                console.log(data)
            }
        })
    })
            $('#sub-btn').click(function () {
        var Username=$('#username').val();
        var Password=$('#password').val();
        var V_Password=$('#cpassword').val();
        var Phone=$('#phone').val();
        var Email=$('#email').val();
        var phone_captcha=$('#msg_code').val();
        var checkif=false
        if($('#checkbox1').prop('checked')){
                checkif='good';
        }
        else {
                checkif='bad';
        }
        console.log(checkif);
        if(Password!=V_Password){
            alert('the vertified password is incorrect')
        }
        var data={
            'username':Username,
            'password':Password,
            'v_password':V_Password,
            'phone':Phone,
            'email':Email,
            'msg_code':phone_captcha,
            'protocal':checkif,
        }
        console.log(data)

        var data_str=JSON.stringify(data);
        console.log(data_str)  ;
        $.ajax({
                url:'http://127.0.0.1:8000/register/',
                method:'POST',
                data:data_str,
                contentType:'application/json',
                dataType:'json',
                success:function (data) {
                    alert('successed')
                    console.log(data)
                    console.log(typeof(data))
                    token=data['token']
                    alert(token)
                    localStorage.clear()
                    // clear local storage
                    // sessionStorage #disable when the exploror close
                    localStorage.token=token

                    // long term avaliable
                    alert(localStorage.token)
                    // location.href='http://127.0.0.1:8080'
                    window.location.href='http://127.0.0.1:8080/userinfo.html'
                },
                error:function (data) {
                    alert('failed')
                    console.log(data)
                }
            })
    })


    })
    $('#libuserregister').click(function () {
        $(this).css('border','1px red solid')
        $(this).siblings().css('border','none')
        $('#register-container').html(
        '            <div class="form-item">\n' +
            '                <label for="username">用户名</label>\n' +
            '                <input type="text" id="lib_username" name="username" placeholder="用户名">\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <label for="password">密码</label>\n' +
            '                <input type="password" id="lib_password" name="password" placeholder="密码">\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <label for="username">确认密码</label>\n' +
            '                <input type="password" id="lib_cpassword" name="cpassword" placeholder="确认密码">\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <label for="phone">手机号码</label>\n' +
            '                <input type="text" id="lib_phone" name="phone" placeholder="手机号码">\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <label for="email">邮箱</label>\n' +
            '                <input type="text" id="lib_email" name="email" placeholder="邮箱">\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <label for="checkcode">验证码</label>\n' +
            '                <input style="width: 150px" type="text" id="lib_checkcode" name="code" placeholder="验证码">\n' +
            '                <button style="width: 110px;" type="button" class="code-btn" id="lib_code-btn">获取验证码</button>\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <label for=\'msg_code\'>phone验证码</label>\n' +
            '                <input style="width: 150px" type="text" id="lib_msg_code" name="code" placeholder="验证码">\n' +
            '            </div>\n' +
            '            <div id="lib_img_code" class="form-item">\n' +
            '                <img src="#">\n' +
            '            </div>\n' +
            '            <div class="form-item">\n' +
            '                <input type="checkbox" id="lib_checkbox1">\n' +
            '                <span>clicking means you accept user protocal and security protocal</span>\n' +
            '            </div>\n' +
            '\n' +
            '            <div class="form-item">\n' +
            '                <button type="button" class="sub-btn" id="lib_sub-btn">立 即 注 册</button>\n' +
            '            </div>'
        )
            getImageCodeforlibrary()
        $('#lib_code-btn').click(function () {
        var image_id = current_id

        var image_text  = $('#lib_checkcode').val()
        var phone = $('#lib_phone').val()

        // 2) 将获取到的数据进行正则的校验
        var reg_uuid = /^[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}$/
        var reg_text = /^[\w]{4}$/
        var reg_phone = /^1[3456789]\d{9}$/

        console.log(reg_uuid.exec(image_id))
        console.log(reg_uuid.test(image_id))


        // 3) 利用正则进行校验，如果校验不通过，则返回弹窗
        if(!reg_uuid.test(image_id)){
            alert('图片校验未通过')
        }

        if(!reg_text.test(image_text)){
            alert('验证码校验未通过')
        }

        if(!reg_phone.test(phone)){
            alert('手机号校验未通过')
        }
        msg_url = 'http://127.0.0.1:8000/libraries/msg_code_aquire/?image_id='+image_id+'&image_text='+image_text+'&phone='+phone
        $.ajax({
            url:msg_url,
            method:'GET',
            contentType:'application/json',
            success:function (data) {
                console.log(data)
            },
            error:function (data) {
                console.log(data)
            }
        })
    })
        $('#lib_sub-btn').click(function () {
        var Username=$('#lib_username').val();
        var Password=$('#lib_password').val();
        var V_Password=$('#lib_cpassword').val();
        var Phone=$('#lib_phone').val();
        var Email=$('#lib_email').val();
        var phone_captcha=$('#lib_msg_code').val();
        var checkif=false;
        var is_library=true
        if($('#lib_checkbox1').prop('checked')){
                checkif='good';
        }
        else {
                checkif='bad';
        }
        console.log(checkif);
        if(Password!=V_Password){
            alert('the vertified password is incorrect')
        }
        var data={
            'username':Username,
            'password':Password,
            'v_password':V_Password,
            'phone':Phone,
            'email':Email,
            'msg_code':phone_captcha,
            'protocal':checkif,
            'is_library':is_library
        }
        console.log(data)

        var data_str=JSON.stringify(data);
        console.log(data_str)  ;
        $.ajax({
                url:'http://127.0.0.1:8000/libraries/register',
                method:'POST',
                data:data_str,
                contentType:'application/json',
                dataType:'json',
                success:function (data) {
                    alert('successed')
                    console.log(data)
                    console.log(typeof(data))
                    token=data['token']
                    localStorage.clear()
                    // clear local storage
                    // sessionStorage #disable when the exploror close
                    localStorage.token=token

                    // long term avaliable
                    alert(localStorage.token)
                    window.location.href='http://127.0.0.1:8080/userinfo.html'
                },
                error:function (data) {
                    alert('failed')
                    console.log(data)
                }
            })
    })
    })
}
$(function () {
    getImageCodeforUser()
    $('#userregister').css('border','1px red solid')
    $('#code-btn').click(function () {

        var image_id = current_id

        var image_text  = $('#checkcode').val()
        var phone = $('#phone').val()

        // 2) 将获取到的数据进行正则的校验
        var reg_uuid = /^[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}$/
        var reg_text = /^[\w]{4}$/
        var reg_phone = /^1[3456789]\d{9}$/

        console.log(reg_uuid.exec(image_id))
        console.log(reg_uuid.test(image_id))


        // 3) 利用正则进行校验，如果校验不通过，则返回弹窗
        if(!reg_uuid.test(image_id)){
            alert('图片校验未通过')
        }

        if(!reg_text.test(image_text)){
            alert('验证码校验未通过')
        }

        if(!reg_phone.test(phone)){
            alert('手机号校验未通过')
        }
        msg_url = 'http://127.0.0.1:8000/users/msg_code/?image_id='+image_id+'&image_text='+image_text+'&phone='+phone
        $.ajax({
            url:msg_url,
            method:'GET',
            contentType:'application/json',
            success:function (data) {
                console.log(data)
            },
            error:function (data) {
                console.log(data)
            }
        })
    })
    $('#sub-btn').click(function () {
        var Username=$('#username').val();
        var Password=$('#password').val();
        var V_Password=$('#cpassword').val();
        var Phone=$('#phone').val();
        var Email=$('#email').val();
        var phone_captcha=$('#msg_code').val();
        var checkif=false
        if($('#checkbox1').prop('checked')){
                checkif='good';
        }
        else {
                checkif='bad';
        }
        if(Password!=V_Password){
            alert('the vertified password is incorrect')
        }
        var data={
            'username':Username,
            'password':Password,
            'v_password':V_Password,
            'phone':Phone,
            'email':Email,
            'msg_code':phone_captcha,
            'protocal':checkif,
        }

        var data_str=JSON.stringify(data);
        console.log(data_str)  ;
        $.ajax({
                url:'http://127.0.0.1:8000/register/',
                method:'POST',
                data:data_str,
                contentType:'application/json',
                dataType:'json',
                success:function (data) {
                    alert('successed')
                    console.log(data)
                    console.log(typeof(data))
                    token=data['token']
                    alert(token)
                    localStorage.clear()
                    // clear local storage
                    // sessionStorage #disable when the exploror close
                    localStorage.token=token

                    // long term avaliable
                    alert(localStorage.token)
                    window.location.href='http://127.0.0.1:8080/userinfo.html'
                },
                error:function (data) {
                    alert('failed')
                    console.log(data)
                }
            })
    })
    registerbox()

})