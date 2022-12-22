def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '/':
        return num1 / num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '//':
        return num1 // num2
    elif operacao == '**':
        return num1 ** num2
    elif operacao == '%':
        return num1 % num2

resultado = calculadora (10, 20, '*')
print(resultado)