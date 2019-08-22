$(function () {
    token=localStorage.token
    $.ajax({
        url:'http://127.0.0.1:8000/loginuser/',
        method:'GET',
        headers:{
            'Authorization':'JWT '+token
        },
        success(data){
            var is_library=data.is_library

            address()
            addUseraddress(token)
            $('#cusername').text(data.username)
            $('#email').text(data.email)
            $('#usericon').attr({'src':'http://127.0.0.1:8888/'+data.img_url})
            id1=data.id
            email1=data.email
            active_email(id1,email1,token)
            changeusericon(token)
            userlibrary(token,is_library)
            usercollectlib(token)
            userinfo(token)
            library_explore_manager(token)
        },
        error(data){
            if(data['status']==401) {
                window.location.href = 'http://127.0.0.1:8080'
            }
        },
    })

    listaddress(token)
})
function address() {
    $('#get_district').click(function () {
        $.ajax({
            url:'http://127.0.0.1:8000/areas/areas',
            method:'GET',
            success(data){
                adddistrictdata(data)
                clickdistrictsibling(data)
            }
        })
    })
}
function adddistrictdata(data) {
    $('#district').html(
        '<li class="first_level"><input type="button" value="地区" id="get_district"></li>'+
        fordistrictlist(data)
    )
}
function fordistrictlist(data) {
    var a=''
    for(var i=0;i<data.length;i++){
         a=a+'<li class="first_level"><span><input type="button" value="'+data[i].name+'" id="'+data[i].id+'"></span><li>'
        }

    return a
}
function clickdistrictsibling(datax){
    $('#district li span').children().click(function () {
        var id=$(this).attr('id')
        var valued=$(this).attr('value')
        $('#district').html('<li class="first_level"><input type="button" value="'+valued+'" id="'+id+'"><li>')
        updatedistrict(datax)
        var new_url='http://127.0.0.1:8000/areas/areas/'+id
        $.ajax({
            url:new_url,
            method:'GET',
            success(data) {
                $('#street').html('<li class="second_level"><input type="button" value="街道" id="get_street"></li>')
                $('#get_street').click(function () {
                   addstreetdata(data.addinfos)
                    clickstreetsibling(data.addinfos)
                })
            }
        })
    })
}
function updatedistrict(data) {
    $('#district li input').click(function () {
            adddistrictdata(data)
            clickdistrictsibling(data)
        })

}
function addstreetdata(data) {
    $('#street').html(
        '<li class="second_level"><input type="button" value="街道" id="get_street"></li>'+
        forstreetlist(data)
    )
}
function forstreetlist(data) {
    var a=''
    for(var i=0;i<data.length;i++){
         a=a+'<li class="second_level"><span><input type="button" value="'+data[i].name+'" id="'+data[i].id+'"></span><li>'
        }
    return a
}
function clickstreetsibling(data){
    $('#street li span').children().click(function () {
        var id = $(this).attr('id')
        var valued = $(this).attr('value')
        $('#street').html('<li class="second_level"><input type="button" value="' + valued + '" id="' + id + '"><li>')
        updatestreet(data)

    })
}
function updatestreet(data) {
    $('#street li input').click(function () {
        addstreetdata(data)
        clickstreetsibling(data)
    })
}
function addUseraddress(token) {
    $('#upload_address').click(function () {
        district_id=$('#district li input').attr('id')
        street_id=$('#street li input').attr('id')
        console.log('dis',district_id,'str',street_id)
        if(district_id=='get_district'||street_id=='get_street'){
            alert('bad request')
        }

        else {
            data={
            'district_id':district_id,
            'street_id':street_id
        }
        var data_str=JSON.stringify(data)
            $.ajax({
                headers:{
                    'Authorization':'JWT '+token
                },
                url:'http://127.0.0.1:8000/addresses/',
                method:'POST',
                data:data_str,
                contentType: 'application/json',
                dataType:'json',
                success(data){
                    console.log(data)
                }
            })
        }
    })
}



function listaddress(token) {
    $.ajax({
        method:'GET',
        headers:{
            'Authorization':'JWT '+token
        },
        url:'http://127.0.0.1:8000/addresses/',
        dataType: 'json',
        contentType: 'application/json',
        success(data) {
            showUseraddresses(data.address)
        }
    })
}
function showUseraddresses(data) {
    $('#addresses-box').html(
        getaddresseslist(data)
    )
}
function getaddresseslist(data) {
    a=''
    for(var i=0;i<data.length;i++){
       a=a+'<li><span id="showdistrict">'+data[i].district+'</span><span id="showstreet">'+data[i].street+'</span></li>'
    }
    return a
}



function active_email(id,email,token) {
    $('#active_button').click(function () {
        $.ajax({
            url:'http://127.0.0.1:8000/email/',
            headers:{
                'Authorization':'JWT '+token
            },
            type:'PUT',
            data: {
                _method: 'PUT',
                id:id1,
                email:email1
            },
            dataType:'json',
            success:function () {
                alert('okay')
            }
        })
    })
}



function changeusericon(token) {
    $('#usericon').click(function () {
        $('#hide_box').css({'display':'block','position':'absolute','left':'50%','right':'50%','transform':'translate(-50%,-50%)','backgroud':'wheat'})
        $('#icon_upload').click(function () {
            var img=$('#icon_img')[0].files[0]
            data={'img':img}
            var formdata=new FormData()
            formdata.append('img',img)
            console.log(formdata)
            $.ajax({
                headers:{
                    'Authorization':'JWT '+token
                },
                method:'POST',
                data:formdata,
                processData:false,
                contentType:false,
                dataType: 'json',
                url:'http://127.0.0.1:8000/usericon',
                success(data){
                    $('#usericon').attr({'src':'http://127.0.0.1:8888/'+data})
                    $('#hide_box').css('display','none')
                },
                error(data) {
                    alert('failure')
                }
            })
        })
    })

}



function userlibrary(token,islibrary) {
    $('#userlibrary').click(function () {
        if(islibrary==true){
            $.ajax({
                method:'GET',
                url:'http://127.0.0.1:8000/libraries/showuserlibs',
                headers:{
                    'Authorization':'JWT '+token
                },
                success(data){
                    if(isempty(data[0])){
                        aquirecreatelibraryinfo()
                        submitinfo(token)
                    }
                    else{
                        showlibinfo(data[0])
                    }
                }
            })
        }
        else {
            $('#info-box').html(
                '<div class="userdetailinfo">需要先成为一个图书馆用户</div>'
            )
        }
    })
}
function isempty(obj) {
    for(var key in obj){
        return false
    }
    return true
}
function aquirecreatelibraryinfo(){
    $('#info-box').html(
        info_box_createlib_html()
    )
    acquirelibtype()
    libaddress()
}
function info_box_createlib_html(){
    html='<div class="userdetailinfo"><span>图书馆名</span><input type="text" id="lib_name"></div>\n'+
        '<div class="userdetailinfo"><span>图书馆地址</span></div>\n'+
        '<div class="userdetailinfo">\n' +
        '        <div class="add_address"><ul id="lib_district"><li class="first_level"><input type="button" value="地区" id="lib_get_district"></li></ul></div>\n' +
        '        <div class="add_address"><ul id="lib_street"><li class="second_level"><input type="button" value="街道" id="lib_get_street"></li></ul></div>\n' +
        '    </div>'+
        '<div class="userdetailinfo"><span>详细地址</span><input type="text" id="lib_detail_address"></div>\n'+
        '<div class="userdetailinfo"><span>图书馆图片</span><input type="file" id="lib_img"></div>\n'+
        '<div class="userdetailinfo"><span>图书馆营业执照</span><input type="file" id="lib_license_img"></div>\n'+
        '<div class="userdetailinfo"><span>图书馆简介</span><input type="text" id="lib_commit"></div>\n'+
        '<div class="userdetailinfo"><span>图书馆价格</span><input type="text" id="lib_price"></div>\n'+
        '<div class="userdetailinfo"><ul id="lib_type"><li id="select_libtype"><input type="button" value="请选择类型"></li></ul></div>\n'+
        '<div class="userdetailinfo"><input type="button" id="lib-sub" value="上传/更新"></div>\n'
    return html
}
function submitinfo(token) {
    $('#lib-sub').click(function () {
        var name=$('#lib_name').val()
        var district_id=$('#lib_district li input').attr('id')
        var street_id=$('#lib_street li input').attr('id')
        var detail_address=$('#lib_detail_address').val()
        var lib_commit=$('#lib_commit').val()
        var lib_price=$('#lib_price').val()
        var lib_img=$('#lib_img')[0].files[0]
        var lib_license=$('#lib_license_img')[0].files[0]
        var type=$('#lib_type li span input').attr('id')
        console.log(type)
        data={
            'name':name,
            'district_id':district_id,
            'street_id':street_id,
            'detail_address':detail_address,
            'lib_commit':lib_commit,
            'lib_img':lib_img,
            'lib_license':lib_license,
            'type':type
        }
        var form_data=new FormData()
        form_data.append('name',name)
        form_data.append('district',Number(district_id))
        form_data.append('street',Number(street_id))
        form_data.append('detail_address',detail_address)
        form_data.append('lib_commit',lib_commit)
        form_data.append('price',lib_price)
        form_data.append('lib_img',lib_img)
        form_data.append('lib_license',lib_license)
        form_data.append('type',type)
        form_data.append('page_mode_id',1)
        $.ajax({
            method:'POST',
            headers:{
                    'Authorization':'JWT '+token
                },
            url:'http://127.0.0.1:8000/libraries/createlib/',
            data:form_data,
            processData:false,
            contentType:false,
            dataType: 'json',
            success(data) {
                location.reload()
            },
            error(data){
              console.log(data)
            }
        })
    })


}
function libaddress() {
    $('#lib_get_district').click(function () {
        $.ajax({
            url:'http://127.0.0.1:8000/areas/areas',
            method:'GET',
            success(data){
                libadddistrictdata(data)
                libclickdistrictsibling(data)
            }
        })
    })
}
function libadddistrictdata(data) {
    $('#lib_district').html(
        '<li class="first_level"><input type="button" value="地区" id="lib_get_district"></li>'+
        libfordistrictlist(data)
    )
}
function libfordistrictlist(data) {
    var a=''
    for(var i=0;i<data.length;i++){
         a=a+'<li class="first_level"><span><input type="button" value="'+data[i].name+'" id="'+data[i].id+'"></span><li>'
        }

    return a
}
function libclickdistrictsibling(datax){
    $('#lib_district li span').children().click(function () {
        var id=$(this).attr('id')
        var valued=$(this).attr('value')
        $('#lib_district').html('<li class="first_level"><input type="button" value="'+valued+'" id="'+id+'"><li>')
        libupdatedistrict(datax)
        var new_url='http://127.0.0.1:8000/areas/areas/'+id
        $.ajax({
            url:new_url,
            method:'GET',
            success(data) {
                $('#lib_street').html('<li class="second_level"><input type="button" value="街道" id="lib_get_street"></li>')
                $('#lib_get_street').click(function () {
                   libaddstreetdata(data.addinfos)
                    libclickstreetsibling(data.addinfos)
                })
            }
        })
    })
}
function libupdatedistrict(data) {
    $('#lib_district li input').click(function () {
            libadddistrictdata(data)
            libclickdistrictsibling(data)
        })

}
function libaddstreetdata(data) {
    $('#lib_street').html(
        '<li class="second_level"><input type="button" value="街道" id="lib_get_street"></li>'+
        libforstreetlist(data)
    )
}
function libforstreetlist(data) {
    var a=''
    for(var i=0;i<data.length;i++){
         a=a+'<li class="second_level"><span><input type="button" value="'+data[i].name+'" id="'+data[i].id+'"></span><li>'
        }
    return a
}
function libclickstreetsibling(data){
    $('#lib_street li span').children().click(function () {
        var id = $(this).attr('id')
        var valued = $(this).attr('value')
        $('#lib_street').html('<li class="second_level"><input type="button" value="' + valued + '" id="' + id + '"><li>')
        libupdatestreet(data)
    })
}
function libupdatestreet(data) {
    $('#lib_street li input').click(function () {
        libaddstreetdata(data)
        libclickstreetsibling(data)
    })
}
function showlibinfo(data) {
    $('#info-box').html(showlibinfo_html(data))
    updatalibinfohtml(data)
}
function showlibinfo_html(lib_data) {
    html='<div class="userdetailinfo" style="position: absolute;left: 10px"><span>图书馆名:</span><span>'+lib_data.name+'</span></div>'+
   '<div class="userdetailinfo" style="position: absolute;left:10px;top:100px"><span>图书馆地址:</span><span>'+lib_data.district+'</span><span>'+lib_data.street+'</span><span>'+lib_data.detail_address+'</span></div>'+
   '<div class="userdetailinfo" style="position: absolute;left:500px;top:20px"><div style="position:relative;left: 80px">图书馆封面</div><img src="http://127.0.0.1:8888/'+lib_data.lib_img_url+'" style="width: 250px;height:250px"></div>'+
   '<div class="userdetailinfo" style="position: absolute;left:10px;top:200px"><span>图书馆评分:</span><span>'+lib_data.grade+'</span></div>'+
   '<div class="userdetailinfo" style="position: absolute;left:10px;top:300px"><span>图书馆详细信息:</span><span>'+lib_data.lib_commit+'</span></div>'+
   '<div class="userdetailinfo" style="position: absolute;left:500px;top:400px"><div style="position:relative;left: 80px">营业执照</div><img src="http://127.0.0.1:8888/'+lib_data.lib_license_url+'" style="height: 250px;width: 250px"></div>'+
   '<div class="userdetailinfo" style="position: absolute;left:30px;top:400px"><div style="position:relative;left: 160px">图书馆缩略图</div><img src="http://127.0.0.1:8888/'+lib_data.lib_license_url+'" style="height: 80px;width: 80px"></div>'+
    '<div class="userdetailinfo" style="position: absolute;left:300px;top:770px"><input id="update_lib_info" value="更新信息" type="button"></div>'
    return html
}
function acquirelibtype(){
    $.ajax({
        method:'GET',
        url:'http://127.0.0.1:8000/libraries/getlibtype',
        success(data){
            console.log(data)
            acquirelibtypehtml(data)
            acquirelibtypeclickevent(data)
        }
    })

}
function acquirelibtypehtml(data){
    $('#lib_type').html(acquirelibtypehtmlstr(data))
}
function acquirelibtypehtmlstr(data) {
    a='<li id="select_libtype"><span><input type="button" value="请选择类型" id="0"></span></li>'
    for(var i=0;i<data.length;i++){
        a=a+'<li style="display: none"><span><input type="button" id="'+data[i].id+'" value="'+data[i].type_name+'"></span></li>'
    }
    return a
}
function acquirelibtypeclickevent(data) {

    $('#select_libtype').click(function () {
        $('#lib_type li').css('display','block')
        $('#lib_type li span').children().click(function () {
            var id=$(this).attr('id')
            var name=$(this).attr('value')
            $('#lib_type').html('<li><span><input type="button" id="'+id+'" value="'+name+'"></span></li>')
            updatalibtype(data)
        })

    })
}
function updatalibtype(data) {
    $('#lib_type li span input').click(function () {
        updatelibtypehtml(data)
        updatelibtypeclickevent(data)
    })
}
function updatelibtypehtml(data){
    $('#lib_type').html(updatelibtypehtmlstr(data))
}
function updatelibtypehtmlstr(data) {
    a='<li id="select_libtype"><span><input type="button" value="请选择类型" id="0"></span></li>'
    for(var i=0;i<data.length;i++){
        a=a+'<li><span><input type="button" id="'+data[i].id+'" value="'+data[i].type_name+'"></span></li>'
    }
    return a

}
function updatelibtypeclickevent(data) {
    $('#lib_type li span').children().click(function () {
        var id=$(this).attr('id')
        var name=$(this).attr('value')
        $('#lib_type').html('<li><span><input type="button" id="'+id+'" value="'+name+'"></span></li>')
        updatalibtype(data)
    })
}
function updatalibinfohtml(data){
    $('#update_lib_info').click(function () {
        $('#info-box').html(
        info_box_createlib_html()
            +'<div class="userdetailinfo">在此页面填空值默认为不更新</div>'
        )
        acquirelibtype()
        libaddress()
        updatalibinfo()
    })
}
function updatalibinfo() {
    $('#lib-sub').click(function () {
        var name=$('#lib_name').val()
        var district_id=$('#lib_district li input').attr('id')
        var street_id=$('#lib_street li input').attr('id')
        var detail_address=$('#lib_detail_address').val()
        var lib_commit=$('#lib_commit').val()
        var lib_price=$('#lib_price').val()
        var lib_img=$('#lib_img')[0].files[0]
        var lib_license=$('#lib_license_img')[0].files[0]
        var type=$('#lib_type li span input').attr('id')
        if(district_id=='lib_get_district'){district_id=''}
        if(street_id=='lib_get_street'){street_id=''}
        if(isempty(lib_license))(lib_license='')
        if(isempty(lib_img))(lib_img='')
        if(type==0){type=''}
        var token=localStorage.token
        var form_data=new FormData()
        form_data.append('name',name)
        form_data.append('district',district_id)
        form_data.append('street',street_id)
        form_data.append('detail_address',detail_address)
        form_data.append('lib_commit',lib_commit)
        form_data.append('price',lib_price)
        form_data.append('lib_img',lib_img)
        form_data.append('lib_license',lib_license)
        form_data.append('type',type)
        form_data.append('page_mode_id',1)
        $.ajax({
            method:'POST',
            headers:{
                    'Authorization':'JWT '+token
                },
            url:'http://127.0.0.1:8000/libraries/updatauserlibrary',
            data:form_data,
            processData:false,
            contentType:false,
            dataType: 'json',
            success(data) {

            },
            error(data){
              console.log(data)
            }
        })
    })
}


function usercollectlib(token) {
    $('#collectionlist').click(function () {
        $.ajax({
            method:'GET',
            url:"http://127.0.0.1:8000/usercollection",
            headers:{
                'Authorization':'JWT '+token
            },
            success(data) {
            usercollectlibhtml(data)
            },
        })
    })
}
function usercollectlibhtml(data){
    if(isempty(data)){$('#info-box').html('<div>没有收藏的图书馆，快去找一个吧</div>')}
    else {$('#info-box').html('<ul id="librarylist">'+usercollectlibhtmlstr(data)+'</ul>')}
}
function usercollectlibhtmlstr(data) {
    a=''

    for(i=0;i<data.length;i++){
            a=a+'    <li>\n' +
                '<a href="http://127.0.0.1:8080/'+data[i].lib_info_url+'" target="_blank">'+
    '                <div class="item">\n' +
    '                    <img src="http://127.0.0.1:8888/'+data[i].lib_img_url+'" style="width: 140px;height: 170px">'+
    '                    <div class="item-info">\n' +
    '                            <h3>'+data[i].name+'</h3>\n' +
    '                        <!-- <span>杭州高新区&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.8KM</span>\n' +
    '                        <br> -->\n' +
    '                        <p style="height: 21px;">\n' +
    '                            <span style="float: left;">'+data[i].district+'</span>\n' +
    '                            <span style="float: right;">'+data[i].street+'</span>\n' +
    '                        </p>\n' +
    '                        <p>整体评分：'+data[i].grade+'分</p>\n' +
    '                        <p>价格:'+data[i].price+'</p>\n' +
    '                        <p>简介：'+data[i].lib_commit+'</p>\n' +
    '                    </div>\n' +
    '                </div>\n' +
                '</a>'
    '            </li>'
    }
    return a
}


function userinfo(token){
    $('#userinfo').click(function () {
        $.ajax({
            url: 'http://127.0.0.1:8000/loginuser/',
            method: 'GET',
            headers: {
                'Authorization': 'JWT ' + token
            },
            success(data){
                userinfohtml(data)
                address()
                addUseraddress(token)
            }
        })
        listaddress(token)
    })
}
function userinfohtml(data) {
    $('#info-box').html('    <div class="userdetailinfo"><span style="margin-right: 10px">email:</span><span id="email">'+data.email+'</span><input type="button" id="active_button" value="邮箱激活"></div>\n' +
        '    <div class="userdetailinfo" ><div style="margin-right: 10px">地址:</div ><ul id="addresses-box"></ul></div>\n' +
        '    <div class="userdetailinfo">\n' +
        '        <div class="add_address"><ul id="district"><li class="first_level"><input type="button" value="地区" id="get_district"></li></ul></div>\n' +
        '        <div class="add_address"><ul id="street"><li class="second_level"><input type="button" value="街道" id="get_street"></li></ul></div>\n' +
        '        <div class="add_address"><ul><li><input type="button" value="上传地址" id="upload_address"></li></ul></div>\n' +
        '    </div>')
}

function library_explore_manager(token){

    $('#libraryexplore').click(function () {

        $('#info-box').attr('_echarts_instance_','')
        $.ajax({
            type: "GET",
            headers:{
                'Authorization':'JWT '+token
            },
            url: "http://127.0.0.1:8000/libraries/analysisexplore/",
            dataType: 'json',
            success: function (result) {
                var chart = echarts.init(document.getElementById('info-box'), 'white', {renderer: 'canvas'});
                chart.clear()
                chart.setOption(result.data,true)

            }
        });
    })
}
