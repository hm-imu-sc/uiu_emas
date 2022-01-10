$.ajax({
    url: "/club_ff/UIUCCL/desc/5/",
    method: "GET",
    success: function(data) {
        $("body").append(data);
    }
});