$("#trimester").change(function(){
	let trimester = $("#trimester").val();
	if(trimester != 0)
	{
		$.ajax({
		url : ("/get_courses_by_trimester/"+trimester+"/"),
		method: "GET",
		success: function(data)
		{

			data = JSON.parse(data);

			let option = "<option value='-1'>Select</option> ";
			data = data['data'];

			for(let i=0;i<data.length;i++)
			{
				option+=("<option value = '" + data[i]['section_id'] + "'>" + data[i]['course_code'] + ' : ' + data[i]['course_name'] + "</option> ");
			}
			$("#courses").html(option);
		}
		});
	}

});

