const sampleObj = {
  'level1.1': {
    'level1.2': {
    	'randomKey': 'Other Value',
      'level1.3': {
        'level1.4': {
          'someKey': 'Other Value'
        }
      }
    }
  },
  'level2.1': {
    'level2.2': {
      'OtherKey': 'Other Value'
    }
  },
  'NotNested': 'Other Value'
}


function findValue(obj, cb, path = '') {
  if (typeof obj !== 'object') {
    if (typeof cb === 'function' && cb(obj)) {
      return {
        path,
        value: obj
      };
    }

    return null;
  }
  
  return Object.entries(obj).reduce((prev, [key, value]) => {
  	return [].concat(prev, findValue(value, cb, `${path}/${key}`));
  }, []);
}


const result = findValue(sampleObj, (value) => {
  return value === 'Other Value';
});


console.log('result =', result); // prints:
/*
[
  {path: "/level1.1/level1.2/randomKey", value: "Other Value"},
  {path: "/level1.1/level1.2/level1.3/level1.4/someKey", value: "Other Value"},
  {path: "/level2.1/level2.2/OtherKey", value: "Other Value"},
  {path: "/NotNested", value: "Other Value"}
]
*/
