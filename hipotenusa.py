import math
import letra_por_letra
import random

#FUNÇÃO PARA CALCULAR A HIPOTENUSA
def calcular_hip(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros) == 2:
        hipot = round(math.sqrt(numeros_inteiros[0]**2 + numeros_inteiros[1]**2), 3)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        hipotenusa = str(hipot).replace('.',',') 
        numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
        numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
        conteudo_1 = 'Boa pergunta, vamos calcular a hipotenusa deste triângulo retângulo.\n'
        conteudo_2 = f'A medida da hipotenusa com um cateto igual a {numeros_inteiros_local_0} e outro cateto\nigual a {numeros_inteiros_local_1} é {hipotenusa}'
        resposta = f'{conteudo_1}{conteudo_2}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)

    else:
        if len(numeros_inteiros) < 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado valores suficientes.\nPara cálculo da Hipotenusa é necessário a medida dos dois catetos.\nPor favor tente novamente.',resp,page)
        if len(numeros_inteiros) > 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado mais de dois números.\nPara cálculo da Hipotenusa é necessário a medida dos dois catetos.\nPor favor tente novamente.',resp,page)
