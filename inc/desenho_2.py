# =============================================================================
#
#                             COGERAÇÃO v1.0
#
#
#                              Rafael Vidal   
#                       (rafael.vidal@poli.ufrj.br)
#
#
# =============================================================================


from inc.desenho_geral import *

def desenho_2 (canvas):
    
    x0 = 10
    y0 = 20
    
    escala = 50
    caldeira_x = x0 + 0
    caldeira_y = y0 + 90
    turbina1_x = x0 + 226
    turbina1_y = y0 + 90
    turbina2_x = x0 + 400
    turbina2_y = y0 + 90
    bomba1_x = x0 + 400
    bomba1_y = y0 + 415
    bomba2_x = x0 + 100
    bomba2_y = bomba1_y
    condensador_y = y0 + 265
    desaerador_x = (bomba1_x + bomba2_x - 3.5*escala)/2
    desaerador_y = bomba1_y - 0.35*escala
    dessuperaquecedor_x = desaerador_x + 2.7*0.3*escala
    dessuperaquecedor_y = desaerador_y - 3*escala
    processo_x = desaerador_x + 2.7*0.8*escala
    processo_y = desaerador_y - 1.2*escala
    
    linha1_2 = canvas.create_line([turbina2_x+escala/10, caldeira_y - escala, turbina2_x+escala/10, turbina2_y - 0.05*escala], fill = 'red', width = 2, arrow = 'last')
    linha2_2 = canvas.create_line([turbina1_x+9*escala/10, turbina1_y + 2*escala, turbina1_x+2*escala, turbina1_y + 2*escala], fill = 'red', width = 2)
    linha2_3 = canvas.create_line([turbina1_x+2*escala, turbina1_y + 2*escala, turbina1_x+2*escala, caldeira_y - escala], fill = 'red', width = 2)
    linha2_4 = canvas.create_line([turbina1_x+2*escala, caldeira_y - escala, turbina2_x+escala/10, caldeira_y - escala], fill = 'red', width = 2)
    linha0_1 = canvas.create_line([caldeira_x + escala, caldeira_y, caldeira_x + escala, caldeira_y - escala], fill = 'red', width = 2)
    linha0_2 = canvas.create_line([caldeira_x + escala, caldeira_y - escala, turbina1_x+escala/10, caldeira_y - escala], fill = 'red', width = 2)
    linha0_3 = canvas.create_line([turbina1_x+escala/10, caldeira_y - escala, turbina1_x+escala/10, turbina1_y-0.05*escala], fill = 'red', width = 2, arrow = 'last')
    linha3   = canvas.create_line([turbina2_x+9*escala/10, turbina2_y, turbina2_x+9*escala/10, condensador_y - 0.6*escala], fill = 'red', width = 2, arrow = 'last')
    linha4_1 = canvas.create_line([turbina2_x+9*escala/10, condensador_y, turbina2_x+9*escala/10, bomba1_y], fill = 'blue', width = 2)
    linha4_2 = canvas.create_line([turbina2_x+9*escala/10, bomba1_y, bomba1_x+0.5*escala, bomba1_y], fill = 'blue', width = 2, arrow = 'last')
    linha5_1 = canvas.create_line([caldeira_x + escala, bomba2_y, caldeira_x + escala, caldeira_y+2*escala], fill = 'blue', width = 2, arrow = 'last')
    linha5_2 = canvas.create_line([bomba2_x, bomba2_y, caldeira_x + escala, bomba2_y], fill = 'blue', width = 2)
    linha6_1 = canvas.create_line([bomba1_x, bomba1_y, desaerador_x + 2.6*escala, bomba2_y], fill = 'blue', width = 2, arrow = 'last')
    linha6_2 = canvas.create_line([desaerador_x, bomba1_y, bomba2_x+0.5*escala, bomba2_y], fill = 'blue', width = 2, arrow = 'last')
    linha7_1 = canvas.create_line([turbina1_x+9*escala/10, turbina1_y+escala, turbina1_x+9*escala/10, turbina1_y + 2.5*escala], fill = 'red', width = 2)
    linha7_2 = canvas.create_line([turbina1_x+9*escala/10, turbina1_y + 2.5*escala, desaerador_x + 1.8*0.2*escala, turbina1_y + 2.5*escala], fill = 'red', width = 2)
    linha7_3 = canvas.create_line([processo_x, turbina1_y + 2.5*escala, processo_x, dessuperaquecedor_y], fill = 'red', width = 2, arrow = 'last')
    linha7_4 = canvas.create_line([desaerador_x + 1.8*0.2*escala, turbina1_y + 2.5*escala, desaerador_x + 1.8*0.2*escala, desaerador_y], fill = 'red', width = 2, arrow = 'last')
    linha8_1 = canvas.create_line([processo_x, dessuperaquecedor_y, processo_x, processo_y-0.35*escala], fill = 'red', width = 2, arrow = 'last')
    linha8_2 = canvas.create_line([processo_x, processo_y-0.35*escala, processo_x, desaerador_y], fill = 'blue', width = 2, arrow = 'last')
    linha9_1 = canvas.create_line([dessuperaquecedor_x + 3*escala, bomba2_y, dessuperaquecedor_x + 3*escala, dessuperaquecedor_y+0.35*escala], fill = 'blue', width = 2)
    linha9_2 = canvas.create_line([dessuperaquecedor_x + 3*escala, dessuperaquecedor_y+0.35*escala, dessuperaquecedor_x + 2.6*escala, dessuperaquecedor_y+0.35*escala], fill = 'blue', width = 2, arrow = 'last')
    
    desenhar_circulo(turbina2_x+9*escala/10, condensador_y, 'Condensador', escala, canvas)
    desenhar_caldeira(caldeira_x,caldeira_y,escala,canvas)
    desenhar_turbina(turbina1_x, turbina1_y, 1, escala, canvas)
    desenhar_turbina(turbina2_x, turbina2_y, 2, escala, canvas)
    desenhar_bomba(bomba1_x, bomba1_y, 1, escala, canvas)
    desenhar_bomba(bomba2_x, bomba2_y, 2, escala, canvas)
    desenhar_caixa(dessuperaquecedor_x, dessuperaquecedor_y, 'Dessuperaquecedor', escala, canvas)
    desenhar_caixa(desaerador_x, desaerador_y, 'Desaerador', escala, canvas)
    desenhar_oval(processo_x, processo_y, 'Processo', escala, canvas)
    
    desenhar_ponto(caldeira_x + escala, caldeira_y - 0.5*escala, canvas, 1, 'E', 'red')
    desenhar_ponto(turbina1_x-escala/10, caldeira_y - escala, canvas, 2, 'N', 'red')
    desenhar_ponto(turbina1_x+escala/10, (caldeira_y - escala + turbina1_y-0.05*escala)/2, canvas, 3, 'E', 'red')
    desenhar_ponto(turbina1_x+9*escala/10, turbina1_y+1.75*escala, canvas, 4, 'E', 'red')
    desenhar_ponto(turbina2_x+escala/10, turbina2_y - 0.5*escala, canvas, 5, 'W', 'red')
    desenhar_ponto(turbina2_x+9*escala/10, turbina2_y+2.25*escala, canvas, 6, 'E', 'red')
    desenhar_ponto(turbina2_x+9*escala/10, condensador_y + 1.8*escala, canvas, 7, 'E', 'blue')
    desenhar_ponto(bomba1_x - 0.75*escala, bomba2_y, canvas, 8, 'N', 'blue')
    desenhar_ponto(dessuperaquecedor_x + 3*escala, 0.5*(bomba2_y+dessuperaquecedor_y+0.35*escala), canvas, 9, 'E', 'blue')
    desenhar_ponto(bomba1_x - 1.5*escala, bomba2_y, canvas, 10, 'N', 'blue')
    desenhar_ponto(turbina1_x+9*escala/10, turbina1_y+2.25*escala, canvas, 11, 'E', 'red')
    desenhar_ponto(processo_x, dessuperaquecedor_y - 4*escala/10, canvas, 12, 'E', 'red')
    desenhar_ponto(desaerador_x + 1.8*0.2*escala, dessuperaquecedor_y + escala, canvas, 13, 'E', 'red')
    desenhar_ponto(processo_x, dessuperaquecedor_y + escala, canvas, 14, 'E', 'red')
    desenhar_ponto(processo_x, dessuperaquecedor_y + 2.5*escala, canvas, 15, 'E', 'blue')
    desenhar_ponto(bomba2_x + 0.9*escala, bomba2_y, canvas, 16, 'N', 'blue')
    desenhar_ponto(caldeira_x + escala, caldeira_y + 4*escala, canvas, 17, 'E', 'blue')