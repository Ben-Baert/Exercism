const _ = require('underscore')

class Hamming {
  compute (s1, s2) {
    if (s1.length !== s2.length) {
      throw new Error("DNA strands must be of equal length.")
    }
    return _.zip(s1, s2).filter([x, y] => x !== y).length 
  }
}

export default Hamming
