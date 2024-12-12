from math import sqrt
import letra_por_letra
import random

def area_tri_isoc(numeros_inteiros,palavras, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 2:
        if 'lados' in palavras and 'base' in palavras:
            #retorna o indece da palavra buscada
            indice_lados = palavras.index('lados')  
            indice_base = palavras.index('base')  
            if indice_base > indice_lados:
                    triang = round((numeros_inteiros[1] / 2) * (sqrt(numeros_inteiros[0] ** 2 - numeros_inteiros[1] ** 2 / 4)), 2)
                    #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
                    triangulo = str(triang).replace('.',',') 
                    numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
                    numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
                    conteudo_1 = 'Certo! Vamos calcular a área de um triângulo isóceles\n'
                    conteudo_2 = f'com base {numeros_inteiros_local_1} e dois lados iguais a {numeros_inteiros_local}.\n' 
                    conteudo_4 = 'Um triângulo isóceles de lados iguais a\n'
                    conteudo_5 = f' {numeros_inteiros_local} e base {numeros_inteiros_local_1} tem uma área igual a {triangulo}.'
                    resposta = f'{conteudo_1}{conteudo_2}{conteudo_4}{conteudo_5}'
                    letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                    #Frase escolhidas aleatorimente para mostrar na tela
                    texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                    texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                    texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                    texto_aleatorio = random.choice([texto1, texto2, texto3])
                    letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
            elif indice_lados > indice_base:
                    triang = round((numeros_inteiros[0] / 2) * (sqrt(numeros_inteiros[1] ** 2 - numeros_inteiros[0] ** 2 / 4)), 2)
                    #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
                    triangulo = str(triang).replace('.',',') 
                    numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
                    numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
                    conteudo_1 = 'Certo! Vamos calcular a área de um triângulo isóceles\n'
                    conteudo_2 = f'com base {numeros_inteiros_local_0} e lados dois iguais {numeros_inteiros_local_1}.\n' 
                    conteudo_4 = 'Um triângulo isóceles de base igual a\n'
                    conteudo_5 = f' {numeros_inteiros_local_0} e lados iguais {numeros_inteiros_local_1} tem uma área igual a {triangulo}.'
                    resposta = f'{conteudo_1}{conteudo_2}{conteudo_4}{conteudo_5}'
                    letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                    #Frase escolhidas aleatorimente para mostrar na tela
                    texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                    texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                    texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                    texto_aleatorio = random.choice([texto1, texto2, texto3])
                    letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            letra_por_letra.letra_por_letra_resp('Certo, entendi que você quer achar a área de um triangulo isóceles, porém não entendi os valores, se digitar um valor para base e um valor dos dois lados iguais,\npor exemplo base igual a 5 e lados iguais 6. Obrigado!',resp,page)

    if len(numeros_inteiros) == 3:
        if numeros_inteiros[0] == numeros_inteiros[1]:
            triang = round((numeros_inteiros[2] / 2) * (sqrt(numeros_inteiros[0] ** 2 - numeros_inteiros[2] ** 2 / 4)), 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            triangulo = str(triang).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[2]).replace('.',',')
            conteudo_1 = 'Certo! Vamos calcular a área de um triângulo isóceles\n'
            conteudo_2 = f'com base {numeros_inteiros_local_1} e dois lados iguais a {numeros_inteiros_local}.\n' 
            conteudo_4 = 'Um triângulo isóceles de lados iguais a\n'
            conteudo_5 = f' {numeros_inteiros_local} e base {numeros_inteiros_local_1} tem uma área igual a {triangulo}.'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_4}{conteudo_5}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        elif numeros_inteiros[1] == numeros_inteiros[2]:
            triang = round((numeros_inteiros[0] / 2) * (sqrt(numeros_inteiros[1] ** 2 - numeros_inteiros[0] ** 2 / 4)), 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            triangulo = str(triang).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[1]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Certo! Vamos calcular a área de um triângulo isóceles\n'
            conteudo_2 = f'com base {numeros_inteiros_local_1} e dois lados iguais a {numeros_inteiros_local}.\n' 
            conteudo_4 = 'Um triângulo isóceles de lados iguais a\n'
            conteudo_5 = f' {numeros_inteiros_local} e base {numeros_inteiros_local_1} tem uma área igual a {triangulo}.'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_4}{conteudo_5}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)        
        else:
            letra_por_letra.letra_por_letra_resp('Certo, entendi que você quer achar a área de um triângulo isóceles, porém não entendi os valores, se digitar um valor para BASE e um valor dos dois LADOS iguais,\npor exemplo base igual a 5 e lados iguais 6. Obrigado!',resp,page)

    else:
        if len(numeros_inteiros) < 2 and len(numeros_inteiros) > 3:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n Já que o triângulo isóceles tem 2 lados iguais e\n uma base diferente, basta digitar o valor de um dos lados iguais\n e o valor da base para fazer o cálculo da área.',resp,page)
