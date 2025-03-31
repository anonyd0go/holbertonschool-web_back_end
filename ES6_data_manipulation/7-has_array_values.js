export default function hasValuesFromArray(set, array) {
  return array.every((ele) => set.has(ele));
}
