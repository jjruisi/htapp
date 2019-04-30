$( document ).ready(function() {
        $("#btn").click(function() {
		
		var $kw = $("#keywords").val();
		var $lang = $("#language").val();
		var $loc = $("#location").val();

		$.ajax({
			url: '/ajax/test_ajax/',
			type: 'POST',
			data: {
				'keywords' : $kw,
				'location' : $loc,
				'lang' : $lang
			},
			dataType: 'json',
			success: function(values) {
				$("#data").html("");
				$("#data").html("<table id='table' class='display' style='width=100%'></table>");
				var obj = JSON.parse(values);
				$("#table").DataTable ( {
					data: obj.data,
					columns: [
						{ "width": "50%", "title" : "url" },
						{ "width": "50%", "title" : "review" }
					]
		                });

			}
		});
        });
});

