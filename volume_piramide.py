from math import tan, radians
import letra_por_letra
import random

def volume_piramide(numeros_inteiros, resp,palavras,page):
    if len(numeros_inteiros) == 3:
        if 'lado' in palavras and 'altura' in palavras:
            indice_lados = palavras.index('lado')
            indice_altura = palavras.index('altura')
            if indice_altura > numeros_inteiros[1]:
                tangente = round(tan(radians(360/numeros_inteiros[0]/2)), 3)
                h = round((numeros_inteiros[1] / 2) / tangente, 3)
                area_triang = round((numeros_inteiros[1]/2 * h), 3)
                area_fig_geo = round(area_triang * numeros_inteiros[0], 3)
                area_piramide = round((area_fig_geo * numeros_inteiros[2]) / 3, 3)
                area_piram = str(area_piramide).replace('.',',') 
                numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
                numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
                numeros_inteiros_local_2 = str(numeros_inteiros[2]).replace('.',',')
                conteudo_1 = 'Certo, vamos calcular o volume de uma piramide com base regular.\n'
                conteudo_2 = f'Neste caso, uma piramide com {numeros_inteiros_local_0} lados,\ncom a medida destes lados {numeros_inteiros_local_1} e altura igual a {numeros_inteiros_local_2}.\n'
                conteudo_3 = f'Respondendo sua questão o volume desta piramide é de {area_piram}.'
                resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
                letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                #Frase escolhidas aleatorimente para mostrar na tela
                texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                texto_aleatorio = random.choice([texto1, texto2, texto3])
                letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
            else:
                tangente = round(tan(radians(360/numeros_inteiros[1]/2)), 3)
                h = round((numeros_inteiros[2] / 2) / tangente, 3)
                area_triang = round((numeros_inteiros[2]/2 * h), 3)
                area_fig_geo = round(area_triang * numeros_inteiros[1], 3)
                area_piramide = round((area_fig_geo * numeros_inteiros[0]) / 3, 3)
                area_piram = str(area_piramide).replace('.',',') 
                numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
                numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
                numeros_inteiros_local_2 = str(numeros_inteiros[2]).replace('.',',')
                conteudo_1 = 'Certo, vamos calcular o volume de uma piramide com base regular.\n'
                conteudo_2 = f'Neste caso, uma piramide com {numeros_inteiros_local_1} lados,\ncom a medida destes lados {numeros_inteiros_local_2} e altura igual a {numeros_inteiros_local_0}.\n'
                conteudo_3 = f'Respondendo sua questão o volume desta piramide é de {area_piram}.'
                resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
                letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                #Frase escolhidas aleatorimente para mostrar na tela
                texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                texto_aleatorio = random.choice([texto1, texto2, texto3])
                letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            conteudo = 'Erro, entendi que você quer saber o volume de uma pirâmide,\nporém não entendi o enunciado da questão.\nPreciso da quantidade de lados da base, a medida de um lado\ne também a medida da altura da pirâmide, por favor tente novamente.'
            letra_por_letra.letra_por_letra_resp(conteudo,resp,page)
    elif len(numeros_inteiros) < 3:
        letra_por_letra.letra_por_letra_resp(f'Foi digitado {len(numeros_inteiros)} dados, não há informações numéricas suficientes,\npor favor digite o valor número de lados da base,\na medida de um lado e a altura da pirâmide para eu\ncalcular o volume da pirâmide, tente novamente.',resp,page)
    elif len(numeros_inteiros) > 3:
        letra_por_letra.letra_por_letra_resp(f'Foi digitado {len(numeros_inteiros)} dados, há excesso informações numéricas,\npor favor digite o valor número de lados da base,\na medida de um lado e a altura da pirâmide para eu\ncalcular o volume da pirâmide, tente novamente.',resp,page)
