function cleanObject(obj) {
  function isEmpty(value){
    return (
    	value == null
    	|| value.length === 0
      || value === ''
      || Object.keys(value).length === 0
    );
  }


  return Object
    .entries(obj)
    .reduce((prev, [key, value]) => {
      let cleanValue = value;

      if (Object.prototype.toString.call(value) === '[object Object]') {
        cleanValue = cleanObject(value);
      }

      return isEmpty(cleanValue) ? prev : {
        ...prev,
        [key]: cleanValue
      };
    }, {})
}
