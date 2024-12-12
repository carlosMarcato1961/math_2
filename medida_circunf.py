import letra_por_letra
import random

def medida_circunf(numeros_inteiros,resp,palavra,page):
    if len(numeros_inteiros) == 1:
        if 'raio' in palavra:
            medida_circunf = round((numeros_inteiros[0] * 2) * 3.1416, 3)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            medida_circ = str(medida_circunf).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Ótima pergunta, lembrando que uma circunferência é uma figura\n'
            conteudo_2 = 'geométrica de formato circular, cuja a fórmula para calcular é diâmetro x PI.\n'
            conteudo_3 = f'Portanto, a medida da circunferência  de raio {numeros_inteiros_local} é  {medida_circ}'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        elif 'diametro' in palavra:
            medida_circunf = round(numeros_inteiros[0]  * 3.1416, 3)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            medida_circ = str(medida_circunf).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Ótima pergunta, lembrando que uma circunferência é uma figura\n'
            conteudo_2 = 'geométrica de formato circular, cuja a fórmula para calcular é diâmetro x PI.\n'
            conteudo_3 = f'Portanto, a medida da circunferência  de diâmetro {numeros_inteiros_local} é  {medida_circ}'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            letra_por_letra.letra_por_letra_resp('Erro de digitação,\npreciso que especifique o valor do raio ou do diâmetro\npara eu calcular a medida da circunferência, tente novamente.',resp,page)
    elif len(numeros_inteiros) == 0:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado nenhum número,\n por favor digite o valor do raio ou do diâmetro para eu calcular\na medida da circunferência, tente novamente.',resp,page)
    elif len(numeros_inteiros) > 1:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, por favor digite apenas um número\npara o valor do diâmetro ou raio para eu calcular a medida da circunferência.\nTente novamente.',resp,page)