import math

base = float(input('Base do retângulo: '))
altura = float(input('Altura do retângulo: '))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt((base * base) + (altura * altura))

print(f'AREA = {area:.4f}')
print(f'PERIMETRO = {perimetro:.4f}')
print(f'DIAGONAL = {diagonal:.4f}')