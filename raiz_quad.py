from math import sqrt
import letra_por_letra
import random


def raiz_quadrada(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1:
        for num in numeros_inteiros:
            r = round(sqrt(num), 3)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            raiz = str(r).replace('.',',') 
            numeros_inteiros_local = str(num).replace('.',',')
            conteudo_1 = f'Certo, vamos calcular a raiz quadrada de {numeros_inteiros_local}.\n'
            conteudo_2 = f'Raiz quadrada de {numeros_inteiros_local} é {raiz}.\n'
            resposta = f'{conteudo_1}{conteudo_2}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Atualiza Textfield resp
        page.controls.append(resp)
        page.update()
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) < 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n preciso de pelo menos 1 número para calcular.',resp,page)
        elif len(numeros_inteiros) > 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n tem mais numeros que preciso para calcular.\n Digite apenas 1 número.',resp,page)