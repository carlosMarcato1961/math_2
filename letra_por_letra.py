import time

#IMPRIMI LETRA POR LETRA NO CAMPO RESPOSTA
def letra_por_letra_resp(texto,resp,page):
        # resp.value = ''
        for letra in texto:
            page.update()
            time.sleep(0.03)
            resp.value += letra
#IMPRIMI LETRA POR LETRA NO CAMPO PERGUNTA
def letra_por_letra_perg(texto,pergunta,page):
        # pergunta.value = ''
        for letra in texto:
            page.update()
            time.sleep(0.03)
            pergunta.value += letra

