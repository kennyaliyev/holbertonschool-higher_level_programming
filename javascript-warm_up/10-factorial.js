#!/usr/bin/node
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1
  }
  return n * factorial(n - 1)
}

const arg = process.argv[2]
const num = parseInt(arg)

// If NaN, use 0 so factorial returns 1
const n = isNaN(num) ? 0 : num

console.log(factorial(n))
