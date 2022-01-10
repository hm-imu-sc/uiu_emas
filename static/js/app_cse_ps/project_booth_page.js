comment_synchroniser = setInterval(function(){
    let current_length = Number($(".chat_box").attr("length"));
    // console.log(current_length);

    $.ajax({
        url: "chat_processor.php",
        type: "POST",
        data: {job: "load", length: current_length},
        datatype: "json",
        success: function(data) {

            data = JSON.parse(data);

            if (data["new_chats_len"] == 0) {
                return;
            }

            let chat_box_content = $(".chat_box").html();
            $(".chat_box").html(data["new_chats"] + chat_box_content);
            $(".chat_box").attr("length", current_length + data["new_chats_len"]);
        }
    });

}, 1000); 