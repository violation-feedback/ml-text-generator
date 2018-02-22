$(document).ready(function(){
  $.getJSON("./api/post.json", function(data) {
    var num = Math.floor(Math.random() * 4) + 1;
    var image = "./images/photo" + num + ".jpg";
    $(".article h1").text(data.titles[0]);
    $(".article img").attr("src", image);
    $("title").text(data.titles[0]);
    for (var i = 1; i < data.titles.length; i++) {
      var li = $("<li>");
      var link = $("<a>").attr("href", "./").text(data.titles[i]);
      li.append(link);
      $(".youMayAlsoLikeList").append(li);
    }
  });
});