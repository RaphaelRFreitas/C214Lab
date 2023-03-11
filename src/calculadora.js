const validate = require('validate.js');
const ValidarEntradas =  require('./validate');

const Calculadora = {
    calc(a, b, op) {
        const validateInputs = validate({a, b, op}, ValidarEntradas.validarEntradas);
        if (validateInputs !== undefined) {
            return "Error: Invalid input";
        }
        switch (op) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
            case '**':
                return a ** b;
            default:
                return "Error: Invalid operation";
        }
    }
}
module.exports = Calculadora;