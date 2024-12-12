import letra_por_letra
import math
import re


def extrair_palavras_e_numeros(texto):
    # Expressão regular para encontrar palavras
    padrao_palavras = r'\b\w+\b'
    palavras = re.findall(padrao_palavras, texto)
    
    # Expressão regular para encontrar números decimais
    #padrao_numeros =  r'\b\d+\.\d+\b|\b\d+\b' #padrão para encontrar numeros inteiros r'\b\d+\b'
    padrao_numeros = r'-?\d+\.?\d*'
    numeros = re.findall(padrao_numeros, texto)
    numeros_inteiros = [float(numero) for numero in numeros]
    
    #Padrão para encontrar operadores aritméticos
    padrao_operadores = r'[+\-*=/%!]'
    operadores = re.findall(padrao_operadores, texto)
    
    return palavras, numeros_inteiros, operadores

def calcula_grau2(resp_grau2,page,resp):
    #PERGUNTA: PEGA O TEXTO DO TEXTFIELD PERGUNTA
    # pergunta = str(pergunta.value)
    corrigir1 = resp_grau2.value
    corrigir2 = corrigir1.replace(',' ,'.')
    #TRANSFORMA O TEXTO EM MINUSCULO
    entrada = corrigir2.lower()
    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
    print(palavras, numeros_inteiros, operadores)
    if '=' in operadores and '0' in palavras:
        #não é equação de segundo grau
        if 'x²' not in palavras:
            letra_por_letra.letra_por_letra_resp('Não existe função de segundo grau sem x²',resp,page)
        elif 'x' not in palavras:
            #x²
            if len(numeros_inteiros) == 1:
                letra_por_letra.letra_por_letra_resp('Neste caso o único número que torna a igualdade verdadeira é 0, portanto raiz = 0',resp,page)
            #x²+c
            elif len(numeros_inteiros) == 2:
                #x²+?=0
                if palavras.index('x²') == 1:
                    corrigir3= corrigir2.replace(' x²', '1²')
                    entrada = corrigir3.lower()
                    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                    delta = -4*numeros_inteiros[0]*numeros_inteiros[1]
                    if delta < 0:
                        letra_por_letra.letra_por_letra_resp('Não existem raizes reais, o delta é negativo',resp,page)
                    else:
                        raiz_delta = round(math.sqrt(delta), 3)
                        raiz_1 = round((0 + raiz_delta)/(2*numeros_inteiros[0]),3)
                        raiz_2 = round((0 - raiz_delta)/(2*numeros_inteiros[0]),3)
                        res = f'{raiz_1} e {raiz_2}'
                        letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
                elif palavras.index('x²') == 2:
                    letra_por_letra.letra_por_letra_resp('Raiz desta equação de 2º grau é 0',resp,page)
            elif len(numeros_inteiros) == 3:
                delta = -4*numeros_inteiros[0]*numeros_inteiros[1]
                if delta < 0:
                    letra_por_letra.letra_por_letra_resp('Não existem raizes reais, o delta é negativo',resp,page)
                else:
                    raiz_delta = round(math.sqrt(delta), 3)
                    raiz_1 = round((0 + raiz_delta)/(2*numeros_inteiros[0]),3)
                    raiz_2 = round((0 - raiz_delta)/(2*numeros_inteiros[0]),3)
                    res = f'{raiz_1} e {raiz_2}'
                    letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
        elif 'x²' in palavras and 'x' in palavras:
            #x²+x=0
            if len(numeros_inteiros) == 1:
                corrigir3= corrigir2.replace(' x²', '1²').replace(' x', '1')
                entrada = corrigir3.lower()
                palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                delta = 1
                raiz_1 = round((-numeros_inteiros[1]+1)/(2*numeros_inteiros[0]),3)
                raiz_2 = round((-numeros_inteiros[1]-1)/(2*numeros_inteiros[0]),3)
                res = f'{raiz_1} e {raiz_2}'
                letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
            elif len(numeros_inteiros) == 2:
                #?x²+x=0
                if palavras.index('x²') == 2:
                    corrigir3 = corrigir2.replace('x²', 'c').replace(' x', '1')
                    entrada = corrigir3.lower()
                    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                    delta = 1
                    raiz_1 = round((-numeros_inteiros[1]+1)/(2*numeros_inteiros[0]),3)
                    raiz_2 = round((-numeros_inteiros[1]-1)/(2*numeros_inteiros[0]),3)
                    res = f'{raiz_1} e {raiz_2}'
                    letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
                #x²-?x=0
                elif palavras.index('x') == 3:
                    corrigir3 = corrigir2.replace(' x²', '1²').replace('x', 'c')
                    entrada = corrigir3.lower()
                    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                    delta = round(math.sqrt(numeros_inteiros[1]**2),3)
                    raiz_1 = round((-numeros_inteiros[1]+delta)/(2*numeros_inteiros[0]),3)
                    raiz_2 = round((-numeros_inteiros[1]-delta)/(2*numeros_inteiros[0]),3)
                    res = f'{raiz_1} e {raiz_2}'
                    letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
                #x²+x+?=0
                elif palavras.index('x') == 2:
                    corrigir3 = corrigir2.replace(' x²', '1²')
                    corrigir4 = corrigir3.replace(' x', '1')
                    entrada = corrigir4.lower()
                    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                    delta = numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2]
                    if delta < 0:
                        letra_por_letra.letra_por_letra_resp('Não existem raizes reais, o delta é negativo',resp,page)
                        resp.value = res
                    else:
                        raiz_delta = round(math.sqrt(numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2]),2)
                        raiz_1 = round((-numeros_inteiros[1]+raiz_delta)/(2*numeros_inteiros[0]),3)
                        raiz_2 = round((-numeros_inteiros[1]-raiz_delta)/(2*numeros_inteiros[0]),3)
                        res = f'{raiz_1} e {raiz_2}'
                        letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
            elif len(numeros_inteiros) == 3:
                #?x²-?x=0
                if  palavras.index('x') == 4:
                    delta = round(math.sqrt(numeros_inteiros[1]**2),3)
                    raiz_1 = round((-numeros_inteiros[1]+delta)/(2*numeros_inteiros[0]),3)
                    raiz_2 = round((-numeros_inteiros[1]-delta)/(2*numeros_inteiros[0]),3)
                    res = f'{raiz_1} e {raiz_2}'
                    letra_por_letra.letra_por_letra_resp(f'as raizes da equação de 2º grau são {res}',resp,page)
                #x²+?x+?=0
                elif palavras.index('x²') == 1:
                    corrigir3 = corrigir2.replace(' x²', '1²')
                    entrada = corrigir3.lower()
                    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                    delta = numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2]
                    if delta < 0:
                        letra_por_letra.letra_por_letra_resp('Não existem raizes reais, o delta é negativo',resp,page)
                        resp.value = res
                    else:
                        raiz_delta = round(math.sqrt(numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2]),3)
                        raiz_1 = round((-numeros_inteiros[1]+raiz_delta)/(2*numeros_inteiros[0]),3)
                        raiz_2 = round((-numeros_inteiros[1]-raiz_delta)/(2*numeros_inteiros[0]),3)
                        res = f'{raiz_1} e {raiz_2}'
                        letra_por_letra.letra_por_letra_resp(f'As raizes da equação de 2º grau são {res}',resp,page)
                #?x²-x+?=0
                elif palavras.index('x²') == 2:
                    corrigir5 = corrigir2.replace('x²', 'c').replace('x', '1')
                    entrada = corrigir5.lower()
                    palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
                    delta = round(numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2],3)
                    if delta < 0:
                        letra_por_letra.letra_por_letra_resp('Não existem raizes reais, o delta é negativo',resp,page)
                    else:
                        raiz_delta = round(math.sqrt(numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2]),2)
                        raiz_1 = round((-numeros_inteiros[1]+raiz_delta)/(2*numeros_inteiros[0]),3)
                        raiz_2 = round((-numeros_inteiros[1]-raiz_delta)/(2*numeros_inteiros[0]),3)
                        res = f'{raiz_1} e {raiz_2}'
                        letra_por_letra.letra_por_letra_resp(f'As raizes da equação de 2º grau são {res}',resp,page)
            elif len(numeros_inteiros) == 4:
                delta = round(numeros_inteiros[1]**2 - 4 * numeros_inteiros[0] * numeros_inteiros[2],3)
                if delta < 0:
                    letra_por_letra.letra_por_letra_resp('Não existem raizes reais, o delta é negativo',resp,page)
                else:
                    raiz_delta = round(math.sqrt(delta),2)

                    raiz_1 = round((-numeros_inteiros[1]+raiz_delta)/(2*numeros_inteiros[0]),3)
                    raiz_2 = round((-numeros_inteiros[1]-raiz_delta)/(2*numeros_inteiros[0]),3)
                    res = f'{raiz_1} e {raiz_2}'
                    letra_por_letra.letra_por_letra_resp(f'As raizes da equação de 2º grau são {res}',resp,page)
    else:
        letra_por_letra.letra_por_letra_resp('digite =0 para equação de 2º grau',resp,page)
    
    return calcula_grau2