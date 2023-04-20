num = int(input('Informe um número de 3 digitos: '))

n1 = num // 100
resto = num % 100

n2 = resto // 10
n3 = resto % 10

soma = n1 + n2 + n3

print(n1)
print(n2)
print(n3)
print(f'A soma é {soma}')

