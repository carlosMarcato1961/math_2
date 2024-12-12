import letra_por_letra
import random

def volume_cone(numeros_inteiros,resp,palavra,page):
    if len(numeros_inteiros) == 2:
        if 'raio' in palavra and 'altura' in palavra:
            indice_raio = palavra.index('raio')
            indice_altura = palavra.index('altura')
            if indice_altura > indice_raio:
                volume_cone = round((3.1416 * numeros_inteiros[0] ** 2 * numeros_inteiros[1])/3, 3)
                #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
                volume_con = str(volume_cone).replace('.',',') 
                numeros_inteiros_local_raio = str(numeros_inteiros[0]).replace('.',',')
                numeros_inteiros_local_altura = str(numeros_inteiros[1]).replace('.',',')
                conteudo_1 = 'Boa pergunta, vamos calcular o volume da cone.\n'
                conteudo_2 = 'Para isso usamos a fórmula V = (PI x r² x h)/3.\n'
                conteudo_3 = 'Se o problema apresentar o valor do diâmetro então\n'
                conteudo_4 = 'devemos usar a fórmula V = (PI x (d/2)² x h)/3. Dito isto\n'
                conteudo_5 = f'o volume do cone com raio da base {numeros_inteiros_local_raio} e altura {numeros_inteiros_local_altura} é {volume_con}'
                resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
                letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                #Frase escolhidas aleatorimente para mostrar na tela
                texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                texto_aleatorio = random.choice([texto1, texto2, texto3])
                letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
            if indice_raio > indice_altura:
                volume_cone = round((3.1416 * numeros_inteiros[1] ** 2 * numeros_inteiros[0])/3, 3)
                #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
                volume_con = str(volume_cone).replace('.',',') 
                numeros_inteiros_local_raio = str(numeros_inteiros[1]).replace('.',',')
                numeros_inteiros_local_altura = str(numeros_inteiros[0]).replace('.',',')
                conteudo_1 = 'Boa pergunta, vamos calcular o volume da cone.\n'
                conteudo_2 = 'Para isso usamos a fórmula V = (PI x r² x h)/3.\n'
                conteudo_3 = 'Se o problema apresentar o valor do diâmetro então\n'
                conteudo_4 = 'devemos usar a fórmula V = (PI x (d/2)² x h)/3. Dito isto\n'
                conteudo_5 = f'o volume do cone com raio da base {numeros_inteiros_local_raio} e altura {numeros_inteiros_local_altura} é {volume_con}'
                resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
                letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                #Frase escolhidas aleatorimente para mostrar na tela
                texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                texto_aleatorio = random.choice([texto1, texto2, texto3])
                letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        elif 'diametro' in palavra and 'altura' in palavra:
            indice_diametro = palavra.index('diametro')
            indice_altura = palavra.index('altura')
            if indice_altura > indice_diametro:
                volume_cone = round((3.1416 * (numeros_inteiros[0]/2) ** 2 * numeros_inteiros[1])/3, 3)
                #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
                volume_con = str(volume_cone).replace('.',',') 
                numeros_inteiros_local_raio = str(numeros_inteiros[0]).replace('.',',')
                numeros_inteiros_local_altura = str(numeros_inteiros[1]).replace('.',',')
                conteudo_1 = 'Boa pergunta, vamos calcular o volume da cone.\n'
                conteudo_2 = 'Para isso usamos a fórmula V = (PI x r² x h)/3.\n'
                conteudo_3 = 'Se o problema apresentar o valor do diâmetro então\n'
                conteudo_4 = 'devemos usar a fórmula V = (PI x (d/2)² x h)/3. Dito isto\n'
                conteudo_5 = f'o volume do cone com diâmetro da base {numeros_inteiros_local_raio} e altura {numeros_inteiros_local_altura} é {volume_con}'
                resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
                letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                #Frase escolhidas aleatorimente para mostrar na tela
                texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                texto_aleatorio = random.choice([texto1, texto2, texto3])
                letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
            if indice_diametro > indice_altura:
                volume_cone = round((3.1416 * (numeros_inteiros[1]/2) ** 2 * numeros_inteiros[0])/3, 3)
                #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
                volume_con = str(volume_cone).replace('.',',') 
                numeros_inteiros_local_raio = str(numeros_inteiros[1]).replace('.',',')
                numeros_inteiros_local_altura = str(numeros_inteiros[0]).replace('.',',')
                conteudo_1 = 'Boa pergunta, vamos calcular o volume da cone.\n'
                conteudo_2 = 'Para isso usamos a fórmula V = (PI x r² x h)/3.\n'
                conteudo_3 = 'Se o problema apresentar o valor do diâmetro então\n'
                conteudo_4 = 'devemos usar a fórmula V = (PI x (d/2)² x h)/3. Dito isto\n'
                conteudo_5 = f'o volume do cone com diâmetro da base {numeros_inteiros_local_raio} e altura {numeros_inteiros_local_altura} é {volume_con}'
                resposta = f'{conteudo_1}{conteudo_2}{conteudo_3}{conteudo_4}{conteudo_5}'
                letra_por_letra.letra_por_letra_resp(resposta,resp,page)
                #Frase escolhidas aleatorimente para mostrar na tela
                texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
                texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
                texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
                texto_aleatorio = random.choice([texto1, texto2, texto3])
                letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            if 'raio' not in palavra and 'diametro' not in palavra:
                letra_por_letra.letra_por_letra_resp('Erro de digitação, você na especificou o valor do raio ou diâmetro da base do cone.',resp,page)
                letra_por_letra.letra_por_letra_resp('Para calcular o volume de um cone\nbasta digitar o valor do raio ou diâmetro da base\ne a altura do cone. Por favor tente novamente.',resp,page)
            if 'altura' not in palavra:
                letra_por_letra.letra_por_letra_resp('Erro de digitação, você na especificou o valor da altura do cone.',resp,page)
                letra_por_letra.letra_por_letra_resp('Para calcular o volume de um cone\nbasta digitar o valor do raio ou diâmetro da base\ne a altura do cone. Por favor tente novamente.',resp,page)

    elif len(numeros_inteiros) < 2:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, não há informações numéricas suficientes,\npor favor digite o valor do raio ou do diâmetro da base e a\naltura do cone para eu calcular o volume do cone, tente novamente.',resp,page)
    elif len(numeros_inteiros) > 2:
        letra_por_letra.letra_por_letra_resp('Erro de digitação, há informações numéricas demasiada,\npor favor digite o valor do raio ou do diâmetro da base e a\naltura do cone para eu calcular o volume do cone, tente novamente.',resp,page)
