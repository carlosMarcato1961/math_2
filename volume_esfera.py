import letra_por_letra
import random


def volume_esfera(numeros_inteiros,resp,palavra,page):
    if len(numeros_inteiros) == 1:
        if 'raio' in palavra:
            volume_esfera = round((4/3) * 3.1416 * (numeros_inteiros[0] ** 3), 3)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            volume_esp = str(volume_esfera).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Boa pergunta, vamos calcular o volume da esfera.\n'
            conteudo_2 = 'Para isso usamos a fórmula V = (4/3) * PI * (r³).\n'
            conteudo_3 = 'Se o problema apresentar o valor do diâmetro então\n'
            conteudo_4 = 'devemos usar a fórmula V = (4/3) * PI * (d/2)³. Dito isto\n'
            conteudo_5 = f'o volume da esfera de raio {numeros_inteiros_local} é {volume_esp}'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        elif 'diametro' in palavra:
            volume_esfera = round((4/3) * 3.1416 * (numeros_inteiros[0]/2)**3, 3)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            volume_esp = str(volume_esfera).replace('.',',') 
            numeros_inteiros_local = str(numeros_inteiros[0]).replace('.',',')
            conteudo_1 = 'Boa pergunta, vamos calcular o volume da esfera.\n'
            conteudo_2 = 'Para isso usamos a fórmula V = (4/3) * PI * (r³).\n'
            conteudo_3 = 'Se o problema apresentar o valor do diâmetro então\n'
            conteudo_4 = 'devemos usar a fórmula V = (4/3) * PI * (d/2)³. Dito isto\n'
            conteudo_5 = f'o volume da esfera de diâmetro {numeros_inteiros_local} é {volume_esp}'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            letra_por_letra.letra_por_letra_resp('Erro de digitação,\npreciso que especifique o valor do raio ou do diâmetro\npara eu calcular o volume da esfera, tente novamente.',resp,page)
    elif len(numeros_inteiros) == 0:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, não foi digitado nenhum número,\n por favor digite o valor do raio ou do diâmetro para eu calcular\no volume da esfera, tente novamente.',resp,page)
    elif len(numeros_inteiros) > 1:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, por favor digite apenas um número\npara o valor do diâmetro ou raio para eu calcular o volume da esfera.\nTente novamente.',resp,page)