num = float(input("Quantos reais? R$"))

digito_extenso = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove"]
casas_dezena = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
casas_centena = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

str_num = str(num)

pre_virgula = ""
pos_virgula = ""

def extenso(str_num):
    str_num = str_num.lstrip("0")

    if int(str_num) <= 19:
        return f"{digito_extenso[int(str_num)]}"
    elif int(str_num) == 100:
        return f"cem"
    else:
        final_zero = int(str_num[1:]) == 0
        quant_digitos = len(str_num)

        if quant_digitos == 2:
            if final_zero:
                return f"{casas_dezena[int(str_num[0]) - 2]}"
            else:
                return f"{casas_dezena[int(str_num[0]) - 2]} e {digito_extenso[int(str_num[1])]}"
        elif quant_digitos == 3:
            ultimos = int(str_num[1:])

            if final_zero:
                return f"{casas_centena[int(str_num[0]) - 1]}"
            elif ultimos < 19:
                return f"{casas_centena[int(str_num[0]) - 1]} e {digito_extenso[ultimos]}"
            elif str_num[1] != "0" and str_num[2] == "0":
                return f"{casas_centena[int(str_num[0]) - 1]} e {casas_dezena[int(str_num[1]) - 2]}"
            elif str_num[1] == "0" and str_num[2] != "0":
                return f"{casas_centena[int(str_num[0]) - 1]} e {digito_extenso[int(str_num[2])]}"
            else:
                return f"{casas_centena[int(str_num[0]) - 1]} e {casas_dezena[int(str_num[1]) - 2]} e {digito_extenso[int(str_num[2])]}"


quant_digitos = len(str_num[:str_num.find(".")])

if int(num) == 0:
    pre_virgula = f"zero reais"
elif quant_digitos < 4:
    pre_virgula = f"{extenso(str_num[0:str_num.find('.')])} reais"
elif quant_digitos == 4:
    centena = str_num[1:str_num.find(".")].lstrip("0")
    final_zero = int(str_num[1:str_num.find(".")]) == 0

    if int(num) == 1000:
        pre_virgula = "mil reais"
    elif str_num[0] == "1":
        pre_virgula = f"mil e {extenso(centena)} reais"
    elif final_zero:
        pre_virgula = f"{digito_extenso[int(str_num[0])]} mil reais"
    else:
        pre_virgula = f"{digito_extenso[int(str_num[0])]} mil e {extenso(centena)} reais"
elif quant_digitos == 5:
    dezena = str_num[:2]
    centena = str_num[2:str_num.find(".")]

    if int(centena) == 0:
        pre_virgula = f"{extenso(dezena)} mil reais"
    else:
        pre_virgula = f"{extenso(dezena)} mil e {extenso(centena)} reais"
elif quant_digitos == 6:
    centena1 = str_num[:3]
    centena2 = str_num[3:str_num.find(".")]

    if int(centena2) == 0:
        pre_virgula = f"{extenso(centena1)} mil reais"
    else:
        pre_virgula = f"{extenso(centena1)} mil e {extenso(centena2)} reais"
elif quant_digitos == 7:
    centena1 = str_num[1:4]
    centena2 = str_num[4:str_num.find(".")]

    if int(centena1) == 0 and int(centena2) == 0:
        pre_virgula = f"{digito_extenso[int(str_num[0])]} milhões de reais"
    elif int(centena1) == 0:
        pre_virgula = f"{digito_extenso[int(str_num[0])]} milhões e {extenso(centena2)} reais"
    elif int(centena2) == 0:
        pre_virgula = f"{digito_extenso[int(str_num[0])]} milhões {extenso(centena1)} mil reais"
    else:
        pre_virgula = f"{digito_extenso[int(str_num[0])]} milhões {extenso(centena1)} mil e {extenso(centena2)} reais"
elif quant_digitos == 8:
    dezena = str_num[:2]
    centena1 = str_num[2:5]
    centena2 = str_num[5:str_num.find(".")]

    if int(centena1) == 0 and int(centena2) == 0:
        pre_virgula = f"{extenso(dezena)} milhões de reais"
    elif int(centena1) == 0:
        pre_virgula = f"{extenso(dezena)} milhões e {extenso(centena2)} reais"
    elif int(centena2) == 0:
        pre_virgula = f"{extenso(dezena)} milhões {extenso(centena1)} mil reais"
    else:
        pre_virgula = f"{extenso(dezena)} milhões {extenso(centena1)} mil e {extenso(centena2)} reais"
elif quant_digitos == 9:
    centena1 = str_num[:3]
    centena2 = str_num[3:6]
    centena3 = str_num[6:str_num.find(".")]

    if int(centena2) == 0 and int(centena3) == 0:
        pre_virgula = f"{extenso(centena1)} milhões de reais"
    elif int(centena2) == 0:
        pre_virgula = f"{extenso(centena1)} milhões e {extenso(centena3)} reais"
    elif int(centena3) == 0:
        pre_virgula = f"{extenso(centena1)} milhões {extenso(centena2)} mil reais"
    else:
        pre_virgula = f"{extenso(centena1)} milhões {extenso(centena2)} mil e {extenso(centena3)} reais"


centavos = str_num[str_num.find(".") + 1:]

if centavos != "0":
    if len(centavos) == 1:
        centavos += "0"

    pos_virgula = extenso(centavos)

if pos_virgula == "":
    print(f"{pre_virgula}")
else:
    print(f"{pre_virgula} e {pos_virgula} centavos")