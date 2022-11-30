#!/usr/bin/node
exports.converter = function (base) {
  return n => n.toString(base);
};
