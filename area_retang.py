import letra_por_letra
import random

def area_retang(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros) == 2:
            area_retang = round(numeros_inteiros[0] * numeros_inteiros[1], 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            area_ret = str(area_retang).replace('.',',') 
            numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
            conteudo_1 = 'Tudo bem, vamos calcular a área deste retângulo.\n'
            conteudo_2 = f'A área do retângulo com dois lados iguais a {numeros_inteiros_local_0} \ne dois lados iguais a {numeros_inteiros_local_1} é {area_ret}\n'
            conteudo_3 = f'Se o que você quer é a área de um triângulo retângulo de catetos {numeros_inteiros_local_0} e {numeros_inteiros_local_1}, a área deste triângulo é {area_retang/2}.\nEspero ter respondido adequadamente 🙂'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)

    elif len(numeros_inteiros) == 4:
        if numeros_inteiros[0] == numeros_inteiros[1]:
            area_retang = round(numeros_inteiros[0] * numeros_inteiros[2], 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            area_ret = str(area_retang).replace('.',',') 
            numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[2]).replace('.',',')
            conteudo_1 = 'Tudo bem, vamos calcular a área deste retângulo.\n'
            conteudo_2 = f'A área do retângulo com dois lados iguais a {numeros_inteiros_local_0} \ne dois lados iguais a {numeros_inteiros_local_1} é {area_ret}\n'
            conteudo_3 = f'Se o que você quer é a área de um triângulo retângulo de catetos {numeros_inteiros_local_0} e {numeros_inteiros_local_1}, a área deste triângulo é {area_retang/2}.\nEspero ter respondido adequadamente 🙂'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        if numeros_inteiros[0] != numeros_inteiros[1]:
            area_retang = round(numeros_inteiros[0] * numeros_inteiros[1], 2)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            area_ret = str(area_retang).replace('.',',') 
            numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
            conteudo_1 = 'Tudo bem, vamos calcular a área deste retângulo.\n'
            conteudo_2 = f'A área do retângulo com dois lados iguais a {numeros_inteiros_local_0} \ne dois lados iguais a {numeros_inteiros_local_1} é {area_ret}\n'
            conteudo_3 = f'Se o que você quer é a área de um triângulo retângulo de catetos {numeros_inteiros_local_0} e {numeros_inteiros_local_1}, a área deste triângulo é {area_retang/2}.\nEspero ter respondido adequadamente 🙂'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
    else:
        if len(numeros_inteiros) != 2 and len(numeros_inteiros) != 4:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n por se tratar de um retângulo preciso da medidas do lado maior\n e do lado menor para fazer o cálculo da área.',resp,page)
