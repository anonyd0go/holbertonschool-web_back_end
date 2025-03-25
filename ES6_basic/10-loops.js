export default function appendToEachArrayValue(array, appendString) {
  const modArray = array;
  for (const ele of array) {
    modArray[array.indexOf(ele)] = appendString + ele;
  }

  return modArray;
}
