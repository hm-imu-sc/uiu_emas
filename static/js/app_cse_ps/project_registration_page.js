$("#course_name").click(function()
{
    let option = $("#course_name option");
    if(option.length>1)
    {
      return;
    }
    $.ajax({
      url: "/cse_ps/get_course_names/",
      method: "GET",
      success: function(data)
      {
        data = JSON.parse(data);

        let html_for_option = "<option value=''>Select Course</option> ";
        data = data['data'];

        for(let i=0;i<data.length;i++)
        {
          html_for_option+=("<option value = '" + data[i]['course_code'] + "'>" + data[i]['course_code'].replace('_', ' ') + " : " + data[i]['course_name'] + "</option> ");
        }
        $("#course_name").html(html_for_option);
      }
    });
});


$("#course_name").change(function(){
  let course_code = $("#course_name").val();
  $.ajax({
    url : ("/cse_ps/get_sections/"+course_code),
    method: "GET",
    success: function(data)
    {
      data = JSON.parse(data);

      let html_for_option = "<option value=''>Select Section</option> ";
      data = data['data'];

      for(let i=0;i<data.length;i++)
      {
        html_for_option+=("<option value = '" + data[i]['id'] + "'>" + data[i]['name'] + "</option> ");
      }
      $("#section").html(html_for_option);
    }
  });
});

$("#check_student").click(function(){
  let student_id = $("#student_id").val();
  $.ajax({
    // url : ("/cse_ps/get_sections/"+course_code),
    // method: "GET",
    // success: function(data)
    // {
    //   data = JSON.parse(data);
    //
    //   let html_for_option = "<option value=''>Select Section</option> ";
    //   data = data['data'];
    //
    //   for(let i=0;i<data.length;i++)
    //   {
    //     html_for_option+=("<option value = '" + data[i]['id'] + "'>" + data[i]['name'] + "</option> ");
    //   }
    //   $("#section").html(html_for_option);
    //}
  });
});
