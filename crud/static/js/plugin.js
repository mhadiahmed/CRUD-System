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
		});
	});

	$('#modal-book').on('submit','.create-form' , function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#book-table tbody').html(data.book_list);
					$('#modal-book').modal('hide');
				} else {
					$('#modal-book .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	})
});