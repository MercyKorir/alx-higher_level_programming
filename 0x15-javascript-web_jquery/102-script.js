$('#btn_translate').click(function () {
  const languageCode = $('#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
    $('#hello').text(data.hello);
  });
});
