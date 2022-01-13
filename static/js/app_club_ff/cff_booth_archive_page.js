$("#club_name_filter").click(function()
{
	let option = $("#club_name_filter option");

//	console.log("---------")

	if(option.length>1)
	{
//	    console.log(option.length)
		return;
	}
	$.ajax({
		url: "/club_ff/get_club_names/",
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);
//			console.log(data)

			let html_for_option = "<option value=''>Club name</option> ";
			data = data['data'];

			for(let i=0;i<data.length;i++)
			{
				html_for_option+=("<option value = '"+ data[i]['club_name'] + "'>" + data[i]['club_name']  + "</option> ");
			}
			$("#club_name_filter").html(html_for_option);
		}
	});
});


$("#year_filter").click(function()
{
	let option = $("#year_filter option");

	if(option.length>1)
	{
	    console.log("----------------")
		return;
	}
	$.ajax({
		url: "/club_ff/get_cff_years/",
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);
			console.log(data)

			let html_for_option = "<option value=''>Year</option> ";
			data = data['data'];

			for(let i=0;i<data.length;i++)
			{
				html_for_option+=("<option value = '"+ data[i]['year'] + "'>" + data[i]['year']  + "</option> ");
			}
			$("#year_filter").html(html_for_option);
		}
	});
});