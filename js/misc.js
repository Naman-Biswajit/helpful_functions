function capitalizeFirstLetters(val) {
	// result like: `Monday`, `MemberType`
	val = val
		.trim()
		.toLowerCase()
		.split(' ')

	return val.map(v => v.charAt(0).toUpperCase() + v.slice(1)).join('')
}