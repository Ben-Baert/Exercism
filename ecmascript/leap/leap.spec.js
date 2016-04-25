import Tadaa from './leap';

describe('A leap year', () => {

  it('is not very common', () => {
    expect(Tadaa(2015)).toBeFalsy();
  });

  it('is introduced every 4 years to adjust about a day', () => {
    expect(Tadaa(2016)).toBeTruthy();
  });

  it('is skipped every 100 years to remove an extra day', () => {
    expect(Tadaa(1900)).toBeFalsy();
  });

  it('is reintroduced every 400 years to adjust another day', () => {
    expect(Tadaa(2000)).toBeTruthy();
  });

  // Feel free to enable the following tests to check some more examples
  describe('Additional example of a leap year that', () => {

    it('is not a leap year', () => {
      expect(Tadaa(1978)).toBeFalsy();
    });

    it('is a common leap year', () => {
      expect(Tadaa(1992)).toBeTruthy();
    });

    it('is skipped every 100 years', () => {
      expect(Tadaa(2100)).toBeFalsy();
    });

    it('is reintroduced every 400 years', () => {
      expect(Tadaa(2400)).toBeTruthy();
    });

  });

});
