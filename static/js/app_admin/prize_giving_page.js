
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
	let project = $("#projects").val();

	let prize = -1;

	let prize_lebels = $(".prizes .prize label i");

	for (let i=0; i<prize_lebels.length; i++) {
		if ($(prize_lebels[i]).hasClass("active")) {
			let prizetag = $(prize_lebels[i]).attr("class").split(" ")[2];
			if (prizetag === "prize-gold") {
				prize = 1;
			}
			else if (prizetag === "prize-silver") {
				prize = 2;
			}
			else if (prizetag === "prize-bronze") {
				prize = 3;
			}
			break;
		}
	}

	if(prize == -1 || trimester == 0 || project == -1 || course_code == -1)
	{
		if(prize == -1)
		{
			let code="<p>Please select a valid prize</p>";
			$("#error").html(code)
		}
		if(project == -1)
		{
			let code="<p>Please select a valid team name</p>";
			$("#error").html(code)
		}
		if(course_code == -1)
		{
			let code="<p>Please select a valid course</p>";
			$("#error").html(code)
		}
		if(trimester == 0)
		{
			let code="<p>Please select a valid trimester</p>";
			$("#error").html(code)
		}

	}
	else
	{
		let csrf = $("input[name=\"csrfmiddlewaretoken\"]").val();
		$.ajax({
			url: ("/give_award/"),
			type: 'POST',
			data: { trimester : trimester, course_code: course_code, project: project, prize: prize ,csrfmiddlewaretoken: csrf,},  // data to submit
			success: function () {
				let code="<p>Prize successfully added</p>";
				$("#error").html(code)
			}
		});
	}


})