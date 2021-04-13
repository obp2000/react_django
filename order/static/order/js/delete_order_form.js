 var $ = jQuery

 const delete_order_buttons = "button.delete-order"

 var attach_modal_delete_form = function() {
 	$(this).modalForm({
 		formURL: $(this).data("form-url"),
 		isDeleteForm: true
 	})
 }

 $(function() {

 	$(delete_order_buttons).each(attach_modal_delete_form)

 })