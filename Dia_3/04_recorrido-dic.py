capitales={
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Colombia':'Bogotá'
}
print('='*50 + "Recorrido por clave")
#1 recorrido por claves
for clave in capitales.keys():
    print(clave)
    
print('='*50 + "Recorrido por valor")

#recorrido por valores
for valor in capitales.values():
    print(valor)

print('='*50 + "Recorrido por clave,valor")    
#recorrido por clave, valor
for clave,valor in capitales.items():
    print(f'la capital de {clave} es {valor}')
