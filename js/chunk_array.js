/*
 * Convert single layer array into nested array based on `chunck_size`
 *
 * Example:
 * Before: [1, 2, 3, 4, 5]
 * After chunk_size=3: [[1,2,3],[4,5]]
 */
function chunkArray(myArray, chunk_size) {
  const arrayLength = myArray.length;
  const tempArray = [];

  for (let index = 0; index < arrayLength; index += chunk_size) {
    tempArray.push(myArray.slice(index, index + chunk_size));
  }

  return tempArray;
}
