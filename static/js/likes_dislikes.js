$(document).ready(function(){

$(".btn").each( function() {
var id = $(this).val();
$(this).click(function(){
var    csrf = $("input[name=csrfmiddlewaretoken").val();
var
formData = {
      pk: id,
      csrfmiddlewaretoken: csrf
    };

$.ajax({
url:'/like/' + id + '/',
type: 'post',
data: formData,
success: function(response){
document.getElementById("quantity" + id).innerHTML = response.quantity_likes;
document.getElementById("button" + id).innerHTML = response.likes_dislikes;
}
});
});
});
});