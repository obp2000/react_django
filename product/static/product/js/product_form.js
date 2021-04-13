var $ = jQuery

const tags = {
	price: {
		rub_m: 'input#id_price_rub_m',
		with_coeffs: 'div#prices_with_coeffs'
	},
	dollar_price: "input#id_dollar_price",
	dollar_rate: "input#id_dollar_rate",
	density: "input#id_density",
	width: "input#id_width",
	weight_for_count: "input#id_weight_for_count",
	length_for_count: "input#id_length_for_count",
	density_for_count: "input#id_density_for_count",
	weight: "input#id_weight",
	meters_in_roll: "input#id_meters_in_roll"
}

const PriceCoeffs = [
	1,
	1.5,
	1.6,
	1.7,
	1.8,
	1.9,
	2,
	1.2,
	1.3,
	1.4
]

var price_rub_m = ({
	dollar_price = 0,
	dollar_rate = 0,
	density = 0,
	width = 0
}) => dollar_price * dollar_rate * density * width / 100000

var price_with_coeff = (price = 0, coeff) => (price * coeff).toFixed(0)

var density_for_count = ({
		weight_for_count = 0,
		length_for_count = 0,
		width = 0
	}) =>
	(weight_for_count > 0 && length_for_count > 0 && width > 0) ?
	(weight_for_count / length_for_count / width).toFixed(0) * 100 : 0

var prices_with_coeffs = (price, coeffs) =>
	coeffs.reduce((result, coeff) =>
		result + coeff + ":" + price_with_coeff(price, coeff) + "&nbsp;&nbsp;", '')

var meters_in_roll = ({
		weight = 0,
		density = 0,
		width = 0
	}) =>
	(weight > 0 && density > 0 && width > 0) ? (weight * 100000 / density / width).toFixed(2) : 0

var set_meters_in_roll = ({
		weight = $(tags.weight).val(),
		density = $(tags.density).val(),
		width = $(tags.width).val()
	}) =>
	$(tags.meters_in_roll).val(meters_in_roll({
		weight,
		density,
		width
	}))

var set_price_rub_m = ({
		dollar_price = $(tags.dollar_price).val(),
		dollar_rate = $(tags.dollar_rate).val(),
		density = $(tags.density).val(),
		width = $(tags.width).val()
	}) =>
	$(tags.price.rub_m).val(parseInt(price_rub_m({
		dollar_price,
		dollar_rate,
		density,
		width
	})))

const set_density_for_count = ({
		weight_for_count = $(tags.weight_for_count).val(),
		length_for_count = $(tags.length_for_count).val(),
		width = $(tags.width).val()
	}) =>
	$(tags.density_for_count).val(density_for_count({
		weight_for_count,
		length_for_count,
		width
	}))

const on_price_rub_m_change = function() {
	$(tags.price.with_coeffs).html(prices_with_coeffs(this.value, PriceCoeffs))
}

const on_dollar_price_change = function() {
	set_price_rub_m({
		dollar_price: this.value
	}).change()
}

const on_dollar_rate_change = function() {
	set_price_rub_m({
		dollar_rate: this.value
	}).change()
}

const on_density_change = function() {
	set_price_rub_m({
		density: this.value
	}).change()
	set_meters_in_roll({
		density: this.value
	})
}

const on_width_change = function() {
	set_price_rub_m({
		width: this.value
	}).change()
	set_density_for_count({
		width: this.value
	})
	set_meters_in_roll({
		width: this.value
	})
}

const on_weight_for_count_change = function() {
	set_density_for_count({
		weight_for_count: this.value
	})
}

const on_length_for_count_change = function() {
	set_density_for_count({
		length_for_count: this.value
	})
}

const on_weight_change = function() {
	set_meters_in_roll({
		weight: this.value
	})
}

$(function() {

	$(tags.price.rub_m).on('change', on_price_rub_m_change).change()

	$(tags.dollar_price).on('change', on_dollar_price_change)

	$(tags.dollar_rate).on('change', on_dollar_rate_change)

	$(tags.density).on('change', on_density_change)

	$(tags.width).on('change', on_width_change)

	$(tags.weight_for_count).on('change', on_weight_for_count_change)

	$(tags.length_for_count).on('change', on_length_for_count_change)

	$(tags.weight).on('change', on_weight_change)

})