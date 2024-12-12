import letra_por_letra
import random

def volume_paralelep(numeros_inteiros,resp,palavra,page):
    if len(numeros_inteiros) == 3:
        volume_cubo = round(numeros_inteiros[0] * numeros_inteiros[1] * numeros_inteiros[2], 3)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        volume_cubo1 = str(volume_cubo).replace('.',',')
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
        numeros_inteiros_local_2 = str(numeros_inteiros[2]).replace('.',',')
        conteudo_1 = 'Entendi, vamos calcular o volume do paralelepípedo, é quase igual a calcular o volume do cubo.\n'
        conteudo_2 = 'O calculo é feito multiplicando a área da base pelo valor da altura.\n'
        conteudo_3 = f'Desta forma, o volume do paralelepípedo de lados {numeros_inteiros_local_1}, {numeros_inteiros_local_2} e {numeros_inteiros_local} é   {volume_cubo1}'
        resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    elif len(numeros_inteiros) < 3:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado números suficientes,\ncomo o paralelepípedo tem arestas com medidas diferentes preciso\nde 3 medidas para o volume do paralelepípedo ser calculado.\nPreciso da altura, comprimento e largura.',resp,page)
    elif len(numeros_inteiros) > 3:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado exesso de números,\ncomo o paralelepípedo tem arestas com medidas diferentes preciso\nde 3 medidas para o volume do paralelepípedo ser calculado.\nPreciso da altura, comprimento e largura.',resp,page)
