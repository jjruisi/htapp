$( document ).ready(function() {
        $("#btn").click(function() {
		
		var $kw = $("#keywords").val();
		var $lang = $("#language").val();
		var $loc = $("#location").val();
		alert($kw + ' ' + $lang + ' ' + $loc);

        	var $str = 'hello world';

		$.ajax({
			url: '/ajax/test_ajax/',
			type: 'POST',
			data: {
				'data' : $str
			},
			dataType: 'json',
			success: function(data) {
				alert(data.data);
			}
		});

        });
});

