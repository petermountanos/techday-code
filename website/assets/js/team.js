jQuery(document).ready(function() {
  //toggle the componenet with class msg_body
  jQuery(".heading").click(function()
  {
    jQuery(this).next(".content").slideToggle(500);
  });
});