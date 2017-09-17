$(document).ready(function(){
	$('.show-form').click(function(){
		$.ajax({
			url: '/books/create',
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-book').modal('show');
			},
			success: function(data){
				$('#modal-book .modal-content').html(data.html_form);
			}
		})
	})
})