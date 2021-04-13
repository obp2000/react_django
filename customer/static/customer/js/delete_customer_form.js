 var $ = jQuery

 const delete_customer_buttons = "button.delete-customer"

 var attach_modal_delete_form = function() {
 	$(this).modalForm({
 		formURL: $(this).data("form-url"),
 		isDeleteForm: true
 	})
 }

 $(function() {

 	$(delete_customer_buttons).each(attach_modal_delete_form)

 })