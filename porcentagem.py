import letra_por_letra
import random

def porcentagem(numeros_inteiros, resp,erro,pergunta,page):
        if len(numeros_inteiros) == 2:        
            porc = round(numeros_inteiros[1]/100*numeros_inteiros[0], 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            porcentagem = str(porc).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
            conteudo_1 = f'Certo, vamos calcular {numeros_inteiros_local} porcento de {numeros_inteiros_local_1}.\n'
            conteudo_2 = f'Respondendo a sua questão {numeros_inteiros_local}% de {numeros_inteiros_local_1} é {porcentagem}'
            resposta = f'{conteudo_1}{conteudo_2}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)

        else:
            if len(numeros_inteiros) > 2:
                letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n tem mais numeros que preciso para calcular.\n Digite apenas 2 número.\nExemplo 20% de 80.',resp,page)
            elif len(numeros_inteiros) < 2:
                letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n preciso de 2 número para calcular.\nExemplo 20% de 80.',resp,page)
