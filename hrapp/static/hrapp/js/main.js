$(document).ready(function() {
	View.init();
})
View = {
	init : function() {
		$('#tweet-btn').click(function() {
			var tweet = $("#tweet-area").val().trim()
			if (tweet.length == 0) {
				return;
			}
			$('#tweet-btn').addClass('disabled').empty().append("Recommending...");
			console.log("ff");
		});
	}

}