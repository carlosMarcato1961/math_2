import letra_por_letra
import random

def volume_cubo(numeros_inteiros,resp,palavra,page):
    if len(numeros_inteiros) == 1:
        volume_cubo = round(numeros_inteiros[0] ** 3, 3)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        volume_cubo1 = str(volume_cubo).replace('.',',')
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        conteudo_1 = 'Boa pergunta, vamos calcular o volume do cubo, lembrando que cubo tem todos os lados iguais.\n'
        conteudo_2 = 'Para calcular o volume usamos a fórmula V = LxLxL, onde L é o valor de uma das arestas do cubo.\n'
        conteudo_3 = f'Explicado isto, o volume do cubo de lado {numeros_inteiros_local} é {volume_cubo1}'
        resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    elif len(numeros_inteiros) == 0:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado nenhum número,\ncomo o cubo tem todos os lados iguais basta digitar o valor de uma das arestas\npara o volume do cubo ser calculado.',resp,page)
    elif len(numeros_inteiros) > 1:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado mais números que o necessário,\ncomo o cubo tem todos os lados iguais basta digitar o valor de uma das arestas\npara o volume do cubo ser calculado.',resp,page)
