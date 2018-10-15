/*
 * Converts a query String to an object
 * Example:
 * Before: item.test[2]=3&item.title=Some Test Name
 * After: {
 *   item: {
 *     test: [3],
 *     title: "Some Test Name"
 *   }
 * }
 */
function buildObject(obj, keyStr, value) {
		if (!keyStr) {
    	return value;
    }
    
    const keySplit = keyStr.split('.');
    
    if (keySplit.length === 1) {
    	if (keyStr.match(/\[\d+\]$/)) {
      	const newKey = keyStr.replace(/\[.*/, '');
      	return Object.assign({}, obj, {
        	[newKey]: [].concat(obj[newKey] || [], value)
        });
      }
    	
    	return Object.assign({}, obj, {
      	[keyStr]: value
      })
    }
    
    const firstKey = keySplit[0];
    
    return Object.assign({}, obj, {
    	[firstKey]: buildObject(obj[firstKey] || {}, keySplit.splice(1).join('.'), value)
    });
}


export default function processQueryString(qstr) {
        return qstr.split('&').reduce((prev, pair) => {
        const [key, value] = pair.split('=');

    if (!key) {
        return prev;
    }

        return Object.assign({}, prev, buildObject(prev, key.trim(), value.trim()));
  }, {});
}

