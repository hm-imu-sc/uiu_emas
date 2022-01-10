$.ajax({
    url: "/general/test/10/",
    method: "GET",
    success: function(data) {
        $("#loading-area").html(data);
    }
});