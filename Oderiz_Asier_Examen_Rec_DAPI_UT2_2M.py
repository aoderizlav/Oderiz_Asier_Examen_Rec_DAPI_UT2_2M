import csv

countries_dict = {"30": "Grecia", "33": "Francia", "34": "España", "351": "Portugal", "380": "Ucrania", "39": "Italia",
                  "41": "Suiza", "44": "Reino Unido", "49": "Alemania", "7": "Rusia"}

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F", "8": "P", "9": "D",
            "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V", "18": "H",
            "19": "L", "20": "C", "21": "K", "22": "E"}


def check_DGT(ruta):
    """
    Es una funcion general que:
    -Abre un fichero de texto
    -Comprueba los datos
    -Sobre-escribe los datos corregidos
    -Cierra el fichero y finalica la ejecución
     Entradas:
       -ruta del fichero (.csv) a abrir
    Salidas:
      -
    """
    file = open(ruta, "r", encoding="utf-8")
    base = file.readlines()
    lista = []
    file.close()
    with open(ruta, "w", encoding="utf-8", newline="") as file:
        campos = ["Nombre", "Apellidos", "DNI", "Telefono", "País", "Vehiculo",
                  "Multas Radar", "Multas ITV", "Multas Estupefacientes", "Total Multas"]
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        for separar_datos in base:
            lista.append(separar_datos.split(","))
        lista_DGT = []
        for persona in lista[1:]:
            dgt = {}
            dgt["Nombre"] = persona[0]
            dgt["Apellidos"] = persona[1]
            dgt["DNI"] = persona[2]
            dgt["Telefono"] = persona[3]
            dgt["Vehiculo"] = persona[4]
            dgt["Multas Radar"] = persona[5]
            dgt["Multas ITV"] = persona[6]
            dgt["Multas Estupefacientes"] = persona[7]
            lista_DGT.append(dgt)
        for datos in lista_DGT:
            datos["Nombre"] = check_username(datos["Nombre"])
            datos["Apellidos"] = check_username(datos["Apellidos"])
            datos["DNI"] = check_nif(datos["DNI"])
            datos["Telefono"] = check_phone(datos["Telefono"])
            datos["Total Multas"] = calculate_bill(datos["Multas Radar"], datos["Multas ITV"],
                                                   datos["Multas Estupefacientes"])
            writer.writerow(datos)
    return

def check_username(user_name):

    """
    Esta funcion recibe un nombre y apellido sin formato y devuelve el nombre y apellido capitalizado
    Entradas:
       -nombre: nombre el cual va a capitalizar el programa
       -apellidos: apellidos los cuales va a capitalizar el programa
    Salidas:
       -nombre: nombre capitalizado
       -apellidos: apellidos capitalizados
    """
    return user_name.title()

def check_nif(user_nif):
    """
    Es una funcion que realiza la comprobación matemática para determinar si el número del nif
    se corresponde con la letra asociada
     Entradas:
       -nif del usuario/a: en formato de 8 números y una letra
    Salidas:
       -nif corregido
    """
    number = str(user_nif[0:8])
    letra = nif_dict[str(int(user_nif[0:8]) % 23)]
    return number + letra

def check_phone(num_entero):
    """
    Es una funcion que permite chequear e identificar si un número de teléfono está bien escrito y a qué país
    corresponde su prefijo
     Entradas:
       -número de teléfono completo
    Salidas:
       -pais al que corresponde el numero de telefono
       -número de teléfono reformateado correctamente
    """
    desglose1 = num_entero.split("(")
    desglose2 = desglose1[1].split(")")
    desglose3 = desglose2[1].split("-")
    prefijo = desglose2[0]
    numero = desglose3[0] + desglose3[1]
    pais_prefijo = countries_dict[prefijo]
    telefono = "+" + prefijo + "-" + numero
    return str(pais_prefijo + " " + telefono)

def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """
    Esta funcion realiza la suma de la cantidad de las multas y devuelve el total a pagar
    Entradas:
       -multas_radar
       -multas_ITV
       -multas_estupefacientes
    Salidas:
       -bill: total a pagar
    """
    bill = int(multas_radar) + int(multas_ITV) + int(multas_estupefacientes)
    return bill


check_DGT("C:/Users/HP/Desktop/Pycharm/Oderiz_Asier_Examen_Rec_DAPI_UT2_2M/Asier Oderiz Lavilla - DGT.csv")

help(check_DGT)
help(check_username)
help(check_nif)
help(check_phone)
help(calculate_bill)



