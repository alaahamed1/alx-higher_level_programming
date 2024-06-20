#!/usr/bin/node
exports.esrever = function (list) {
  newList = [];
  for (element of list) {
    newList.unshift(element);
  }
  return newList;
};
