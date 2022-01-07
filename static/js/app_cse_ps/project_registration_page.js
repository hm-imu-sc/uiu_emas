$("#course_name").click(function()
{
    $.ajax({
      url: "/cse_ps/get_course_names/",
      method: "GET",
      success: function(data)
      {
        
      }

    });
});
