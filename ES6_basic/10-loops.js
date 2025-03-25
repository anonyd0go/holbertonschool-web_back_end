export default function appendToEachArrayValue(array, appendString) {
    for (const ele of array) {
      array[array.indexOf(ele)] = appendString + ele;
    }
  
    return array;
  }
