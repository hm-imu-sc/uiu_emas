$("#club").click(function()
{
    let option = $("#club option");
    if(option.length>1)
    {
      return;
    }
    $.ajax({
      url: "/club_ff/get_club_names/",
      method: "GET",
      success: function(data)
      {
        data = JSON.parse(data);

        let html_for_option = "<option value=''>Select Your Club</option>";
        data = data['data'];

        for(let i=0;i<data.length;i++)
        {
          html_for_option+=("<option value = '" + data[i]['club_id'] + "'>" + data[i]['club_name'] + "</option> ");
        }
        $("#club").html(html_for_option);
      }
    });
});
