let comment_viewer = $(".comment-viewer");
$(comment_viewer).scrollTop($(comment_viewer)[0].scrollHeight);

function send_comment() {

    let user_id = "011181062";
    let user_type = "student";

    let project_id = $(".comment-viewer").attr("project_id");
    let comment = $("#new-comment").val();
    $("#new-comment").val("");

    let csrf_token = $("input[name=\"csrfmiddlewaretoken\"]").val();

    $.ajax({
        url: "/cse_ps/commenter/",
        method: "POST",
        data: {
            user_id: user_id,
            user_type: user_type,
            project_id: project_id,
            comment: comment, 
            csrfmiddlewaretoken: csrf_token
        },
        success: function(data) {
            return;
        }
    });
}

$("#new-comment").keyup(function(e) {
    if (e.key == "Enter") {
        send_comment();
    }
});

$("#comment-send-btn").click(send_comment);

comment_synchroniser = setInterval(function(){
    let current_length = Number($("#comment-length").attr("length"));
    let project_id = $(comment_viewer).attr("project_id");
    
    $.ajax({
        url: "/cse_ps/comment_loader/" + project_id + "/" + current_length + "/",
        type: "GET",
        success: function(data) {

            if (data.length == 2) {
                return;
            }

            $("#comment-length").remove();
            $(comment_viewer).append(data);

            $(comment_viewer).scrollTop($(comment_viewer)[0].scrollHeight);
        }
    });

}, 1000); 

// clearInterval(comment_synchroniser);