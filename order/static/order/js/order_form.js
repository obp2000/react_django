var $ = jQuery

const tags = {
	customer: {
		customer: 'select#id_customer',
		pindex: "input#id_pindex",
		city: "div#city",
		address: 'div#customer_address'
	},
	order_items: {
		table_tbody: "table#order_items_table tbody",
		product_str: "product",
		amount_str: "amount",
		price_str: "price",
		one_m_weight_str: "one_m_weight",
		sum_str: "sum",
		weight_str: "-weight"
	},
	order: {
		sum: "input#id_sum",
		weight: "input#id_weight"
	},
	gift: {
		row: "tr#gift",
		weight: "input#id_gift_weight"
	},
	samples: {
		weight: "input#id_samples_weight"
	},
	post: {
		cost: 'input#id_post_cost',
		count_cost: 'button#count_post_cost_button',
		discount: 'span#post_discount',
		cost_with_packet: 'span#post_cost_with_packet',
		total_cost: 'input#id_total_postals'
	},
	packet: {
		packet: 'select#id_packet',
		weight: "input#id_packet_weight"
	},
	total: {
		sum: "input#id_total_sum",
		weight: "input#id_total_weight"
	}
}

const need_gift = (sum) => sum >= 2000

const post_cost_with_packet = ({
	post_cost = 0,
	packet = 0
}) => parseInt(post_cost) + parseInt(packet)

const post_discount = ({
		post_cost,
		packet,
		sum = 0
	}) => (sum < 1000) ? 0 :
	(post_cost_with_packet({
		post_cost,
		packet
	}) * 0.3).toFixed(2)

const total_postals = (params) => post_cost_with_packet(params) - post_discount(params)

const total_sum = ({
	post_cost,
	packet,
	sum
}) => (Number(sum) + total_postals({
	post_cost,
	packet,
	sum
})).toFixed(2)

const order_item_sum = (amount = 0, price = 0) => (amount * price).toFixed(2)

const all_order_items_selects = (tag_str) => tags.order_items.table_tbody + " select[id$=" + tag_str + "]"

const all_order_items_inputs = (tag_str) => tags.order_items.table_tbody + " input[id$=" + tag_str + "]"

const current_gift_weight = (sum, gift_weight) => (need_gift(sum)) ? parseInt(gift_weight) : 0

const total_weight = (weight, gift_weight, samples_weight, packet_weight, sum) => parseInt(weight) +
	parseInt(samples_weight) +
	parseInt(packet_weight) +
	current_gift_weight(sum, gift_weight)

const order_item_weight = (amount, one_m_weight) =>
	(amount > 0 && one_m_weight > 0) ? Math.floor(amount * one_m_weight) : 0

$.fn.check_gift = function() {
	(need_gift($(tags.order.sum).val())) ? $(this).show(): $(this).hide()
}

var set_post_discount = (params) => $(tags.post.discount).text(post_discount(params))

var set_total_postals = (params) => $(tags.post.total_cost).val(total_postals(params))

var set_order_sum = (params) => $(tags.total.sum).val(total_sum(params))

var set_sum_totals = ({
	post_cost = $(tags.post.cost).val(),
	packet = $(tags.packet.packet).val(),
	sum = $(tags.order.sum).val()
}) => {
	var params = {
		post_cost,
		packet,
		sum
	}
	set_post_discount(params)
	set_total_postals(params)
	set_order_sum(params)
}

$.fn.find_order_item_input = function(input_str) {
	return $(this).find("input[id$=" + input_str + "]")
}

$.fn.find_order_item_select = function(select_str) {
	return $(this).find("select[id$=" + select_str + "]")
}

$.fn.product = function(select_str) {
	return $(this).find_order_item_select(tags.order_items.product_str)
}

$.fn.amount = function() {
	return $(this).find_order_item_input(tags.order_items.amount_str)
}

$.fn.price = function() {
	return $(this).find_order_item_input(tags.order_items.price_str)
}

$.fn.sum = function() {
	return $(this).find_order_item_input(tags.order_items.sum_str)
}

$.fn.one_m_weight = function() {
	return $(this).find_order_item_input(tags.order_items.one_m_weight_str)
}

$.fn.weight = function() {
	return $(this).find_order_item_input(tags.order_items.weight_str)
}

$.fn.sum_values = function() {
	return $(this).toArray().reduce((sum, element) => sum + Number(element.value), 0)
}

const all_order_items_products = () => all_order_items_selects(tags.order_items.product_str)

const all_order_items_amounts = () => all_order_items_inputs(tags.order_items.amount_str)

const all_order_items_prices = () => all_order_items_inputs(tags.order_items.price_str)

const all_order_items_one_m_weights = () => all_order_items_inputs(tags.order_items.one_m_weight_str)

const all_order_items_sums = () => all_order_items_inputs(tags.order_items.sum_str)

const all_order_items_weights = () => all_order_items_inputs(tags.order_items.weight_str)

var set_order_item_sum = ({
		order_item_row,
		amount = order_item_row.amount().val(),
		price = order_item_row.price().val()
	}) =>
	order_item_row.sum().val(order_item_sum(amount, price))

var set_order_items_sum = () =>
	$(tags.order.sum).val($(all_order_items_sums()).sum_values().toFixed(2))

var set_sums = (params) => {
	set_order_item_sum(params)
	set_order_items_sum()
	set_sum_totals({})
	$(tags.gift.row).check_gift()
}

var set_order_weight = () => $(tags.total.weight).val(total_weight(
	$(tags.order.weight).val(),
	$(tags.gift.weight).val(),
	$(tags.samples.weight).val(),
	$(tags.packet.weight).val(),
	$(tags.order.sum).val()))

var set_order_item_weight = ({
		order_item_row,
		amount = order_item_row.amount().val(),
		one_m_weight = order_item_row.one_m_weight().val()
	}) =>
	order_item_row.weight().val(order_item_weight(amount, one_m_weight))

var set_order_items_weight = () =>
	$(tags.order.weight).val($(all_order_items_weights()).sum_values())

var set_weights = (params) => {
	set_order_item_weight(params)
	set_order_items_weight()
	set_order_weight()
}

var set_sums_and_weights = (params) => {
	set_sums(params)
	set_weights(params)
}

var set_post_cost_with_packet = ({
		post_cost = $(tags.post.cost).val(),
		packet = $(tags.packet.packet).val()
	}) =>
	$(tags.post.cost_with_packet).text(post_cost_with_packet({
		post_cost,
		packet
	}))

$.fn.current_order_item_row = function() {
	return $(this).closest('tr')
}

var postcalc_url = "http://api2.postcalc.ru"

var postcalc_params = () => ({
	f: '153038',
	o: 'json',
	st: 'localhost',
	ml: 'obp2000@mail.ru',
	key: 'test',
	t: $(tags.customer.pindex).val(),
	w: $(tags.order.weight).val(),
	v: 0,
	p: 'pv'
})

const on_customer_change = ({
	params: {
		data: {
			pindex,
			city,
			address
		}
	}
}) => {
	$(tags.customer.pindex).val(pindex)
	$(tags.customer.city).text(city)
	$(tags.customer.address).text(address)
}

const on_order_item_price_change = function() {
	set_sums({
		order_item_row: $(this).current_order_item_row(),
		price: this.value
	})
}

const on_order_item_one_m_weight_change = function() {
	set_weights({
		order_item_row: $(this).current_order_item_row(),
		one_m_weight: this.value
	})
}

const on_order_item_amount_change = function() {
	set_sums_and_weights({
		order_item_row: $(this).current_order_item_row(),
		amount: this.value
	})
}

const on_order_item_product_change = function({
	params: {
		data: {
			price,
			one_m_weight
		}
	}
}) {
	var $order_item_row = $(this).current_order_item_row()
	$order_item_row.price().val(price).change()
	$order_item_row.one_m_weight().val(one_m_weight).change()
}

const on_packet_change = function() {
	set_post_cost_with_packet({
		packet: this.value
	})
	set_sum_totals({
		packet: this.value
	})
}

const on_post_cost_change = function() {
	set_post_cost_with_packet({
		post_cost: this.value
	})
	set_sum_totals({
		post_cost: this.value
	})
}

var set_post_cost1 = function(jqXHR, textStatus, errorThrown) {
	alert(textStatus)
}

var set_post_cost2 = function(xhr, status) {
	// if (!xhr.responseText) {

	// }
	// else {
	var data = xhr.responseText;
	console.log("response: ", xhr)
	// }
}

var set_post_cost3 = function(data) {
	// data1 = JSON.parse(data);
	alert('sssssss')
}

var set_post_cost = ({
	Отправления: {
		ЦеннаяПосылка: {
			Тариф
		}
	}
}) => $(tags.post.cost).val(Тариф).change()


const count_post_cost = function() {
	$.ajax({
		url: postcalc_url,
		// jsonp: "callback",
		dataType: "jsonp",
		data: postcalc_params(),
		success: set_post_cost,
		// error: set_post_cost2,
		// complete: set_post_cost2
	})
}

const on_order_item_add = function(order_item_row, formCount) {
	order_item_row.product().djangoSelect2()
}

const on_order_item_remove = function(order_item_row) {
	order_item_row.amount().val(0).change()
}

const order_items_formset_settings = {
	prefix: 'order_items',
	addCssClass: 'btn btn-info btn-sm',
	deleteCssClass: 'btn btn-info btn-sm',
	addButtonHolder: 'td#add_order_item_button_holder',
	callbacks: {
		onAdd: on_order_item_add,
		onRemove: on_order_item_remove
	},
	uiText: {
		addPrompt: 'Добавить',
		removePrompt: '&times;',
	}
}

$(document).on('select2:select', all_order_items_products(), on_order_item_product_change)

$(document).on('change', all_order_items_amounts(), on_order_item_amount_change)

$(document).on('change', all_order_items_prices(), on_order_item_price_change)

$(document).on('change', all_order_items_one_m_weights(), on_order_item_one_m_weight_change)

$(function() {

	$(tags.customer.customer).on('select2:select', on_customer_change)

	$(tags.order_items.table_tbody).formset(order_items_formset_settings)

	$(tags.packet.packet).on('change', on_packet_change)

	$(tags.post.cost).on('change', on_post_cost_change)

	$(tags.post.count_cost).on('click', count_post_cost)

})
