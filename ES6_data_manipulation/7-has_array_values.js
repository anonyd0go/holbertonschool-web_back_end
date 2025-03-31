export default function hasValuesFromArray(set, array) {
  return set.isSupersetOf(new Set(array));
}
