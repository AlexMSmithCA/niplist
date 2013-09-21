window.onload = function(){
  $('#login').bind('click', function(e){
    e.preventDefault();
    $('#login-container').removeClass('hidden');
    $('#overlay').addClass('show');
  })
}
