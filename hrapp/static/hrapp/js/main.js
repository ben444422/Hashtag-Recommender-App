
View = {
    info : null,
    init : function(info) {
        $(document).ready(function() {
            View.info = info;
            View.init_view();
        });
    },
    init_view: function() {

    	$('#recommendation-box').hide();
		$('#tweet-btn').click(function() {
			var tweet = $("#tweet-area").val().trim()
			if (tweet.length == 0) {
				return;
			}
			$('#tweet-btn').addClass('disabled').empty().append("Recommending...");


			$.ajax({
                 type: "GET",
                 url: "/hr/recommend/",
                 data: {
                       'tweet': encodeURI(tweet), 
                       // pass this token in order to get through the permissions
                       'csrfmiddlewaretoken': View.info.csrf_token
                 },
                 success: function(data){
                    console.log(data)
                    $('#tweet-btn').removeClass('disabled').empty().append("Recommend Me");
                    $('#recommendation').empty().append(tweet + "<span id='hashtag' class='orangey'> #" + data['hashtags'][0] + " #" + data['hashtags'][1] + " #" + data['hashtags'][2] + "</span>");
                 	$('#tweet-box').slideUp();
                 	$('#recommendation-box').slideDown();

                 	var cur_hashtag = 0
                 	$('#new-hashtag-btn').click(function() {
                 		if (cur_hashtag+2 == data['hashtags'].length- 1) {
                 			return;
                 		}
                 		cur_hashtag = cur_hashtag + 1;
                 		$('#hashtag').empty().append(" #" + data['hashtags'][cur_hashtag] + " #" + data['hashtags'][cur_hashtag+1] + " #" + data['hashtags'][cur_hashtag+2]);
                 		
                 		
                 	});

                 }
            });
		});

		$('#back-btn').click(function() {
			$('#tweet-box').slideDown();
            $('#recommendation-box').slideUp();
		});
	}
}

