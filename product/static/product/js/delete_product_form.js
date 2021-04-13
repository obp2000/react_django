 var $ = jQuery

 const delete_product_buttons = "button.delete-product"

 var attach_modal_delete_form = function() {
 	$(this).modalForm({
 		formURL: $(this).data("form-url"),
 		isDeleteForm: true
 	})
 }

 $(function() {

 	$(delete_product_buttons).each(attach_modal_delete_form)

 })