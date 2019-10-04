$(document).ready(function(){
  $('.user-intro h4').removeClass('hidden');
  $("#js-rotating").Morphext({
    animation: "rubberBand",
    separator: ",",
    speed: 3000
  });
});
