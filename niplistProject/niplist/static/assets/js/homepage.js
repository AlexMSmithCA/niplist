window.onload = function(){
  $('#login').bind('click', function(e){
    e.preventDefault();
    $('#login-container').removeClass('hidden');
    $('#overlay').addClass('show');
    $('.form-signin input[type=text], .form-signin input[type=password]').addClass('form-control'); //bootstrap styling
    $('.form-signin input[type=text]').attr('placeholder', 'E-mail');
    $('.form-signin input[type=password]').attr('placeholder', 'Password');
  })
}
