#!/bin/bash
echo "Digite o primeiro número:"
read num1
echo "Digite o segundo número:"
read num2
echo "Escolha uma operação (+, -, *, /):"
read op
case $op in
    +) echo "Resultado: $(($num1 + $num2))" ;;
    -) echo "Resultado: $(($num1 - $num2))" ;;
    \*) echo "Resultado: $(($num1 * $num2))" ;;
    /) echo "Resultado: $(($num1 / $num2))" ;;
    *) echo "Operação inválida!" ;;
esac # Ctrl+o para salvar, depois ENTER para confirmar e Ctrl+x para sair#
