from math import sqrt
import letra_por_letra
import random

def area_tri_escaleno(numeros_inteiros,resp,erro,pergunta,page):
    if len(numeros_inteiros)  == 3:
        semi_perimetro = (numeros_inteiros[0] + numeros_inteiros[1] + numeros_inteiros[2]) / 2
        parte_a = semi_perimetro - numeros_inteiros[0]
        parte_b = semi_perimetro - numeros_inteiros[1]
        parte_c = semi_perimetro - numeros_inteiros[2]
        if parte_a>0 and parte_b>0 and parte_c>0:
            resultado = round(sqrt(semi_perimetro * parte_a * parte_b * parte_c), 2) 
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            resultado_str = str(resultado).replace('.',',') 
            numeros_inteiros_local_0 = str(numeros_inteiros[0]).replace('.',',')
            numeros_inteiros_local_1 = str(numeros_inteiros[1]).replace('.',',')
            numeros_inteiros_local_2 = str(numeros_inteiros[2]).replace('.',',')
            conteudo_1 = 'Ok, vamos calcular a área de um triangulo escaleno de lados\n'
            conteudo_2 = f'a = {numeros_inteiros_local_0}, b = {numeros_inteiros_local_1} e c = {numeros_inteiros_local_2}.\n'
            conteudo_5 = f'A área de um  triângulo de lados {numeros_inteiros_local_0}/{numeros_inteiros_local_1}/{numeros_inteiros_local_2} é de {resultado_str} .'
            resposta = f'{conteudo_1}{conteudo_2}{conteudo_5}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            letra_por_letra.letra_por_letra_resp('Erro, o valor do lado maior é maior ou igual a soma dos\n outros dois lados. Portanto não se trata de um triângulo.\nPor favor verifique se não houve erro de digitação.',resp,page)
    else:
        if len(numeros_inteiros) < 3:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado os valores de menos de 3 lados.\nPreciso da medida dos 3 lados para calcular a área de um\ntriangulo escaleno.',resp,page)
        if len(numeros_inteiros) > 3:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, foi digitado valores a mais.\nPreciso da medida dos 3 lados para calcular a área de um\ntriangulo escaleno.',resp,page)

    return area_tri_escaleno
