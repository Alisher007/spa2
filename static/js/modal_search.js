function res_delete(params) {
    $.ajax({
        headers: { "X-CSRFToken": res_update_token },
		url: res_delete_url,
        method: "POST",
        data: {
            'date': id_arrdate_update.val(),
        },
        dataType: 'json',
        success: function (data) {
            if (data.data == 'ok') {
                location.href = res_update_arrdate_url;
            }
        },
        fail: function (data) {
			console.log(data);
			
        }
      });
}


// CUSTOMER MODAL

const c_search_input = $("#c_search_input");
const c_search_btn = $("#c_search_btn");
const c_search_place = $("#c_search_place");

c_search_btn.on('click', function (e) {
    e.preventDefault();
        
    
    
	$.ajax({
		url: res_search_url,
		method: "GET",
        data: {
			'q': c_search_input.val()
        },
        dataType: 'json',
        success: function (data) {
            c_search_place.html(data['html_customers-search']);
        },
        fail: function (data) {
			console.log(data);
			
        }
      });
})


var c_modal_id = document.getElementById("c_modal_id");

// Get the button that opens the modal
const id_customerid = $("#id_customerid");

// Get the <span> element that closes the modal
var c_close = document.getElementsByClassName("c_close")[0];

// When the user clicks the button, open the modal 
function cs_select_id(e) {
    e.preventDefault()
    c_modal_id.style.display = "block";
}
function res_create_submit(e) {
    if ($('#id_starttime').val() >= $('#id_endtime').val()) {
        e.preventDefault()
        alert('the end time should be higher than the start time')
    }   
    
}


// When the user clicks on <span> (x), close the modal

if (c_close !== undefined) {
    c_close.onclick = function() {
        c_modal_id.style.display = "none";
    }
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == c_modal_id) {
    c_modal_id.style.display = "none";
  }
}




// PRODUCT MODAL
const p_search_input = $("#p_search_input");
const p_search_btn = $("#p_search_btn");
const p_search_place = $("#p_search_place");
const p_search_place2 = $("#p_search_place2");
const p_search_confirm = $("#p_search_confirm");

p_search_btn.on('click', function (e) {
    e.preventDefault();
	$.ajax({
		url: res_product_search_url,
		method: "GET",
        data: {
			'q': p_search_input.val()
        },
        dataType: 'json',
        success: function (data) {
            p_search_place.html(data['html_products-search']);
        },
        fail: function (data) {
			console.log(data);
			
        }
      });
})

var p_modal_id = document.getElementById("p_modal_id");

// Get the button that opens the modal
const id_products = $("#id_products");

// Get the <span> element that closes the modal
var p_close = document.getElementsByClassName("p_close")[0];

// When the user clicks the button, open the modal 

function cs_products_id(e) {
    e.preventDefault()
    p_modal_id.style.display = "block";
}



// When the user clicks on <span> (x), close the modal
if (p_close !== undefined) {
    p_close.onclick = function() {
        p_modal_id.style.display = "none";
    }
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == p_modal_id) {
    p_modal_id.style.display = "none";
  }
}