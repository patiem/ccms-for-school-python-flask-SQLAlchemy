function gradeValue(value) {
    if (value > -1){
        return value + '%'
    }
    else{
        return 'None'
    }
}

function confirm_remove(){
    location.reload(true);
    var user_answear = confirm("Are you sure?");
    if (user_answear == true){
        alert("User removed")
    }
    else{
        alert("Nothing happen")
    }
}

$('a.edit').click(function () {
    var tr_id = $(this).closest('tr').find('#id').data('id');
    var dict_id = { Idx: tr_id}
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