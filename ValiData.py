class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

def mes_valido(mes):
    return 1 <= mes <= 12

def ano_valido(ano):
    return 1900 <= ano <= 9999

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dia_valido(dia,mes,ano):
    if mes in [4, 6, 9 ,11]:
        return 1 <= dia <= 30
    elif mes == 2:
        if bissexto(ano):
            return 1 <= dia <= 29
        else: 
            return 1 <= dia <= 28
    else: 
        return 1 <= dia <= 31 
    
def data_valida(data):
    return mes_valido(data.mes) and ano_valido(data.ano) and dia_valido(data.dia, data.mes, data.ano)

data1 = Data(29, 2, 2020)  
data2 = Data(31, 4, 2021)  
data3 = Data(28, 2, 2021)  
data4 = Data(31, 11, 2022) 

print(data_valida(data1))  
print(data_valida(data2))  
print(data_valida(data3))  
print(data_valida(data4))  