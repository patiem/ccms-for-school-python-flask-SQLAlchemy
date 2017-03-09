$('.grade_input').change(function () {
    var value =  $(this).val();
    if (value > -1){
        $(this).parent('.grade_range').find('.grade_output').val(value)
    }
    else {
        $(this).parent('.grade_range').find('.grade_output').val('None')
    }
    $(this).addClass('Changed');
    var link = $(this).closest('tr').find('.left').data('link');
    var dict_data = { Value: value, Link:link};
    $.ajax({
        type: 'POST',
        url: '/update_submission',
        data : JSON.stringify(dict_data),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',

        success: function(response) {
            var mentor_name = response['fullname'];
            $('.Changed').closest('tr').find('.mentor_name').html(mentor_name);
            $('.Changed').removeClass('Changed');

            // $('.grade_input').closest('tr').find('.left').val(mentor)
        },
        error: function(error) {
            console.log(error);
            alert('nope');
        }

    });
});




$('.remove_user').click(function () {
    location.reload(true);
    var tr_id = $(this).closest('tr').find('.id').data('id');
    var dict_id = { Idx: tr_id};
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
});

$('a.edit_team').click(function () {
    var team_id = $(this).parent('.table_parent').find('.team_id').data('id');
    var team_name = $(this).parent('.table_parent').find('.team_name').data('name');

    $('#edit_name').val(team_name);
    $('#team_edit_id').val(team_id);

});

$('.edit_team_submit').click(function () {
   $('.close').trigger('click');
});

$(function () {
    var team_id;

    $('.add_to_team').click(function () {
        team_id = $(this).parent('.table_parent').find('.team_id').data('id');
    });

    $('.to_team').click(function () {
        var url = $(this).attr('href');
        url = url + team_id;
        $(this).attr('href', url);
    });
});