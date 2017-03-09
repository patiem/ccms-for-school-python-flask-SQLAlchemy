function gradeValue(value) {
    if (value > -1){
        return value + '%'
    }
    else{
        return 'None'
    }
}
$('.remove_user').click(function () {
    location.reload(true);
    var tr_id = $(this).closest('tr').find('.id').data('id');
    var dict_id = { Idx: tr_id}
    var user_answear = confirm("Are you sure?");
    if (user_answear == true){
        $.ajax({
            type: 'POST',
            url: '/remove-user',
            data : JSON.stringify(dict_id),
            dataType: 'json',
            contentType: 'application/json; charset=utf-8'
    });
        alert("User removed")
    }
    else{
        alert("Nothing happen")
    }
});

$('a.edit').click(function () {
    var tr_id = $(this).closest('tr').find('#id').data('id');
    var dict_id = { Idx: tr_id};
    $.ajax({
        type: 'POST',
        url: '/edit',
        data : JSON.stringify(dict_id),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        // contentType : 'application/x-www-form-urlencoded',

        success: function(response) {
            console.log(response['id']);
            $('#edit_id').val(response['id'])
            $('#name').val(response['name'])
            $('#surname').val(response['surname'])
            $('#email').val(response['e-mail'])
            $('#telephone').val(response['telephone'])
        },
        error: function(error) {
            console.log(error);
            alert('nope');
        }

    })

});


$('#add_email').change(function () {
    var email = $(this).val();
    var atpos = email.indexOf("@");
    if (atpos>1 && (email.endsWith(".com") || email.endsWith(".pl"))) {
        var email_dict = {Mail: email};
        $.ajax({
            type: 'POST',
            url: '/check-mail',
            data: JSON.stringify(email_dict),
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: function (response) {
                console.log(response['value']);
                if (response['value'] == false) {
                    $('#add_submit').removeClass('inactive').addClass('orange').prop("disabled", false);
                    $('#add_email').removeClass('error');
                    $('#mail_message').html("");

                }
                else {
                    $('#add_submit').addClass('inactive').removeClass('orange').prop("disabled", true);
                    $('#add_email').addClass('error');
                    $('#mail_message').html("E-mail already exist")
                }

            },
            error: function (error) {
                console.log(error);
            }
        })
    }
    else{
        $('#add_submit').addClass('inactive').removeClass('orange').prop("disabled", true);
        $('#add_email').addClass('error');
        $('#mail_message').html("Wrong e-mail format: need to have @ and end with .pl or .com");
    }
});


$('#email').change(function () {
    var email = $(this).val();
    var atpos = email.indexOf("@");
    if (atpos>1 && (email.endsWith(".com") || email.endsWith(".pl"))) {
        var email_dict = {Mail: email};
        $.ajax({
            type: 'POST',
            url: '/check-mail',
            data: JSON.stringify(email_dict),
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: function (response) {
                console.log(response['value']);
                if (response['value'] == false) {
                    $('#submit').removeClass('inactive').addClass('orange').prop("disabled", false);
                    $('#email').removeClass('error');
                    $('#mail_message_add').html("")

                }
                else {
                    $('#submit').addClass('inactive').removeClass('orange').prop("disabled", true);
                    $('#email').addClass('error');
                    $('#mail_message_add').html("E-mail already exist")
                }

            },
            error: function (error) {
                console.log(error);
            }
        })
    }
    else{
        $('#submit').addClass('inactive').removeClass('orange').prop("disabled", true);
        $('#email').addClass('error');
        $('#mail_message_add').html("Wrong e-mail format: need to have @ and end with .pl or .com");
    }
});



$('a.edit').click(function () {
    var tr_id = $(this).closest('tr').find('.id').data('id');
    var dict_id = { Idx: tr_id};
    $.ajax({
        type: 'POST',
        url: '/edit',
        data : JSON.stringify(dict_id),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        // contentType : 'application/x-www-form-urlencoded',

        success: function(response) {
                console.log(response['id']);
                $('#edit_id').val(response['id'])
                $('#name').val(response['name'])
                $('#surname').val(response['surname'])
                $('#email').val(response['e-mail'])
                $('#telephone').val(response['telephone'])
            },
        error: function(error) {
                console.log(error);
                alert('nope');
            }

    })
    
});

$('.close').click(function () {
    $('#submit').removeClass('inactive').addClass('orange').prop("disabled", false);
    $('#email').removeClass('error');
    $('#mail_message_add').html("");
    $('#add_submit').removeClass('orange').addClass('inactive').prop("disabled", true);
    $('#add_email').removeClass('error');
    $('#mail_message').html("");
    $('#add_name').val('');
    $('#add_surname').val('');
    $('#add_email').val('');
    $('#add_telephone').val('');

});

$('#attendance_date').change(function () {
    var date = $('#attendance_date').val();
    var pathname = window.location.pathname; // Returns path only
    if(date){
        window.location.replace(pathname + '/' + date);
    }
    else{
        window.location.replace(pathname);
    }
});

$('.attendance_tr').change(function () {
    $(this).css('background-color','#70FF9E');
    // alert('JUPI!!')
});

$('a.edit_team').click(function () {
    var tr_id = $(this).closest('tr').find('#id').data('id');
    var dict_id = { Idx: tr_id};
    $.ajax({
        type: 'POST',
        url: '/edit',
        data : JSON.stringify(dict_id),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        // contentType : 'application/x-www-form-urlencoded',

        success: function(response) {
            console.log(response['id']);
            $('#edit_id').val(response['id'])
            $('#name').val(response['name'])
            $('#surname').val(response['surname'])
            $('#email').val(response['e-mail'])
            $('#telephone').val(response['telephone'])
        },
        error: function(error) {
            console.log(error);
            alert('nope');
        }

    })

});