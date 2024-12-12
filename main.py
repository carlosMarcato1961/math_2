import flet as ft
import re
import random
import raiz_quad,hipotenusa,catetos,potencia,fatorial,porcentagem
import expres_numericas,area_quad,area_tri_equil,area_tri_isoc
import area_tri_escaleno,area_circulo,seno,cosseno,volume_cone
import area_retang, tanGENTE, area_fig_geo, letra_por_letra,volume_piramide
from dialogos_oper import dialogo
import funcao_grau_2,medida_circunf,volume_esfera,volume_cubo,volume_paralelep
import funcao_grau_2
import corretor_palavras


def main(page: ft.Page):
    page.title = 'Math.PY'
    page.bgcolor= 'black'
    page.padding= 20
    page.scroll=ft.ScrollMode.AUTO
    # page.window_width = 450

    #FUNÇÃO QUE SEPARA DO TEXTO DIGITADO AS STRING, OS NUMEROS E OS OPERADORES
    def extrair_palavras_e_numeros(texto):
        # Expressão regular para encontrar palavras
        padrao_palavras = r'\b[\w\.]+\b' #todas as palavras sem '.'    r'\b\w+\b'
        palavras = re.findall(padrao_palavras, texto)
        
        # Expressão regular para encontrar números decimais
        #padrao_numeros =  r'\b\d+\.\d+\b|\b\d+\b' #padrão para encontrar numeros inteiros r'\b\d+\b'
        padrao_numeros = r'-?\d+\.?\d*'
        numeros = re.findall(padrao_numeros, texto)
        numeros_inteiros = [float(numero) for numero in numeros]
        
        #Padrão para encontrar operadores aritméticos
        padrao_operadores = r'[+\-*=/%!°]'
        operadores = re.findall(padrao_operadores, texto)
        
        return palavras, numeros_inteiros, operadores

    #DICIONARIO DE PALAVRAS CORRETAS PARA O SISTEMA em arquivo json
    # with open('src/dicionario.json', 'r') as arquivo:
    #     dicionario = json.load(arquivo)
    dicionario = ["raiz", "quadrada","expoente","elevado","fatorial","porcento","cento", "multiplica", "dividir",
                  "menos","area","circulo","raio","diametro","quadrado","triangulo","equilatero","isoceles",
                  "escaleno","figura","geometrica","retangulo","seno","cosseno","tangente","hipotenusa","cateto",
                  "circunferencia","volume","esfera","cubo","paralelepipedo","cone","piramide","lado","altura","obrigado",
                  "agradeço","obrigada"]


    #CONCATENA OS NUMEROS DIGITADOS NA FUNÇÃO DE SEGUNDO GRAU
    def concatena_grau2(e):
        #criar uma variavel que vai armazenar os numeros digitados
        num_digitados = resp_grau2.value
        #pegar os valores digitados e colocar na variavel vl_digitado
        vl_digitado = e.control.content.value
        #concatenar os valores
        resp_grau2.value = num_digitados + str(vl_digitado)
        page.update()
    #CALCULA AS FUNÇÕES E IMPRIME O RESULTADO
    def calcular(e):
        resp.value = '🎃'
        corrigir1 = pergunta.value
        #substitui virgula por ponto, para fazer calculos
        corrigir2 = corrigir1.replace(',' ,'.')
        #TRANSFORMA O TEXTO EM MINUSCULO
        corrigi3 = corrigir2.lower()
        #ABAIXO PEGA O TEXTO DIGITADO E COMPARA COM O DICIONARIO.JSON, CORRIGINDO PEQUENOS ERROS
        entrada = corretor_palavras.corretor_texto(corrigi3,dicionario,max_distancia=1)
        #ABAIXO PEGA-SE O TEXTO CORRIGUDO E NORMATIZADO, SEPARA EM PALAVRAS, NUMEROS E OPERADORES
        palavras, numeros_inteiros, operadores = extrair_palavras_e_numeros(entrada)
        erro = ''

        #IMPRESSÃO NO TERMINAL PARA AVALIAR A SAÍDA
        print('\npalavras',palavras,'\nnumeros_inteiros', numeros_inteiros,'     tamanho',len(numeros_inteiros), '\noperadores',
               operadores,'\npergunta:',pergunta.value,'\ncorrigir1',corrigir1,'\ncorrigir2',corrigir2,'\nentrada',entrada,)

        #RAIZ QUADRADA                
        if 'raiz' in palavras and 'quadrada'in palavras:
            raiz_quad.raiz_quadrada(numeros_inteiros, resp,erro,pergunta,page)
        elif 'raiz' in palavras:
            letra_por_letra.letra_por_letra_resp('Desculpe, se sua intenção for calcular uma raiz quadrada especifique na pergunta. Obrigado.',resp,page)
        #POTENCIA
        elif 'expoente' in palavras  or 'elevado' in palavras:
            potencia.potencia(numeros_inteiros, resp,erro,pergunta,page)  
        #FATORIAL
        elif '!' in operadores or 'fatorial' in palavras:
            fatorial.fatorial(numeros_inteiros, resp,erro,pergunta,page)
        #PORCENTAGEM
        elif '%' in operadores or 'porcento' in palavras or 'cento'in palavras:
            porcentagem.porcentagem(numeros_inteiros, resp,erro,pergunta,page)
        #EXPRESSÕES NUMERICAS
        elif 'x' in entrada or 'multiplicado' in entrada or 'multiplica' in entrada or 'vezes' in entrada or 'dividir' in palavras or 'dividido' in palavras or 'soma' in palavras or 'mais' in palavras or 'menos' in palavras or 'subtrai' in palavras or '-' in operadores or '+' in operadores or '*' in operadores or '/' in operadores:
            expres_numericas.expres_numericas(numeros_inteiros,operadores, resp,erro,entrada,pergunta,page)
        #AREAS
        elif 'area' in palavras:
            if 'quadrado' in palavras:
                area_quad.area_quad(numeros_inteiros, resp,erro,pergunta,page)
            elif 'triangulo' in palavras:
                if 'equilatero' in palavras:
                    area_tri_equil.area_tri_equil(numeros_inteiros, resp,erro,pergunta,page)
                elif 'isoceles' in palavras:
                    area_tri_isoc.area_tri_isoc(numeros_inteiros,palavras, resp,erro,pergunta,page)
                elif 'escaleno' in palavras:
                    area_tri_escaleno.area_tri_escaleno(numeros_inteiros, resp,erro,pergunta,page)
            elif 'circulo' in palavras:
                if 'raio' in palavras or 'rai' in palavras:
                    area_circulo.area_circulo_raio(numeros_inteiros, resp,erro,pergunta,page)
                elif 'diametro' in palavras:
                    area_circulo.area_circulo_diametro(numeros_inteiros, resp,erro,pergunta,page)
                else:
                    letra_por_letra.letra_por_letra_resp('Faltou o valor do raio ou do diâmetro',resp,page)
            elif 'figura' in palavras:
                if 'geometrica' in palavras:
                    area_fig_geo.area_fig_geo(numeros_inteiros, resp,erro,pergunta,page)
                else: 
                    letra_por_letra.letra_por_letra_resp('Acho que você quer saber a área de uma figura geométrica regular.\n',resp,page)
                    letra_por_letra.letra_por_letra_resp('Se for isso escreva "área de uma figura geométrica de (número) lados que medem (número) cada um"',resp,page)
            elif 'retangulo' in palavras:
                area_retang.area_retang(numeros_inteiros, resp,erro,pergunta,page) 
        #TRIANGULO RETANGULO
        #seno
        elif 'seno' in palavras:
            seno.seno(numeros_inteiros, resp,erro,pergunta,page)
        #coseno
        elif 'cosseno' in palavras:
            cosseno.cosseno(numeros_inteiros, resp,erro,pergunta,page)
        #tangente
        elif 'tangente' in palavras:
            tanGENTE.tangente(numeros_inteiros, resp,erro,palavras,pergunta,page)
    #CALCULAR A MEDIDA DE UM CATETO OU HIPOTENUSA
        #HIPOTENUSA
        elif 'hipotenusa' in palavras:
            if 'hipotenusa' in palavras and 'cateto' in palavras:
                catet = palavras.index('cateto')
                hipot = palavras.index('hipotenusa')
                if hipot < catet:
                    hipotenusa.calcular_hip(numeros_inteiros,resp,erro,pergunta,page)
                else:
                    catetos.calcular_cat_op(numeros_inteiros,resp,erro,pergunta,page)
            else:
                letra_por_letra.letra_por_letra_resp('Percebi que você está querendo calcular a hipotenusa ou cateto,\nporém falta informação na pergunta.',resp,page)
        #MEDIDA DA CIRCUNFERENCIA
        elif 'circunferencia' in palavras:
            medida_circunf.medida_circunf(numeros_inteiros, resp,palavras,page)
        #VOLUMES
        elif 'volume' in palavras:    
            if 'esfera' in palavras:
                volume_esfera.volume_esfera(numeros_inteiros, resp,palavras,page)
            elif 'cubo' in palavras:
                volume_cubo.volume_cubo(numeros_inteiros, resp,palavras,page)
            elif 'paralelepipedo' in palavras: 
                volume_paralelep.volume_paralelep(numeros_inteiros, resp,palavras,page)
            elif 'cone' in palavras:
                volume_cone.volume_cone(numeros_inteiros, resp,palavras,page)
            elif 'piramide' in palavras:
                volume_piramide.volume_piramide(numeros_inteiros, resp,palavras,page)
        #OBRIGADO
        elif 'obrigado' in palavras or 'agradeço' in palavras or 'obrigada' in palavras:
            letra_por_letra.letra_por_letra_resp('Fico feliz com sua satisfação.\nEspero ter ajudado na sua dúvida.\nObrigado por usar o Math.PY 🙂🙂🙂',resp,page)
        else:
            #ERRO POR DIGITAÇÃO ERRADA DAS PALAVRAS
            letra_por_letra.letra_por_letra_resp('Desculpe, não entendi a pergunta, por favor verifique a ortografia.\nProcure especificar o nome da figura geométrica e/ou operação desejada.',resp,page)
        page.update()    
        
#até aqui já mudei para letras por letras
#ATÉ AQUI AS PALAVRAS CHAVES FORAM CONFERIDAS

    #LIMPA A CAIXA DE PERGUNTA E RESPOSTA
    def apagar(e):
        pergunta.value = ''
        resp.value = '🎃'
        resp_grau2.value = 'Função:'
        page.update()
    
    def calcula_grau2(e):
        funcao_grau_2.calcula_grau2(resp_grau2,page,resp)
        #Frase escolhidas aleatorimente para mostrar na tela
        texto1 = '\n\nTem mais duvidas? Adoro resolver problemas de matemática 🙂'
        texto2 = '\n\nSe tiver mais perguntas sobre matemática fique a vontate para perguntar.🙂'
        texto3 = '\n\nEspero ter respondido adequadamente, fico feliz em resolver problemas matemáticos. 🙂'
        texto_aleatorio = random.choice([texto1, texto2, texto3])
        letra_por_letra.letra_por_letra_perg(texto_aleatorio,resp,page)
        page.update()

#ELEMENTOS DA PAGINA
    topo = ft.ResponsiveRow(controls=[ft.Text('Math.PY',size=50,color='blue',text_align='center',col={'xs':8,'sm':8,'md':4,'xl':4}),
                                    ft.Image(src='lanterna_jack.png',width=150,height=150,col={'xs':4,'sm':4,'md':2,'xl':2}),
                                    ft.Text('A sua plataforma inteligente de MATEMÁTICA\nDesenvolvida totalmente em Python',size=25,text_align='center',col={'sm':12,'md':6,'xl':6}),
                                    ],alignment=ft.alignment.center)
    pergunta = ft.TextField(label='Digite sua pergunta',border_color='blue',multiline=True)
    enter = ft.ElevatedButton(text='Responder', on_click=calcular, bgcolor='green', color='black')
    limpa = ft.OutlinedButton(text='Limpar', on_click=apagar)
    resp = ft.TextField(label='Sua resposta aparece aqui.',value='🎃',multiline=True,
                        border_color='blue',text_size=18,read_only=True)
    texto_col_2 = ft.Text('  Click e veja abaixo o que temos sobre Matemática', size=16, color='blue',text_align='center')
    texto_atual = ft.Text('NOSSO SITE ESTÁ EM CONSTANTE DESENVOLVIMENTO, SEMPRE SERÁ OFERTADO NOVOS RECURSOS',
                           size=14, color='#008000',text_align='center',)
    imagem_raiz = ft.Container()


    # BOTÕES DE CALCULO DE FUNÇÃO DE 2º GRAU
    bot_0 = ft.Container(content=ft.Text(value='0',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_1 = ft.Container(content=ft.Text(value='1',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_2 = ft.Container(content=ft.Text(value='2',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_3 = ft.Container(content=ft.Text(value='3',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_4 = ft.Container(content=ft.Text(value='4',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_5 = ft.Container(content=ft.Text(value='5',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_6 = ft.Container(content=ft.Text(value='6',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_7 = ft.Container(content=ft.Text(value='7',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_8 = ft.Container(content=ft.Text(value='8',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_9 = ft.Container(content=ft.Text(value='9',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_x = ft.Container(content=ft.Text(value=' x',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_x2 = ft.Container(content=ft.Text(value=' x²',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_soma = ft.Container(content=ft.Text(value='+',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_sub = ft.Container(content=ft.Text(value='-',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    bot_igual = ft.Container(content=ft.Text(value='= 0',color='white',size=25),bgcolor='blue',on_click=concatena_grau2,
                        height=40,width=60,alignment=ft.alignment.center,border_radius=10,border=ft.border.all(1,'white'))
    janela_grau2 = ft.Container(content=ft.Text(value='Use as teclas ao lado para digitar a equação de segundo grau e clique no botão abaixo para calcular as raizes.',
                                size=14,color='blue',text_align='center'),alignment=ft.alignment.center)
    titulo_grau2 = ft.Text(value='CÁLCULO DE FUNÇÕES DE 2º GRAU',size=20,color='blue')
    resp_grau2 = ft.TextField(label='Função de 2º grau.',value='Função:',multiline=True,read_only=True,border_color='blue',text_size=18)
    bot_raizes = ft.Container(content=ft.ElevatedButton(text='Raizes',bgcolor='blue',color='white',on_click=calcula_grau2), alignment=ft.alignment.center)

    #ORGANIZA NA TELA OS BOTÕES DO CALCULO DE FUNÇÃO DE 2º GRAU
    botoes_grau2 = ft.ResponsiveRow(controls=[ft.Column([bot_0,bot_1,bot_2], col='1.5'),ft.Column([bot_3,bot_4,bot_5],
                                    col='1.5'),ft.Column([bot_6,bot_7,bot_8],col='1.5'),ft.Column([bot_9,bot_soma,bot_sub],
                                    col='1.5'),ft.Column([bot_x,bot_x2,bot_igual],col='1.5'), ft.Column([janela_grau2,bot_raizes],col='4.5')])
    
    #TELA DOS DIALOGOS
    dialogos = dialogo(page)


    #COLUNAS
    #criando as colunas de que contem os objetos da app
    # coluna_logo = ft.Column([logo],col={'sm':12,'md':6,'xl':4})
    coluna_topo = ft.Column(controls=[topo],col={'sm':12,'md':12,'xl':12})
    coluna_1 = ft.Column([pergunta,ft.Row([enter,limpa]),resp,titulo_grau2,resp_grau2,botoes_grau2],
                        col={'sm':12,'md':6,'xl':6})
    coluna_2 = ft.Column([texto_col_2,dialogos,imagem_raiz],col={'sm':12,'md':6,'xl':6})

    page.add(
        #tornando a app responsiva para diversos tamanhos de tela
        ft.ResponsiveRow(
            [
                ft.ResponsiveRow(controls=[coluna_topo],col={'sm':12,'md':12,'xl':12}),
                ft.ResponsiveRow(controls=[coluna_1,coluna_2],col={'sm':12,'md':12,'xl':12}),
                ft.ResponsiveRow(controls=[texto_atual],col={'sm':12,'md':12,'xl':12}),
                # coluna_topo,coluna_1,coluna_2
                
            ]
        ),
        )
    
   
#commando roda o app e abre no  navegador
ft.app(target=main, assets_dir='assets')#, view=ft.WEB_BROWSER)
