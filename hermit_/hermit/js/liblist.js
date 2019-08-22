$(function () {
    $.ajax({
        url:'http://127.0.0.1:8000/libraries/showlibs/',
        method:'GET',
        dataType:'json',
        contentType:'application/json',
        success(data){
            console.log(data)
            changehtml(data)
        }
    })
    searchcontext()
})
function isempty(obj) {
    for(var key in obj){
        return false
    }
    return true
}


function changehtml(data){
    if(isempty(data)){$('#main_search_box').html('<div>找不到需要的图书馆了哦</div>')}
    else {$('#main_search_box').html('<ul id="librarylist">'+getlist(data)+'</ul>')}
}
function getlist(data) {
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

function searchcontext() {
    libtypesearchlist()
    districtsearchlist()
    streetsearchlist()
    pricecondition()
}
function libtypesearchlist(){
    $.ajax({
        method:'GET',
        url:'http://127.0.0.1:8000/libraries/getlibtype',
        success(data){
            libtypesearchlisthtml(data)
            libtypesearchlistclickevent()
        }
    })
}
function libtypesearchlisthtml(data) {
    $('#libtypesearchlist').html(
        '<li id="0">不限</li>'+
        libtypesearchlisthtmlstr(data)
    )
}
function libtypesearchlisthtmlstr(data) {
    a=''
    for(var i=0;i<data.length;i++){

        html_str='<li id="'+data[i].id+'">'+data[i].type_name+'</li>'
        a=a+html_str
    }
    return a
}
function libtypesearchlistclickevent(){
    var id
    $('#libtypesearchlist').children().click(function () {
        id=$(this).attr('id')
        var url=searchurl(id,'','','')
        if(id!='0'){
            $('#'+libtype_id).siblings().css('border','none')
            $('#'+libtype_id).css('border','1px red solid')
        }
        if(id=='0') {
            $('#libtypesearchlist').children().css('border', 'none')
        }
        $.ajax({
            method:'GET',
            url:url,
            success(data) {
                console.log(data)
                changehtml(data)
            }
        })
    })
}
function districtsearchlist() {
    $.ajax({
        url:'http://127.0.0.1:8000/areas/district',
        method:'GET',
        dataType: 'json',
        contentType: 'application/json',
        success(data){
            districtsearchlisthtml(data)
            districtsearchlistclickevent()
        }
    })
}
function districtsearchlisthtml(data) {
    $('#districtsearchlist').html(
        '<li id="000000">不限</li>'+
        districtsearchlisthtmlstr(data)
    )
}
function districtsearchlisthtmlstr(data) {
    a=''
    for(var i=0;i<data.length;i++){
        html_str='<li id="'+data[i].id+'">'+data[i].name+'</li>'
        a=a+html_str
    }
    return a
}
function districtsearchlistclickevent() {
    var id
    $('#districtsearchlist').children().click(function () {
        id=$(this).attr('id')
        street_id=''
        var url=searchurl('',districtsearch_id=id,'','')
        if(id!='000000'){
            $('#'+district_id).siblings().css('border','none')
            $('#'+district_id).css('border','1px red solid')
            $.ajax({
                method:'GET',
                url:'http://127.0.0.1:8000/areas/areas/'+id,
                success(data){
                    streetsearchlisthtml(data.addinfos)
                    streetsearchlistclickevent()
                }
            })
        }
        if(id=='000000') {
            $('#districtsearchlist').children().css('border','none')
            $('#streetsearchlist').children().css('border','none')
            streetsearchlist()
        }
        $.ajax({
            method:'GET',
            url:url,
            success(data) {
                console.log(data)
                changehtml(data)
            }
        })
    })
}
function streetsearchlist() {
    $.ajax({
        url:'http://127.0.0.1:8000/areas/street',
        method:'GET',
        dataType: 'json',
        contentType: 'application/json',
        success(data){
            streetsearchlisthtml(data)
            streetsearchlistclickevent()
        }
    })
}
function streetsearchlisthtml(data) {
    $('#streetsearchlist').html(
        '<li id="00000000">不限</li>'+
        streetsearchlisthtmlstr(data)
    )
}
function streetsearchlisthtmlstr(data) {
    a=''
    for(var i=0;i<data.length;i++){
        html_str='<li id="'+data[i].id+'">'+data[i].name+'</li>'
        a=a+html_str
    }
    return a
}
function streetsearchlistclickevent() {
    var id
    $('#streetsearchlist').children().click(function () {
        id=$(this).attr('id')
        var url=searchurl('','',streetsearch_id=id,'')
        if(id!='00000000'){
            $('#'+street_id).siblings().css('border','none')
            $('#'+street_id).css('border','1px red solid')
            $('#'+district_id).siblings().css('border','none')
            $('#'+district_id).css('border','1px red solid')
        }
        if(id=='00000000') {
            $('#streetsearchlist').children().css('border','none')
        }
        $.ajax({
            method:'GET',
            url:url,
            success(data) {
                console.log(data)
                changehtml(data)
            }
        })
    })
}
function pricecondition() {
    $('#pricesearchlist').children().click(function () {
        var price_tag=$(this).text()
        console.log(price_tag)
        console.log(price)
        var url=searchurl('','','',price_tag)
        $.ajax({
            method:'GET',
            url:url,
            success(data) {
                console.log(data)
                changehtml(data)
            }
        })
    })
}
var libtype_id=''
var district_id=''
var street_id=''
var price=''
function searchurl(libtypesearch_id='',districtsearch_id='',streetsearch_id='',price_tag='') {

    if(streetsearch_id==''&&districtsearch_id==''&&price_tag==''&&libtypesearch_id!=''&&libtypesearch_id!='0'){
        libtype_id=libtypesearch_id
    }
    if(streetsearch_id==''&&districtsearch_id==''&&price_tag==''&&libtypesearch_id=='0'){libtype_id=''}
    // if(streetsearch_id==''&&districtsearch_id==''&&libtypesearch_id==''){libtype_id=libtype_id}
    if(streetsearch_id==''&&libtypesearch_id==''&&price_tag==''&&districtsearch_id!=''&&districtsearch_id!='000000'){district_id=districtsearch_id}
    if(streetsearch_id==''&&libtypesearch_id==''&&price_tag==''&&districtsearch_id=='000000'){district_id=''}
    // if(streetsearch_id==''&&libtypesearch_id==''&&districtsearch_id==''){district_id=district_id}
    if(districtsearch_id==''&&libtypesearch_id==''&&price_tag==''&&streetsearch_id!=''&&streetsearch_id!='00000000') {
        street_id=streetsearch_id
        re=/\d{6}/
        district_id=street_id.match(re)[0]
    }
    if(districtsearch_id==''&&libtypesearch_id==''&&price_tag==''&&streetsearch_id=='00000000'){street_id=''}
    // if(districtsearch_id==''&&libtypesearch_id==''&&streetsearch_id==''){street_id=street_id}
    if(libtypesearch_id==''&&districtsearch_id==''&&streetsearch_id==''&&price_tag=='不限'){price=''}
    if(libtypesearch_id==''&&districtsearch_id==''&&streetsearch_id==''&&price_tag!='不限'&&price_tag!=''){price=price_tag}

    var url='http://127.0.0.1:8000/libraries/searchliblist/?libtypesearch_id='+libtype_id+'&districtsearch_id='+district_id+'&streetsearch_id='+street_id+'&price='+price
    console.log(url)
    return url
}
