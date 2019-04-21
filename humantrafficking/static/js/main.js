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
				var obj = JSON.parse(values);
				$("#table").DataTable ( {
					data: obj.data,
					columns: [
						{ title : "url" },
						{ title : "review" }
					]
		                });

			}
		});
        });
});

