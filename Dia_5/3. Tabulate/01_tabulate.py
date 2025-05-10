from tabulate import tabulate

data=[
    ["100","cesar","cesar@gmail.com"],
    ["200","ana","ana@gmail.com"],
    ["400","Mar","mar@gmail.com"],
    ["500","Jorge","Jorge@gmail.com"],
]
columnas=["DNI","NOMBRE","EMAIL"]
tabla=tabulate(data,headers=columnas,tablefmt="heavy_outline")
print(tabla)