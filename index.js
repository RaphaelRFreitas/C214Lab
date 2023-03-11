const Calculadora = require('./src/calculadora');

const a = 2;
const b = 3;
let op = '+';

console.log(Calculadora.calc(a, b, op));

op = '-';
console.log(Calculadora.calc(a, b, op));

op = '*';
console.log(Calculadora.calc(a, b, op));

op = '/';
console.log(Calculadora.calc(a, b, op));

op = '**';
console.log(Calculadora.calc(a, b, op));

op = 'a';
console.log(Calculadora.calc(a, b, op));

op = '+';
console.log(Calculadora.calc('String', b, op));