function filter(club_id_selector, criteria_selector, offset=0, success) {
    let club_id = $(club_id_selector).val();
    let criteria = $(criteria_selector).val();
    console.log("/club_ff/post_processor/" + club_id + "/" + criteria + "/" + offset + "/")
    $.ajax({
        url: "/club_ff/post_processor/" + club_id + "/" + criteria + "/" + offset + "/",
        method: "GET",
        success: success
    }); 
}

$("#club_name").change(function() {filter(this, "#sort_by", 0, function(data) {
    $(".feed").html(data)
})});

$("#sort_by").change(function() {filter("#club_name", this, 0, function(data) {
    $(".feed").html(data)
})});