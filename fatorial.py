import letra_por_letra
import random

def fatorial(numeros_inteiros, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1:
        #transforma float em int, pois o calculo do fatorial é feito com inteiros
        num = int(numeros_inteiros[0])
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i 
        res_texto = str(resultado)
        conteudo_1 = f'Certo, você quer calcular o fatorial de {num}.\n'
        conteudo_2 = f'Para resolver nultiplicamos o número por seus antecessores\naté chegar no 1. Dito isso, o Fatorial de {num} é {res_texto}'
        resposta = f'{conteudo_1}{conteudo_2}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)

    else:
        if len(numeros_inteiros) > 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n tem mais numeros que preciso para calcular.\n Digite apenas 1 número.',resp,page)
        elif len(numeros_inteiros) < 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n preciso de pelo menos 1 número para calcular.',resp,page)