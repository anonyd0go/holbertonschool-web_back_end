export default class Currency {
  constructor(code, name) {
    this.name = name;
    this.code = code;
  }

  get name() {
    return this._name;
  }

  set name(val) {
    if (typeof val !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = val;
  }

  get code() {
    return this._code;
  }

  set code(val) {
    if (typeof val !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = val;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
