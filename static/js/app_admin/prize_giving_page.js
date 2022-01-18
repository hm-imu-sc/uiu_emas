
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
				option+=("<option value = '" + data[i]['course_code'] + "'>" + data[i]['course_code'] + ' : ' + data[i]['course_name'] + "</option> ");
			}
			$("#courses").html(option);
		}
		});
	}

});

$("#courses").change(function() {
	let course_code = $("#courses").val();
	if (course_code != -1) {
		$.ajax({
			url: ("/get_projects_by_course_code/" + course_code + "/"),
			method: "GET",
			success: function (data) {

				data = JSON.parse(data);

				let option = "<option value='-1'>Select</option> ";
				data = data['data'];

				for (let i = 0; i < data.length; i++) {
					option += ("<option value = '" + data[i]['project_id'] + "'>" + data[i]['title'] + "</option> ");
				}
				$("#projects").html(option);
			}
		});
	}
});

$("form .prizes .prize label i").click(function(){
    $("form .prizes .prize label i").removeClass("active");
    $(this).addClass("active");
});

$("#submit").click(function (){
	let trimester = $("#trimester").val();
	let course_code = $("#courses").val();
	let prize = -1;
	if($('#f_prize').hasClass())
		prize = 1

})