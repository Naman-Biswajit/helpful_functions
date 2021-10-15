/**
 * Just a simple promise based sleep function
 *
 * usage:
 * sleep(100)
 *
 * @param ms
 * @returns {Promise<any>}
 */
export function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}