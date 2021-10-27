function capitalizeFirstLetters(val) {
	// result like: `Monday`, `MemberType`
	val = val
		.trim()
		.toLowerCase()
		.split(' ')

	return val.map(v => v.charAt(0).toUpperCase() + v.slice(1)).join('')
}

// Input Masking - Credit Card
// HTML Input Element like:
//   <input type="text" size="20" autocomplete="off" class="form-control" id="number" required />

function spaceBetween(word, letterCount, delimiter) {
	return word
		.replaceAll(delimiter, '') // remove old spaces
		.match(new RegExp(`.{1,${letterCount}}`, 'g')) // split by letterCount
		.join(delimiter); // join back to a new string by the `delimiter`
}

$('#number').on('keyup', function (e) {
	var val = $(this).val();

	// format in same input field
	$(this).val(spaceBetween(val, 4, ' '));
});