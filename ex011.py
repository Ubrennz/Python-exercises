largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
litros_de_tinta_por_metro = area / 2

print(f'Sua parede tem as dimenções {largura} x {altura} e sua área é de {area:.2f}m²')
print(f'Para pintar essa parede, vc precisará de {litros_de_tinta_por_metro:.2f}L de tinta')