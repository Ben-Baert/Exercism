"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

exports["default"] = function (year) {
  return year % 4 == 0 && !(year % 100 == 0) || year % 400 == 0;
};

module.exports = exports["default"];