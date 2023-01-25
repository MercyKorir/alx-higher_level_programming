$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: $('#language_code').val() })
      .done(function (data) {
        $('#hello').text(data.hello);
      });
  });
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  });
});
