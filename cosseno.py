import math
import letra_por_letra
import random

def cosseno(numeros_inteiros, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 1:
        # Calcula o angulo em radiandos e depois calcula o seno
        cosseno = round(math.cos(math.radians(numeros_inteiros[0])), 3)
        cossen = str(cosseno).replace('.',',')
        numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = f'ok, vamos calcular o cosseno do ângulo {numeros_inteiros_local_0}°\n'
        conteudo_3 = f'O cosseno do ângulo {numeros_inteiros_local_0}° é {cossen}.'
        resposta = f'{conteudo_1}{conteudo_3}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) < 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado nenhum número.\nO cálculo do cosseno precisa do valor do ângulo.\nPor favor tente novamente.',resp,page)
        if len(numeros_inteiros) > 1:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado mais de um número.\nO cálculo do cosseno precisa do valor do ângulo.\nPor favor tente novamente.',resp,page)
