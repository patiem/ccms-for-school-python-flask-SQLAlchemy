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
    var tr_id = $(this).closest('tr').find('#id').data('id');
    var dict_id = { Idx: tr_id}
    var user_answear = confirm("Are you sure?");
    if (user_answear == true){
        $.ajax({
            type: 'POST',
            url: 'http://localhost:5000/remove-user',
            data : JSON.stringify(dict_id),
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            // contentType : 'application/x-www-form-urlencoded',

    })
        alert("User removed")
    }
    else{
        alert("Nothing happen")
    }
})

$('#add_email').change(function () {
    var email = $(this).val();
    var email_dict = { Mail: email};
    $.ajax({
        type: 'POST',
        url: 'http://localhost:5000/check-mail',
        data : JSON.stringify(email_dict),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function(response) {
                console.log(response['value']);
                if(response['value'] == false){
                    $('#add_submit').removeClass('inactive').addClass('orange');
                    $('#add_submit').prop("disabled", false)

                }
                else {
                    $('#add_submit').addClass('inactive').removeClass('orange');
                    $('#add_submit').prop("disabled", true)
                }

            },
        error: function(error) {
                console.log(error);
            }
    })
})


$('a.edit').click(function () {
    var tr_id = $(this).closest('tr').find('#id').data('id');
    var dict_id = { Idx: tr_id};
    $.ajax({
        type: 'POST',
        url: 'http://localhost:5000/edit',
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
    
})