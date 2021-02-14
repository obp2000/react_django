 var $ = jQuery
 $(function() {

 	var $rows = $("select[id^=id_order_items-]").filter("[id$=product]").closest('tr')

 	$rows.each(
 		function() {
 			var product = $(this).find("select[id$=product]")
 			var amount = $(this).find("input[id$=amount]")
 			var price = $(this).find("input[id$=price]")
 			var sum = $(this).find("input[id$=sum]")
 			var weight = $(this).find("input[id$=weight]")
 			var density = $(this).find("input[id$=density]")
 			var width = $(this).find("input[id$=width]")

 			var change_sum = () => {
 				sum.val((amount.val() * price.val()).toFixed(2))
 			}

 			// var calc_weight = () => {
 			// 	if (amount.val() > 0) {
 			// 		var product_data_tag = product_on_deck.find("[data-price]")
 			// 		if (product_data_tag.data('density') > 0 &&
 			// 			product_data_tag.data('width') > 0) {
 			// 			var sum_weight = amount.val() * product_data_tag.data('density') *
 			// 				product_data_tag.data('width') / 100
 			// 			weight.val(sum_weight.toFixed(0))

 			// 		} else {
 			// 			weight.val(0)
 			// 		}
 			// 	} else {
 			// 		weight.val(0)
 			// 	}
 			// }

 			// var change_weight22222 = (density, width) => {
 			// 	var sum_weight = (amount.val() > 0 && density > 0 && width > 0) ?
 			// 		(amount.val() * density * width / 100).toFixed(0) : 0
 			// 	weight.val(sum_weight)
 			// }

 			var change_weight = () => {
 				var sum_weight = (amount.val() > 0 && density.val() > 0 && width.val() > 0) ?
 					(amount.val() * density.val() * width.val() / 100).toFixed(0) : 0
 				weight.val(sum_weight)
 			}

 			function change_product(e) {
 				// alert(density.val())
 				var data = e.params.data
 				price.val(data['price']).change()
 				width.val(data['width'])
 				density.val(data['density']).change()
 				// change_sum()
 				// change_weight()
 			}

 			product.on('select2:select', change_product)

 			amount.change(function() {
 				change_sum()
 				change_weight()
 				change_order_sum()
 				change_order_weight()
 			})

 			price.change(function() {
 				change_sum()
 				change_order_sum()
 			})

 			density.change(function() {
 				change_weight()
 				change_order_weight()
 			})
 		}
 	)

 	var change_order_sum = () => {
 		var sum = 0
 		$("input[id^=id_order_items]").filter("[id$=sum]").each(function() {
 			sum += Number($(this).val())
 		})
 		$("input#id_sum").val(sum.toFixed(2))
 	}

 	 var change_order_weight = () => {
 		var weight = 0
 		$("input[id^=id_order_items]").filter("[id$=weight]").each(function() {
 			weight += Number($(this).val())
 		})
 		$("input#id_weight").val(weight)
 	}

 })