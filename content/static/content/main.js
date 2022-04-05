AOS.init();
discount()
discount_info()
size_slider()


$( window ).resize(function() {
    size_slider()

});

function size_slider() {
    if ($('body').width() <= 700){
        $('.slider').css({'width':($('.main_shop').width()-50), 'margin':'25px'})

    }else if($('body').width() <= 1240){
        $('.slider').css({'width':($('.main_shop').width() - ($('.list-all-category').width()+80))-180, 'margin':'50px'})
    }else{
        $('.slider').css({'width':(1240 - ($('.list-all-category').width()+80))-150, 'margin':'50px'})
    }
}

function discount() {
    $('.product').each(function(){
        let discount_percent =$( this ).find('.discount .percent').html()
        let price = $( this ).find('.tile_price span').html()
        $( this ).find('.discount .old_price').html(Math.ceil(price / (100 - discount_percent) * 100))
    })
}

function discount_info() {
    $('.product_info').each(function(){
        let discount_percent = discount_detail
        let price = $( this ).find('.price .nmb').html()
        $( this ).find('.discount .old_price').html(Math.ceil(price / (100 - discount_percent) * 100))
    })
}


$('.menu_icon').click(function(){
    $('.neonText').animate({left: "0px"}, 500)
    $('.menu_icon').css({display: "None"}, 500)
})

$('.close').click(function(){
    $('.neonText').animate({left: "-100%"}, 500)
    $('.menu_icon').css({display: "block"}, 500)
})


$('.part_2').click(function(){
    $('.neonText').animate({left: "-100%"}, 500)
    $('.menu_icon').css({display: "block"}, 500)
})

$('.row_open_all_meta img').click(function(){
    let btn = $('.row_open_all_meta img').attr("src")
    if (btn == '/static/shop/img/down.png'){
        $('.meta').animate({'height': "100%", 'max-height':"1000px"}, 2000)
        $('.row_open_all_meta').animate({'bottom':'0px'}, 2000)
        $('.row_open_all_meta img').attr("src", '/static/shop/img/up.png')
    }else{
        $('.meta').animate({'height': "40%", 'max-height':"100px"}, 2000)
        $('.row_open_all_meta').animate({'bottom':'30px'}, 2000)
        $('.row_open_all_meta img').attr("src", '/static/shop/img/down.png')
    }
})


$('.miniatures img').click(function(){
    $('.product_gallery .main_img img').attr("src",$(this).attr("src"))
})

$('.product').click(function(){
    document.location.href = $(this).find('a').attr('href')
})

$('.neonBorder .catalog_title').click(function(){

    parameters = {duration: 1000}
    if ($(this).filter('.off').length >0){
        $('.neonBorder .item').slideDown(parameters)
        $(this).removeClass('off')
        $(this).find('img').attr("src","/static/shop/img/up.png")
    }else{
        $('.neonBorder .item').slideUp(parameters)
        $(this).addClass('off')
        $(this).find('img').attr("src","/static/shop/img/down.png")
    }

})

$('.detail_price div').click(function(){
    let zxc = $(this).attr('class')
    $('.detail_price div').each(function(){
        $(this).removeClass('active_row')
    })
    $('.product_info .price .nmb').html(all_price[zxc] )
    $(this).addClass('active_row')
    discount_info()

})

$('.price_b .buy_btn').click(function(){
    picked_product = $('.detail_price').find('.active_row').attr('class')
    if (picked_product.indexOf('default') > -1) {
        kof = 1
    }else if(picked_product.indexOf('remote') > -1){
        kof = 2
    }else if(picked_product.indexOf('plate') > -1){
        kof = 0
    }
    code = all_price['vendor_code'] + kof
    add_in_basket(code)

})

function add_in_basket(code) {
    let data = {}
    let csrf_token = $('.basket [name="csrfmiddlewaretoken"]').val()
    data['product'] = code
    data['val'] = '1'
    data["csrfmiddlewaretoken"] = csrf_token
    $.ajax({
        url: '/cart/add',
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            cart(data.sum)
        },
        error: function(){
            console.log("error")
        }
     })

}

function cart(amount) {
    $('.nav_body .cart .count').html(amount)

}

function down_basket(code, parent) {
    let data = {}
    let csrf_token = $('.basket [name="csrfmiddlewaretoken"]').val()
    data['product'] = code
    data['val'] = '1'
    data["csrfmiddlewaretoken"] = csrf_token
    $.ajax({
        url: '/cart/down',
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            console.log(data)
            if (data['amount'] > 0){
                parent.closest('.f_count').find('.count').html(data['amount'])
            }else{
                 parent.closest('.cart_product').remove()
            }
            $('#cart_sum').html(data['purchase_amount']+' ₴')
            cart(data['sum'])
        },
        error: function(){
            console.log("error")
        }
     })


}

$('.cart').click(function(){
    open_cart()
    $('.user_cart').removeClass('hide')
})

$('.form').click(function(){
    $('.user_cart').removeClass('hide')
})

function add_basket(code, parent) {
    let data = {}
    let csrf_token = $('.basket [name="csrfmiddlewaretoken"]').val()
    data['product'] = code
    data['val'] = '1'
    data["csrfmiddlewaretoken"] = csrf_token
    $.ajax({
        url: '/cart/add',
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            console.log(data)
            parent.closest('.f_count').find('.count').html(data['amount'])
            $('#cart_sum').html(data['purchase_amount']+' ₴')
            cart(data['sum'])

        },
        error: function(){
            console.log("error")
        }
     })


}

function open_cart() {
    let data = {}
    let csrf_token = $('.basket [name="csrfmiddlewaretoken"]').val()
    data["csrfmiddlewaretoken"] = csrf_token
    $.ajax({
        url: '/cart/my-cart',
        type: 'POST',
        data: data,
        cache: true,
        success: function (data, sum) {
            for(i in data){
                if(i == 'purchase_amount'){
                    console.log('purchase_amount',data[i])
                    $('#cart_sum').html(data[i]+' ₴')
                }else{
                    $('.all_products').append(`
                    <div class="cart_product">
                        <div class="cart_img">
                            <img src="${data[i]['img']}" alt="">
                        </div>
                        <div class="cart_info">
                            <p><a href="/shop/${data[i]['url']}" > ${data[i]['title']}(${data[i]['type']}) </a></p>
                            <div class="price">
                                <div class="f_count" data-vendor_code = "${data[i]['vendor_code']}"
                                    data-type_kof = "${data[i]['type_kof']}">
                                    <img class = "minus" src="/static/shop/img/minus.png" alt="-">
                                    <p class="cart_count">${data[i]['amount']}</p>
                                    <img class="plus" src="/static/shop/img/plus.png" alt="+">
                                </div>
                                <div class="value_price">
                                    <p>${data[i]['price']} ₴</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `)
                }
            }
        },
        error: function(){
            console.log("error")
        }
     })

}

$(document).on('click', '.minus', function(){
    my_class = $(this).parent()
    vendor_code = my_class.data("vendor_code")
    type_kof = my_class.data("type_kof")
    console.log(type_kof)
    down_basket(`${vendor_code}${type_kof}`, $(this))

})

$(document).on('click', '.plus', function(){
    my_class = $(this).parent()
    vendor_code = my_class.data("vendor_code")
    type_kof = my_class.data("type_kof")
    console.log(type_kof)
    add_basket(`${vendor_code}${type_kof}`, $(this))

})

$('.cart_exit').click(function(){
    close_cart()
    console.log('123')
})

function close_cart(){
    $('.user_cart').addClass('hide')
    $('.all_products').html(' ')

}


function api_novaposhta(modelName, method, town) {
    data = {}
    data = `{
        "apiKey": "a4db860d3a92d17805659f3198a753c5",
        "modelName": "${modelName}",
        "calledMethod": "${method}",
        "methodProperties" : {
            "CityName":"${town}",
            "Limit": 50
            }
        }`
//    console.log(data)
    return $.ajax({
        url: `https://api.novaposhta.ua/v2.0/json/`,
        type: 'POST',
        data: data,
        cache: true,

        success: function (data) {
            console.log(data)
        },
        error: function(){
            console.log("error")
        }
    })

}




$('#town').keyup(function(){
    town = `${$(this).val()}`
    method = "searchSettlements"
    modelName = "Address"
    data = api_novaposhta(modelName, method, town)
    .then(
          function(data) {
            if (data["data"]["0"]['TotalCount'] >= 1 ){
                $('#town').parent().find(".dropdown_points").remove()
                $('#town').parent().append(`<div class = "dropdown_points"></div>`)
                $.each(data["data"]["0"]['Addresses'], function(index, value){
                    console.log(index, value["MainDescription"])
                    $('.dropdown_points').append(
                        `<div class = "dropdown_element">${value["MainDescription"]}</div>`
                    )
                })

            }
          })
})

$(document).on('click', '.dropdown_element', function(){
    value = $(this).html()
    $('#town').val(value)
    $(".dropdown_points").remove()


})




$('#department').keyup(function(){
    if($('#town').val()){
        town = `${$('#town').val()}`
        method = "getWarehouses"
        modelName = "AddressGeneral"
        data = api_novaposhta(modelName, method, town).then(
          function(data) {
            if (data["data"].length >= 1 ){
                $('#department').parent().find(".dropdown_points_dep").remove()
                $('#department').parent().append(`<div class = "dropdown_points_dep"></div>`)
                $.each(data["data"], function(index, value){
                    console.log(index, value["MainDescription"])
                    console.log('FUCK')
                    $('.dropdown_points_dep').append(
                        `<div class = "dropdown_element_dep">${value["Description"]}</div>`
                    )
                })

            }
          })
    }
})


$(document).on('click', '.dropdown_element_dep', function(){
    value = $(this).html()
    console.log(value)
    $('#department').val(value)
    $(".dropdown_points_dep").remove()


})


$("form").submit(function(event ){
    event .preventDefault()
    var $form = $( this )
    data = {}
    data["csrfmiddlewaretoken"] = $('.basket [name="csrfmiddlewaretoken"]').val()
    console.log($form.find('input'))
    $form.find('input').each(function( index ) {
        data[$(this).attr('name')] = $(this).val()
    })
    var data = $.post( $form["0"]["action"], data )
    console.log(data)

    data.done(function() {
        console.log(data['responseJSON'])
  })



//    $.post(
//        console.log('form.attr("action")')
//        $.form.attr("action"), // ссылка куда отправляем данные
//        $.form.serialize()     // данные формы
//    ).done(
//        alert(data)
//    )

})



$('.single-item').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});

