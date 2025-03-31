export default function getListStudentIds(list) {
  if (!(list instanceof Array)) {
    return [];
  }

  return list.map((x) => x.id);
}
