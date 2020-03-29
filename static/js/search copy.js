const user_input = $("#user-input")
const search_icon = $('#search-icon')
const artists_div = $('#replaceable-content')

const delay_by_in_ms = 700
let scheduled_function = false


function ajax_call2(input_target) {
	$.ajax({
        url: 'http://localhost:8000/customers/search/',
        data: {
			'q': input_target
        },
        dataType: 'json',
        success: function (data) {
			artists_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				artists_div.html(data['html_from_view'])
				// fade-in the div with new contents
				artists_div.fadeTo('slow', 1)
				// stop animating search icon
				search_icon.removeClass('blink')
			})
        }
      });
}

function test(params) {
	console.log(params);
	
}
user_input.on('keyup', function (e) {
	e.preventDefault()
	var input_target = $(this).val()	
	// start animating the search icon with the CSS class
	search_icon.addClass('blink')
	// // setTimeout returns the ID of the function to be executed

	setTimeout(ajax_call2, delay_by_in_ms, input_target);

	
})
