from math import sqrt
import letra_por_letra
import random

def area_tri_equil(numeros_inteiros, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1:
        triang = round((numeros_inteiros[0] ** 2 * sqrt(3)) / 4, 2)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        triangulo = str(triang).replace('.',',') 
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = 'Ok! Vamos calcular a área de um triângulo equilátero,\n'
        conteudo_2 = f'com todos os lados iguais a {numeros_inteiros_local}.\n\n' 
        conteudo_3 = f'Esse triângulo com lados iguais a {numeros_inteiros_local} tem uma área igual a {triangulo}.'
        resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    elif len(numeros_inteiros) == 3:
        if numeros_inteiros[0] == numeros_inteiros[1] == numeros_inteiros[2]:
            triang = round((numeros_inteiros[0] ** 2 * sqrt(3)) / 4, 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            triangulo = str(triang).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Ok! Vamos calcular a área de um triângulo equilátero,\n'
            conteudo_2 = f'com todos os lados iguais a {numeros_inteiros_local}.\n\n' 
            conteudo_3 = f'Esse triângulo com lados iguais a {numeros_inteiros_local} tem uma área igual a {triangulo}.'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            triang = round((numeros_inteiros[0] ** 2 * sqrt(3)) / 4, 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            triangulo = str(triang).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Ok! Vamos calcular a área de um triângulo equilátero,\n'
            conteudo_2 = f'observando que os números digitados não são iguais\ne sabendo que o triângulo equilátero tem os 3 lados iguais,\n'
            conteudo_3 = f'vou usar o número {numeros_inteiros_local}, entendo que todos os lados são iguais a este.\n'
            conteudo_4 = f'Então podemos concluir que\n' 
            conteudo_5 = f'Este triângulo com lados iguais a {numeros_inteiros_local} tem uma área igual a {triangulo}.'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) != 1 and len(numeros_inteiros) != 3:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n Já que o triângulo equilátero tem todos os 3 lados iguais,\n basta digitar o valor de um lado para fazer o cálculo da área.',resp,page)
