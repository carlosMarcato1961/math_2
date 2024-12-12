import math
import letra_por_letra
import random

#FUNÇÃO PARA CALCULAR OS CATETOS
def calcular_cat_op(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros) == 2:
        if numeros_inteiros[0] > numeros_inteiros[1]:
            cat = round(math.sqrt(numeros_inteiros[0]**2 - numeros_inteiros[1]**2), 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            cateto = str(cat).replace('.',',') 
            numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
            conteudo_1 = 'tudo bem, vamos calcular o cateto deste triângulo retângulo.\n'
            conteudo_2 = f'A medida do cateto com hipotenusa igual a {numeros_inteiros_local_0} e cateto igual a {numeros_inteiros_local_1} é {cateto}'
            resposta = f'{conteudo_1}{conteudo_2}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)

        elif numeros_inteiros[0] < numeros_inteiros[1]:
            cat = round(math.sqrt(numeros_inteiros[1]**2 - numeros_inteiros[0]**2), 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            cateto = str(cat).replace('.',',') 
            numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
            conteudo_1 = 'tudo bem, vamos calcular o cateto deste triângulo retângulo.\n'
            conteudo_2 = f'A medida do cateto com hipotenusa igual a {numeros_inteiros_local_1} e o outro cateto igual a {numeros_inteiros_local_0} é {cateto}'
            resposta = f'{conteudo_1}{conteudo_2}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) < 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado valores suficientes.\nPara cálculo o cateto é necessário a medida da hipotenusa e do outro cateto.\nPor favor tente novamente.',resp,page)
        if len(numeros_inteiros) > 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado mais de dois números.\nPara cálculo o cateto é necessário a medida da hipotenusa e do outro cateto.\nPor favor tente novamente.',resp,page)
