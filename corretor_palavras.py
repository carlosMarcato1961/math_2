import flet as ft
import nltk
from nltk.metrics import edit_distance
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def corretor_texto(texto, dicionario, max_distancia=1):
    #stopwords serve para remover palavras desnecessarias ao entendimento da aplicação com artidgos e proposições
    stop_words = set(stopwords.words('portuguese'))
    palavras = [palavra for palavra in word_tokenize(texto)]# if palavra not in stop_words]
    palavras_corrigidas = []
    #abaixo é feita a comparação das palavras digitadas com as palavras do dicionario
    #max_distancia serve para limitar a distância de Levenshtein, neste caso foi colocado 1 para corrigir pequenos erros
    for palavra in palavras:
        menor_distancia = float('inf')
        palavra_correta = palavra
        #procura por palavras semelhantes no dicionario
        for palavra_dic in dicionario:
            distancia = edit_distance(palavra, palavra_dic)
            if distancia <= max_distancia and distancia < menor_distancia:
                menor_distancia = distancia
                palavra_correta = palavra_dic
        #depois de encontrar a palavra correta, ela substitui a palavra digitada pelo dicionario
        palavras_corrigidas.append(palavra_correta)

    # return str(palavras_corrigidas)
    #.join pega lista palavras_corrigidas e as junta em uma string separada por espaço
    return  ' '.join(palavras_corrigidas)
