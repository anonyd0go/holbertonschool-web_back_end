export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  get size() {
    return this._size;
  }

  set size(val) {
    if (typeof val !== 'number') {
      throw TypeError('Size must be a number');
    }
    this._size = val;
  }

  get location() {
    return this._location;
  }

  set location(val) {
    if (typeof val !== 'string') {
      throw TypeError('Location must be a string');
    }
    this._location = val;
  }

  toString() {
    return this.location;
  }

  valueOf() {
    return this.size;
  }
}
