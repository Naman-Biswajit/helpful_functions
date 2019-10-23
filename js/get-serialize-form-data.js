function getDataObject(itemsKey, serializedValues = []) {
  return serializedValues
    .reduce((prev, {name, value}) => {    
      if (!name.match('[0-9]$')) {
        return {
          ...prev,
          [name]: value
        }
      }

      const prevItems = prev[itemsKey] || [];
      const index = parseInt(name.replace(/[^0-9]/g, ''));
      const newName = name.replace(/[0-9]/g, '');
      const prevObj = prevItems[index] || {};
      
      prevItems[index] = {
        ...prevObj,
        [newName]: value
      };

      return {
        ...prev,
        [itemsKey]: prevItems
      };
    }, {});
}
