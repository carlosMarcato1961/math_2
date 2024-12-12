import letra_por_letra
import random

def area_quad(numeros_inteiros, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1 or len(numeros_inteiros) == 4:
        quad = numeros_inteiros[0] * numeros_inteiros[0]
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        quadrado = str(quad).replace('.',',') 
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = f'Certo! Vamos calcular a área de um quadrado com lado {numeros_inteiros_local}.\n'
        conteudo_2 = f'A área de um quadrado de lados {numeros_inteiros_local} é {quadrado}'
        resposta = f'{conteudo_1}{conteudo_2}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    elif len(numeros_inteiros) > 1 and len(numeros_inteiros) != 4:
        quad = numeros_inteiros[0] * numeros_inteiros[0]
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        quadrado = str(quad).replace('.',',') 
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = f'OK! Vou calcular a área do quadrado usando o {numeros_inteiros_local},\nque é o primeiro valor que você digitou.'
        conteudo_2 = f'\nSó preciso de um valor para fazer esse cálculo, pois se trata de um quadrado.\nDito isto a área de um quadrado de lados {numeros_inteiros_local} é {quadrado}'
        resposta = f'{conteudo_1}{conteudo_2}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) < 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\nvocê não digitou nenhum valor.\nPreciso de pelo menos do valor de 1 lado para calcular.',resp,page)
