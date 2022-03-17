 var $ = jQuery

 const delete_buttons = "button.delete-object"

 var attach_modal_delete_form = function() {
 	$(this).modalForm({
 		formURL: $(this).data("form-url"),
 		isDeleteForm: true
 	})
 }

 $(function() {
 	$(delete_buttons).each(attach_modal_delete_form)
 })