
$(function () {
    $('#login-btn').click(function () {
        var username=$('#username').val();
        var password=$('#password').val();
        console.log(username);
        console.log(password);
        data={
            'username':username,
            'password':password
        }
        console.log(data);
        var data_str=JSON.stringify(data);
         $.ajax({
            url:'http://127.0.0.1:8000/logining/',
            method:'POST',
            data:data_str,
            contentType:'application/json',
            dataType:'json',
            success:function (data) {
                token = data['token']
                $('#showtoken').text(token)
                localStorage.clear()
                    // clear local storage
                    // sessionStorage #disable when the exploror close
                localStorage.token=token
                    // long term avaliable
                window.location.href='http://127.0.0.1:8080/userinfo.html'
            },
            fail:function (data) {
                console.log(data)
                alert('failed')
            }
        })
    })
    // loginbox()
})