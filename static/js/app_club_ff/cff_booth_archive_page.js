$("#club_name_filter").click(function()
{
	let option = $("#club_name_filter option");

	if(option.length>1)
	{
		return;
	}
	$.ajax({
		url: "/club_ff/get_club_names/",
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);

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
		return;
	}
	$.ajax({
		url: "/club_ff/get_cff_years/",
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);

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

$("#filter").click(function(){
  let club_name = $("#club_name_filter").val();

  if(club_name.length==0)
  {
    club_name = 'NULL';
  }
  let year = $("#year_filter").val();

  if(year.length==0)
  {
    year = 'NULL';
  }

  $.ajax({
		url : ("/club_ff/get_filtered_cff/"+club_name+"/"+year),
		method: "GET",
		success: function(data)
		{
			data = JSON.parse(data);

			console.log(data);

            data = data['data'];


            booth_thumbnails = ""

            for(let i=0;i<data.length;i++)
              {
                booth_thumbnails+= `
                <div class="booth_thumbnail">
                    <div class="club_name">` + data[i]['club_name']  +  `</div>
                    <div class="booth_details">
                        <div class="description">
                            <h2>Description:</h2>
                            <span>` + data[i]['club_description'] + `Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium quas, reiciendis facilis possimus ratione, animi inventore vero numquam dolorum perferendis at quod magnam saepe? Numquam.</span>
                             <br>
                             <a class="visit_link" href="{{booths.id}}">Visit Booth</a>
                        </div>
                    </div>
                        `;
                booth_thumbnails+= `</div>
                </div>
                </div>

                </div> `;

              }
            $("#booth_thumbnails").html(booth_thumbnails);
        }
        });
});


