$("#course_filter").click(function()
{
	let option = $("#course_filter option");
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

			let html_for_option = "<option value=''>Course</option> ";
			data = data['data'];

			for(let i=0;i<data.length;i++)
			{
				html_for_option+=("<option value = '" + data[i]['course_code'] + "'>" + data[i]['course_code'].replace('_', ' ') + " : " + data[i]['course_name'] + "</option> ");
			}
			$("#course_filter").html(html_for_option);
		}
	});
});

$("#trimester_filter").click(function()
{
	let option = $("#trimester_filter option");
	if(option.length>1)
	{
		return;
	}
	$.ajax({
		url: "/cse_ps/get_trimesters/",
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);

			let html_for_option = "<option value=''>Trimester</option> ";
			data = data['data'];

			for(let i=0;i<data.length;i++)
			{
        let trimester_string = data[i]['trimester'];
        let season = "";
        if(trimester_string.charAt(2)==1)
        {
          season = "Spring";
        }
        else if(trimester_string.charAt(2)==2)
        {
          season = "Summer";
        }
        else
        {
          season = "Fall";
        }

        trimester_string = trimester_string.slice(0, -1);

				html_for_option+=("<option value = '" + data[i]['trimester'] + "'>" + season + ' \'' + trimester_string + "</option> ");
			}
			$("#trimester_filter").html(html_for_option);
		}
	});
});

$("#filter").click(function(){
	let course_code = $("#course_filter").val();
  if(course_code.length==0)
  {
    course_code = 'NULL';
  }
	let trimester = $("#trimester_filter").val();
  if(trimester.length==0)
  {
    trimester = 'NULL';
  }

  $.ajax({
		url : ("/cse_ps/get_filtered_archeive_projects/"+course_code+"/"+trimester),
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);
			console.log(data);

      data = data['data'];

      let booth_thumbnails = "";

      for(let i=0;i<data.length;i++)
      {
        booth_thumbnails+= `
        <div class="booth_thumbnail" course_name = "` + data[i]['course_name'] + `" trimester = "`+ data[i]['trimester'] + `" >
            <div class="project_name">
              <span>Project Name:</span><span>` + data[i]['title'] + `</span>
            </div>
            <div class="project_details">
                <div class="description">
                    <span>Description:</span><span>` + data[i]['short_description'] + `Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium quas, reiciendis facilis possimus ratione, animi inventore vero numquam dolorum perferendis at quod magnam saepe? Numquam.</span>
                </div>

                <div class="project_members">
                    <h2>Project Members:</h2>
                    <div class="members">`;


        for(let j=0;j<data[i]['project_members'].length;j++)
        {
          booth_thumbnails+=`
          <div>
              <span class="id">` + data[i]['project_members'][j]['id'] +` | </span>
              <span class="id">` +  data[i]['project_members'][j]['name'] + `</span>
          </div>
          `;
        }

        booth_thumbnails+= `</div>
                </div>
            </div>
        </div>
        `;
      }
      $("#booth_thumbnails").html(booth_thumbnails);

		}
	});

});
