import letra_por_letra
import random
def potencia(numeros_inteiros, resp,erro,pergunta,page):
    if len(numeros_inteiros) == 2:
        pot = round(numeros_inteiros[0] ** numeros_inteiros[1], 3)
        #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
        potencia = str(pot).replace('.',',') 
        numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
        numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
        conteudo_1 = f'Certo, vamos resolver {numeros_inteiros_local} elevado a {numeros_inteiros_local_1}.\n'
        conteudo_2 = f' Respondendo a sua questão, {numeros_inteiros_local} elevado ao expoente {numeros_inteiros_local_1}\n retorna o resultado {potencia}'
        resposta = f'{conteudo_1}{conteudo_2}'
        letra_por_letra.letra_por_letra_resp(resposta,resp,page)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) < 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n preciso de 2 número para calcular.',resp,page)
        elif len(numeros_inteiros) > 2:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\ntem mais numeros que preciso para calcular.\nDigite o número que é a base e o expoente.',resp,page)
