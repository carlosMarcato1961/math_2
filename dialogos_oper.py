import flet as ft  

def dialogo(page:ft.Page):
    #dialogo raiz
    def fechar_raiz(e):
        dlg_raiz.open = False
        page.update()
        #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_raiz = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5),)
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_raiz,expand=1.5)
    dlg_raiz = ft.AlertDialog(content= ft.Column(controls=[imagem_raiz,bot_fechar],width=600))
    def open_raiz(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_raiz)
        dlg_raiz.open = True
        page.update()

    #dialogo potencia
    def fechar_pot(e):
            dlg_pot.open = False
            page.update()
        #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_pot = ft.Image(src='texto_potencia.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_pot,expand=1.5)
    dlg_pot = ft.AlertDialog(content= ft.Column(controls=[imagem_pot,bot_fechar],width=600))
    def open_pot(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_pot)
        dlg_pot.open = True
        page.update()
    
    #dialogo fatorial
    def fechar_fat(e):
        dlg_fat.open = False
        page.update()
        #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_fat = ft.Image(src='texto_fatorial.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_fat,expand=1.5)
    dlg_fat = ft.AlertDialog(content= ft.Column(controls=[imagem_fat,bot_fechar],width=600))
    def open_fat(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_fat)
        dlg_fat.open = True
        page.update()

    #dialogo porcentagem
    def fechar_porc(e):
        dlg_porc.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_porc = ft.Image(src='texto_porcentagem.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_porc,expand=1.5)
    dlg_porc = ft.AlertDialog(content= ft.Column(controls=[imagem_porc,bot_fechar],width=600))
    def open_porc(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_porc)
        dlg_porc.open = True
        page.update()

    #dialogo expressão numérica
    def fechar_exp_num(e):
        dlg_exp_num.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_exp_num = ft.Image(src='texto_exp_num.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_exp_num,expand=1.5)
    dlg_exp_num = ft.AlertDialog(content= ft.Column(controls=[imagem_exp_num,bot_fechar],width=600))
    def open_exp_num(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_exp_num)
        dlg_exp_num.open = True
        page.update()

    #dialogo area quadrado
    def fechar_area_quad(e):
        dlg_area_quad.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_quad = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5),)
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_quad,expand=1.5)
    dlg_area_quad = ft.AlertDialog(content= ft.Column(controls=[imagem_area_quad,bot_fechar],width=600))
    def open_area_quad(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_quad)
        dlg_area_quad.open = True
        page.update()

    #dialogo area retangulo
    def fechar_area_ret(e):
        dlg_area_ret.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_ret = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_ret,expand=1.5)
    dlg_area_ret = ft.AlertDialog(content= ft.Column(controls=[imagem_area_ret,bot_fechar],width=600))
    def open_area_ret(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_ret)
        dlg_area_ret.open = True
        page.update()

    #dialogo area triangulo equilatero
    def fechar_area_tri_equi(e):
        dlg_area_tri_equi.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_tri_equi = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_tri_equi,expand=1.5)
    dlg_area_tri_equi = ft.AlertDialog(content= ft.Column(controls=[imagem_area_tri_equi,bot_fechar],width=600))
    def open_area_tri_equi(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_tri_equi)
        dlg_area_tri_equi.open = True
        page.update()

    #dialogo area triangulo isoceles
    def fechar_area_tri_isoceles(e):
        dlg_area_tri_isoceles.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_tri_isoceles = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_tri_isoceles,expand=1.5)
    dlg_area_tri_isoceles = ft.AlertDialog(content= ft.Column(controls=[imagem_area_tri_isoceles,bot_fechar],width=600))
    def open_area_trian_isoc(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_tri_isoceles)
        dlg_area_tri_isoceles.open = True
        page.update()

    #dialogo area triangulo escaleno
    def fechar_area_tri_escaleno(e):
        dlg_area_tri_escaleno.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_tri_escaleno = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_tri_escaleno,expand=1.5)
    dlg_area_tri_escaleno = ft.AlertDialog(content= ft.Column(controls=[imagem_area_tri_escaleno,bot_fechar],width=600))
    def open_area_trian_esc(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_tri_escaleno)
        dlg_area_tri_escaleno.open = True
        page.update()

    #dialogo area circulo
    def fechar_area_circ(e):
        dlg_area_circ.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_circ = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_circ,expand=1.5)
    dlg_area_circ = ft.AlertDialog(content= ft.Column(controls=[imagem_area_circ,bot_fechar],width=600))
    def open_area_circ(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_circ)
        dlg_area_circ.open = True
        page.update()

    #dialogo area figura geometrica
    def fechar_area_figura(e):
        dlg_area_figura.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_area_figura = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_area_figura,expand=1.5)
    dlg_area_figura = ft.AlertDialog(content= ft.Column(controls=[imagem_area_figura,bot_fechar],width=600))
    def open_fig_geo(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_area_figura)
        dlg_area_figura.open = True
        page.update()

    #dialogo seno
    def fechar_seno(e):
        dlg_seno.open = False   
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_seno = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_seno,expand=1.5)
    dlg_seno = ft.AlertDialog(content= ft.Column(controls=[imagem_seno,bot_fechar],width=600))
    def open_seno(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_seno)
        dlg_seno.open = True
        page.update()

    #dialogo cosseno
    def fechar_cosseno(e):
        dlg_cosseno.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_cosseno = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_cosseno,expand=1.5)
    dlg_cosseno = ft.AlertDialog(content= ft.Column(controls=[imagem_cosseno,bot_fechar],width=600))
    def open_cosseno(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_cosseno)
        dlg_cosseno.open = True
        page.update()

    #dialogo tangente
    def fechar_tangente(e):
        dlg_tangente.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_tangente = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_tangente,expand=1.5)
    dlg_tangente = ft.AlertDialog(content= ft.Column(controls=[imagem_tangente,bot_fechar],width=600))
    def open_tangente(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_tangente)
        dlg_tangente.open = True
        page.update()

    #dialogo calcular hipotenusa
    def fechar_hipotenusa(e):
        dlg_hipotenusa.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_hipotenusa = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_hipotenusa,expand=1.5)
    dlg_hipotenusa = ft.AlertDialog(content= ft.Column(controls=[imagem_hipotenusa,bot_fechar],width=600))
    def open_hipotenusa(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_hipotenusa)
        dlg_hipotenusa.open = True
        page.update()

    #dialogo calcular cateto
    def fechar_cateto(e):
        dlg_cateto.open = False 
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_cateto = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_cateto,expand=1.5)
    dlg_cateto = ft.AlertDialog(content= ft.Column(controls=[imagem_cateto,bot_fechar],width=600))
    def open_catetos(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_cateto)
        dlg_cateto.open = True
        page.update()

    #dialogo mediada circunferência
    def fechar_circunferencia(e):
        dlg_circunferencia.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_circunferencia = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_circunferencia,expand=1.5)
    dlg_circunferencia = ft.AlertDialog(content= ft.Column(controls=[imagem_circunferencia,bot_fechar],width=600))
    def open_medida_circunf(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_circunferencia)
        dlg_circunferencia.open = True
        page.update()

    #dialogo função grau 2
    def fechar_funcao_grau_2(e):
        dlg_funcao_grau_2.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_funcao_grau_2 = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_funcao_grau_2,expand=1.5)
    dlg_funcao_grau_2 = ft.AlertDialog(content= ft.Column(controls=[imagem_funcao_grau_2,bot_fechar],width=600))
    def open_funcao_2grau(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_funcao_grau_2)
        dlg_funcao_grau_2.open = True
        page.update()

    #dialogo volume esfera
    def fechar_volume_esfera(e):
        dlg_volume_esfera.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_volume_esfera = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_volume_esfera,expand=1.5)
    dlg_volume_esfera = ft.AlertDialog(content= ft.Column(controls=[imagem_volume_esfera,bot_fechar],width=600))
    def open_volume_esfera(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_volume_esfera)
        dlg_volume_esfera.open = True
        page.update()

    #dialogo volume cubo
    def fechar_volume_cubo(e):
        dlg_volume_cubo.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_volume_cubo = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_volume_cubo,expand=1.5)
    dlg_volume_cubo = ft.AlertDialog(content= ft.Column(controls=[imagem_volume_cubo,bot_fechar],width=600))
    def open_volume_cubo(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_volume_cubo)
        dlg_volume_cubo.open = True
        page.update()

    #dialogo volume paralelepipedo
    def fechar_volume_paralelepipedo(e):
        dlg_volume_paralelepipedo.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_volume_paralelepipedo = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_volume_paralelepipedo,expand=1.5)
    dlg_volume_paralelepipedo = ft.AlertDialog(content= ft.Column(controls=[imagem_volume_paralelepipedo,bot_fechar],width=600))
    def open_volume_paralelep(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_volume_paralelepipedo)
        dlg_volume_paralelepipedo.open = True
        page.update()

    #dialogo volume cone
    def fechar_volume_cone(e):
        dlg_volume_cone.open = False    
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_volume_cone = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_volume_cone,expand=1.5)
    dlg_volume_cone = ft.AlertDialog(content= ft.Column(controls=[imagem_volume_cone,bot_fechar],width=600))
    def open_volume_cone(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_volume_cone)
        dlg_volume_cone.open = True
        page.update()

    #dialogo volume piramide
    def fechar_volume_piramide(e):
        dlg_volume_piramide.open = False
        page.update()
         #scale=ft.Scale(scale=1.5) faz a imagem estourar os limites AlertDialog
        #expand dá um espaço para o objeto dentro do AlertDialog
    imagem_volume_piramide = ft.Image(src='texto_raiz_quadra.png',expand=7,scale=ft.Scale(scale=1.5))
    bot_fechar = ft.ElevatedButton(content=ft.Text(value='Fechar',size=14),color='red',on_click=fechar_volume_piramide,expand=1.5)
    dlg_volume_piramide = ft.AlertDialog(content= ft.Column(controls=[imagem_volume_piramide,bot_fechar],width=600))
    def open_volume_piramide(e):#função on click para abrir o dialogo
        page.overlay.append(dlg_volume_piramide)
        dlg_volume_piramide.open = True
        page.update()

    #definindo os botoes
    bot_raiz = ft.ElevatedButton(content=ft.Text(value='Raiz Quadrada',size=12),color='blue',on_click=open_raiz)
    bot_potencia = ft.ElevatedButton(content=ft.Text(value='Potenciação',size=12),color='blue',on_click=open_pot)
    bot_fatorial = ft.ElevatedButton(content=ft.Text(value='Fatorial',size=12),color='blue',on_click=open_fat)
    bot_porcentagem = ft.ElevatedButton(content=ft.Text(value='Porcentagem',size=12),color='blue',on_click=open_porc)
    bot_exp_num = ft.ElevatedButton(content=ft.Text(value='Expressão Numérica',size=12),color='blue',on_click=open_exp_num)
    bot_area_quad = ft.ElevatedButton(content=ft.Text(value='Área Quadrado',size=12),color='blue',on_click=open_area_quad)
    bot_area_ret = ft.ElevatedButton(content=ft.Text(value='Área Retângulo',size=12),color='blue',on_click=open_area_ret)
    bot_trian_equil = ft.ElevatedButton(content=ft.Text(value='Área Triângulo Equilátero',size=12),color='blue',on_click=open_area_tri_equi) 
    bot_trian_isoc = ft.ElevatedButton(content=ft.Text(value='Área Triângulo Isóceles',size=12),color='blue',on_click=open_area_trian_isoc)
    bot_trian_esc = ft.ElevatedButton(content=ft.Text(value='Área Triângulo Escaleno',size=12),color='blue',on_click=open_area_trian_esc)
    bot_area_circ = ft.ElevatedButton(content=ft.Text(value='Área Círculo',size=12),color='blue',on_click=open_area_circ)
    bot_fig_geo = ft.ElevatedButton(content=ft.Text(value='Figura Geométrica',size=12),color='blue',on_click=open_fig_geo)
    bot_seno = ft.ElevatedButton(content=ft.Text(value='Calcular Seno',size=12),color='blue',on_click=open_seno) 
    bot_cosseno = ft.ElevatedButton(content=ft.Text(value='Calcular Cosseno',size=12),color='blue',on_click=open_cosseno) 
    bot_tangente = ft.ElevatedButton(content=ft.Text(value='Calcular Tangente',size=12),color='blue',on_click=open_tangente)
    bot_calcular_hipotenusa = ft.ElevatedButton(content=ft.Text(value='Calcular Hipotenusa',size=12),color='blue',on_click=open_hipotenusa)
    bot_calcular_catetos = ft.ElevatedButton(content=ft.Text(value='Calcular Cateto',size=12),color='blue',on_click=open_catetos)
    bot_medida_circunf = ft.ElevatedButton(content=ft.Text(value='Medida de Circunferência',size=12),color='blue',on_click=open_medida_circunf)
    bot_funcao_2grau = ft.ElevatedButton(content=ft.Text(value='Função 2º Grau',size=12),color='blue',on_click=open_funcao_2grau)
    bot_volume_esfera = ft.ElevatedButton(content=ft.Text(value='Volume Esfera',size=12),color='blue',on_click=open_volume_esfera)
    bot_volume_cubo = ft.ElevatedButton(content=ft.Text(value='Volume Cubo',size=12),color='blue',on_click=open_volume_cubo) 
    bot_volume_paralelep = ft.ElevatedButton(content=ft.Text(value='Volume Paralelepipedo',size=12),color='blue',on_click=open_volume_paralelep) 
    bot_volume_cone = ft.ElevatedButton(content=ft.Text(value='Volume Cone',size=12),color='blue',on_click=open_volume_cone) 
    bot_volume_piramide = ft.ElevatedButton(content=ft.Text(value='Volume Pirâmide',size=12),color='blue',on_click=open_volume_piramide)

    abas_assuntos = ft.Tabs(
        indicator_color='white',
        label_color='white',
        unselected_label_color='#008000',
        height=450,
        # expand=True,
        tabs=[ft.Tab(
                        text='Áreas',
                        content=ft.Column(
                            controls=[
                                ft.GridView(
                                    controls=[bot_area_quad,bot_area_ret,bot_trian_equil,bot_trian_isoc,bot_trian_esc,bot_area_circ,bot_fig_geo,],
                                    expand=1, runs_count=3,
                                    #abaixo tamanho maximo do botão
                                    max_extent=170,
                                    #abaixo foi definido que a largura do botão é 4x maior que altura
                                    child_aspect_ratio=4,
                                    spacing=5,
                                    run_spacing=5,
                                    padding=10
                                )
                            ]
                        )
                    ),
                ft.Tab(
                        text='Volumes',
                        content=ft.Column(
                            controls=[
                                ft.GridView(
                                    controls=[bot_volume_esfera,bot_volume_cubo,bot_volume_paralelep,bot_volume_cone,bot_volume_piramide],
                                    expand=1, runs_count=3,
                                    #abaixo tamanho maximo do botão
                                    max_extent=170,
                                    #abaixo foi definido que a largura do botão é 3x maior que altura
                                    child_aspect_ratio=4,
                                    spacing=5,
                                    run_spacing=5,
                                    padding=10
                                )
                            ]
                        )
                    ),
                ft.Tab(
                        text='Cálculos',
                        content=ft.Column(
                            controls=[
                                ft.GridView(
                                    controls=[bot_raiz,bot_potencia,bot_fatorial,bot_porcentagem,bot_exp_num,
                                    bot_medida_circunf,bot_funcao_2grau],
                                    expand=1, runs_count=3,
                                    #abaixo tamanho maximo do botão
                                    max_extent=170,
                                    #abaixo foi definido que a largura do botão é 3x maior que altura
                                    child_aspect_ratio=4,
                                    spacing=5,
                                    run_spacing=5,
                                    padding=10
                                )
                            ]
                        )
                    )
               , ft.Tab(
                        text='Triângulo retângulo',
                        content=ft.Column(
                            controls=[
                                ft.GridView(
                                    controls=[bot_seno,bot_cosseno,bot_tangente,bot_calcular_hipotenusa,bot_calcular_catetos],
                                    expand=1, runs_count=3,
                                    #abaixo tamanho maximo do botão
                                    max_extent=170,
                                    #abaixo foi definido que a largura do botão é 3x maior que altura
                                    child_aspect_ratio=4,
                                    spacing=5,
                                    run_spacing=5,
                                    padding=10
                                )
                            ]
                        )
                    )
                
        ]

    )


    return abas_assuntos

    # page.add(
    #     #tornando a app responsiva para diversos tamanhos de tela
    #     ft.ResponsiveRow(controls=
            
    #         [
    #             grid_operacoes
                
    #         ]
    #     ),
    # )

#ft.app(target=dialogo) #, view=ft.WEB_BROWSER)

