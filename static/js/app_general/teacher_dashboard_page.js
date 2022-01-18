
function fetch_projects(target, project_status){
    $(".tab-buttons button").removeClass("active");
    $(target).addClass("active");
    $.ajax({
        url: "/general/project_processor_teacher/" + project_status + "/",
        method: "GET", 
        success: function(data) {
            let icon = "<i class=\"fad fa-clipboard\"></i>";
            if (data.length == 3) {
                data = "<div class=\"no-projects\"><span>No projects to show !!!</span></div>"
            }

            $(".projects").html(data);
        }
    });
}

$("#appr_proj").click(function(){fetch_projects(this, 1)});
$("#appr_pen_proj").click(function(){fetch_projects(this, 0)});