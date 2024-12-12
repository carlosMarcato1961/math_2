import re
import letra_por_letra
import random

def expres_numericas(numeros_inteiros, operadores, resp,erro,entrada,pergunta,page):
    #essa variavel não é usada, serve para testar se foi digitado dois numeros pelo menos
        # substituir palavras chaves por '*'
        result = entrada.replace('x','*').replace('vezes','*').replace('multiplicado','*').replace('multiplica','*').replace('dividir','/').replace('dividido', '/').replace('soma', '+').replace('mais', '+').replace('menos','-').replace('subtrai','-')
        #limpa todo o texto deixando apenas numeros e operadores
        expressao_limpa = re.sub(r'[^\d\s+\-*/().]', '', result)
        # Expressão regular para encontrar números decimais
        #padrao_numeros =  r'\b\d+\.\d+\b|\b\d+\b' #padrão para encontrar numeros inteiros r'\b\d+\b'
        padrao_numeros = r'-?\d+\.?\d*'
        numeros = re.findall(padrao_numeros, expressao_limpa)
        numeros_inteiros = [float(numero) for numero in numeros]
        #Padrão para encontrar operadores aritméticos
        padrao_operadores = r'[+\-*=/%!]'
        operadores = re.findall(padrao_operadores, expressao_limpa)
        #realiza a operação
        print(expressao_limpa,numeros_inteiros,operadores)
        if len(numeros_inteiros) > len(operadores):
            res = round(eval(expressao_limpa), 3)
            #trata a saída float para string substituindo o '.' pela ',' usado no Brasil
            resultado = str(res).replace('.',',')
            conteudo_1 = 'Certo, resolvendo esta expressão numérica.\n'
            conteudo_2 = f'O resultado da expressão numérica é {resultado}.'
            resposta = f'{conteudo_1}{conteudo_2}'
            letra_por_letra.letra_por_letra_resp(resposta,resp,page)
            #Frase escolhidas aleatorimente para mostrar na tela
            texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
            texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
            texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas. 🙂'
            texto_aleatorio = random.choice([texto1, texto2, texto3])
            letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        else:
            letra_por_letra.letra_por_letra_resp('Erro de digitação, provavelmente é um problema numérico,\n tem que haver 1 número a mais que a quantidade de operadores.\nExemplo: 4+2-2',resp,page)
