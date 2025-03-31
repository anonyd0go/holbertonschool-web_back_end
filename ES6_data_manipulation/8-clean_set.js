export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  return Array.from(set).filter(
    (str) => str.startsWith(startString),
  ).map(
    (str) => str.slice(startString.length),
  ).join('-');
}
