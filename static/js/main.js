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
    $.ajax({
        type: 'POST',
        url: '/edit',
        data : {'idx': tr_id},
        contentType : 'application/json;charset=UTF-8',
        dataType : 'json',
        success: function(response) {
                console.log(response);
            },
        error: function(error) {
                console.log(error);
            }

    })
    
})