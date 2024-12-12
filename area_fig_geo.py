from math import tan, radians
import letra_por_letra
import random

def area_fig_geo(numeros_inteiros, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 2:
        tangente = round(tan(radians(360/numeros_inteiros[0]/2)), 2)
        h = round((numeros_inteiros[1] / 2) / tangente, 2)
        area_triang = round((numeros_inteiros[1]/2 * h), 2)
        area_fig_geo = round(area_triang * numeros_inteiros[0], 2)
        area_figura_geo = str(area_fig_geo).replace('.',',') 
        numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
        numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
        conteudo_1 = 'Certo, vamos calcular a área desta figura geométrica regular.\n'
        conteudo_2 = f'Uma figura com número de lados igual a {numeros_inteiros_local_0} e com a medida destes lados igual a {numeros_inteiros_local_1}.\n'
        conteudo_3 = f'Tem uma área de {area_figura_geo}'
        resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) < 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, informações númericas não são suficientes.\nPara calcular a área de uma figura geométrica preciso da quantidade\nde lados e quanto mede este lado, por favor tente novamente.',resp,page)
        if len(numeros_inteiros) > 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, excesso de informações númericas.\nPara calcular a área de uma figura geométrica preciso da quantidade\nde lados e quanto mede este lado, por favor tente novamente.',resp,page)
