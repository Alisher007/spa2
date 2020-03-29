const customer_edit = $("#customer_edit")
const search_icon = $('#search-icon')
const artists_div = $('#replaceable-content')

function customer_ajax() {
	$.ajax({
		url: 'http://localhost:8000/customers/edit/' + customer_id.value + '/',
		method: "POST",
        data: {
			'email': customer_input.value
        },
		dataType: 'json',
        success: function (data) {
			console.log(data);
        },
        fail: function (data) {
			console.log(data);
			
        }
      });
}
customer_edit.on('click', function (e) {
	e.preventDefault()
	console.log(customer_id.value , ' after change');
	console.log(customer_input.value , ' after change');
	
	// var input_target = $(this).val();
	customer_ajax()

	
})
