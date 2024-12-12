import letra_por_letra
import random

def area_circulo_raio(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1:
        area_circulo = round((numeros_inteiros[0] ** 2) * 3.1416, 2)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        area_circ = str(area_circulo).replace('.',',') 
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = 'tudo bem, vamos calcular a área deste círculo.\n'
        conteudo_2 = f'A área do circulo de raio {numeros_inteiros_local} é {area_circ}'
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
            letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado nenhum número,\n Só preciso que digite o valor do raio\npara eu calcular a área do círculo, tente novamente.',resp,page)
        elif len(numeros_inteiros) > 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, quais dos números digitados é o raio do círculo?\nPor favor digite apenas um valor.',resp,page)

def area_circulo_diametro(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1:
        area_circulo = round(((numeros_inteiros[0]/2) ** 2) * 3.1416, 2)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        area_circ = str(area_circulo).replace('.',',') 
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = 'tudo bem, vamos calcular a área deste círculo.\n'
        conteudo_2 = f'A área do circulo de diâmetro {numeros_inteiros_local} é {area_circ}'
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
            letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado nenhum número,\n Só preciso que digite o valor do diâmetro\npara eu calcular a área do círculo, tente novamente.',resp,page)
        elif len(numeros_inteiros) > 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, quais dos números digitados é o diâmetro do círculo?\nPor favor digite apenas um valor.',resp,page)
