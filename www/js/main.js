function confirm_remove(){
    location.reload(true);
    var user_answear = confirm("Are you sure?")
    if (user_answear == true){
        alert("User removed")
    }
    else{
        alert("Nothing happen")
    }
}