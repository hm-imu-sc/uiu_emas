
let temp = {
	student_ids: {}
}

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

// $("#check_student").click(function(){
// 	let student_id_input = $("#student_id");
// 	let student_id = $(student_id_input).val();
// 	$.ajax({
// 		url : ("/cse_ps/get_student/"+student_id),
// 		method: "GET",
// 		success: function(data)
// 		{
// 			data = JSON.parse(data);
// 			console.log(data);
// 			if(data['message'] != "OK")
// 			{
// 				$(student_id_input).removeClass("valid_project_member");
// 				$(student_id_input).addClass("invalid_project_member");

// 				$("#student_info").html("No Student Found with student ID " + student_id)
// 			}
// 			else
// 			{
// 				$(student_id_input).removeClass("invalid_project_member");
// 				$(student_id_input).addClass("valid_project_member");

// 				let student_information = "";
// 				data = data['data'];

// 				for(let i=0;i<data.length;i++)
// 				{
// 					student_information+=(data[i]['name'] + " (" + student_id + "), " + data[i]['department']);
// 				}
// 				$("#student_info").html(student_information);
// 			}
// 		}
// 	});
// });

$("#add_member").click(function(){
	let student_id = $("#student_id").val();
	
	if (temp[student_id]) {
		return;
	}

	let project_members = $("#project_members").val();
	if (project_members.length==0) {
		$("#project_members").html(student_id);
	}
	else {
		$("#project_members").append("," + student_id);
	}

	temp[student_id] = true;

	return;
});

$("#student_id").keyup(function(){
    let student_id_input = $("#add_member");
    let student_id = $(this).val();

    if (student_id === "") {
        return;
    }

    $.ajax({
        url : ("/cse_ps/get_student/"+student_id),
        method: "GET",
        success: function(data) {
            data = JSON.parse(data);
            if (data['message'] != "OK") {
                $(student_id_input).attr("disabled", "true");
                $(student_id_input).removeClass("add_anabled");
                $(student_id_input).addClass("add_disabled");
				$("#student_info").html("No Student Found with student ID " + student_id);
            }
            else {
                $(student_id_input).removeAttr("disabled");
                $(student_id_input).removeClass("add_disabled");
                $(student_id_input).addClass("add_anabled");
				
				let student_information = "";
				data = data['data'];

				student_information+=(data[0]['name'] + " (" + student_id + "), Department of " + data[0]['department']);

				$("#student_info").html(student_information);
            }
        }
    });
});