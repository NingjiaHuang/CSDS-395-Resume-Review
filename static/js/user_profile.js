$( document ).ready(function() {
    init_page();
});

$(document).on('click','#edit',function(){
    $('.info').hide();
    $('.edit').show();
});

$(document).on('click','#cancel',function(){
    $('.info').show();
    $('.edit').hide();
});

$(document).on('click','#update',function(){
    console.log('click');
    if (checkValidity()) {
        $( "#submit" ).click();
    }
    else {
        $('.err-msg').show();
    }
});

$(document).on('click','#confirm_unlock',function(){
    $('#id_unlock').val('true');
    $( "#submit" ).click();
});

function init_page() {
    $("li#user_profile" ).addClass("active");
    $('.info').show();
    $('.edit').hide();
    $('.err-msg').hide();
    $('input#id_first_name').val($('#info_first_name').text().replace(/\s/g,''));
    $('input#id_last_name').val($('#info_last_name').text().replace(/\s/g,''));
    $('input#id_phone_number').val($('#info_phone_number').text().replace(/\s/g,''));
    $('#id_major').val($('#info_major').text().trim());
    $('#id_academic_standing').val($('#info_academic_standing').text().replace(/\s/g,''));
    $('#id_self_intro').val($('#info_self_intro').text().trim());
    var price = $('#info_price').text().trim();
    $('#id_price').val(parseInt(price));

}


function checkValidity() {
    if (!($("input#id_first_name").val() && $("input#id_last_name").val() && $("input#id_phone_number").val())) {
        return false;
    }

    var phone = $('input#id_phone_number').val(),
    intRegex = /[0-9 -()+]+$/;
    if((phone.length < 6) || (!intRegex.test(phone)))
    {
         return false;
    }

    return true;
}