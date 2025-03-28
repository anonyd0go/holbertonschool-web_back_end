export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(string) {
    if (typeof string !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = string;
  }

  get length() {
    return this._length;
  }

  set length(number) {
    if (typeof number !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = number;
  }

  get students() {
    return this._students;
  }

  set students(stdnts) {
    if (typeof stdnts !== 'object') {
      throw TypeError('Students must be an array of strings');
    }
    for (const student of stdnts) {
      if (typeof student !== 'string') {
        throw TypeError('Students must be an array of strings');
      }
    }

    this._students = stdnts;
  }
}
