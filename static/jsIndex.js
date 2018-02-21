$(document).ready(function(){
  $.getJSON('/api/post.json', 
    function(data) {
    var num = Math.floor(Math.random() * 3) + 1;
  var image = num+".jpg";
     $(".news").html("<h3 class='newsInBrief'> NEWS IN BRIEF </h3><h1 class='headline'>"+data.titles[0]+"</h1>"+"<img class='image' src='"+image+"'>");
     
     $(".youMayAlsoLikeList").html("<li><h2>"+data.titles[1]+"</h2></li><li><h2>"+data.titles[2]+"</h2></li><li><h2>"+data.titles[3]+"</h2></li><h2><li>"+data.titles[4]+"</h2></li>"); 
        
    });
  
  
});
