$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (i, item) {
      $('<li/>').text(item.title).appendTo('#list_movies');
    });
  });
});
