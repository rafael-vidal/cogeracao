# =============================================================================
#
#                             COGERAÇÃO v1.0
#
#
#                              Rafael Vidal   
#                       (rafael.vidal@poli.ufrj.br)
#
#
#                                                                    27/02/2020
# =============================================================================

def desenhar_bomba(x, y, n, escala, canvas): #center coordinates, radius
    r = escala/2
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    x2 = x - 0.6*r
    y2 = y + 0.8*r
    x3 = x - 1.1*r
    y3 = y + 1.4*r
    x4 = x + 1.1*r
    y4 = y + 1.4*r
    x5 = x + 0.6*r
    y5 = y + 0.8*r

    canvas.create_polygon([x2,y2,x3,y3,x4,y4,x5,y5],outline='black', fill='gray', width=2)
    canvas.create_oval(x0, y0, x1, y1, outline = 'black', fill = 'gray', width=2)
    canvas.create_text(x, y, text = 'B{}'.format(n), fill = 'white', anchor = 'center', font = 'Arial {} bold'.format(int(escala/5)))

def desenhar_turbina(x1, y1, n, escala, canvas): #center coordinates, radius  
    x2 = x1
    y2 = y1 + escala
    x3 = x1 + escala
    y3 = y1 + 1.5*escala
    x4 = x3
    y4 = y1 - 0.5*escala
    canvas.create_polygon([x1,y1,x2,y2,x3,y3,x4,y4],outline='black', fill='gray', width=2)
    canvas.create_text(x1 + escala/2, y1 + escala/2, text = 'T{}'.format(n), fill = 'white', anchor = 'center', font = 'Arial {} bold'.format(int(escala/5)))
    
def desenhar_caixa(x1, y1, texto, escala, canvas, color = 'gray'): #center coordinates, radius  
    x2 = x1
    y2 = y1 + escala*0.7
    x3 = x1 + 2.6*escala
    y3 = y2
    x4 = x3
    y4 = y1
    canvas.create_polygon([x1,y1,x2,y2,x3,y3,x4,y4],outline='black', fill='gray', width=2)
    canvas.create_text((x1+x3)/2, (y1+y2)/2, text = texto, fill = 'white', anchor = 'center', font = 'Arial {} bold'.format(int(escala/5)))
    
def desenhar_circulo(x, y, texto, escala, canvas, color='blue'): #center coordinates, radius
    r = 0.6*escala
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r

    canvas.create_oval(x0, y0, x1, y1, outline = 'black', fill = color, width=2)
    canvas.create_text(x, y, text = texto, fill = 'white', anchor = 'center', font = 'Arial {} bold'.format(int(1.2*len(texto)/2)))
    
def desenhar_caldeira(x1, y1, escala, canvas):
    escala = 2*escala
    canvas.create_polygon([x1, y1, x1 + escala, y1, x1 + escala, y1 + escala, x1, y1 + escala], outline = 'black', fill = 'red', width = 2)
    canvas.create_oval(x1+7*escala/8, y1+7*escala/8, x1+escala/8, y1+escala/8, width=2)
    desenhar_circulo(x1+escala/4, y1+escala/4, '', escala/6, canvas, color='red')
    desenhar_circulo(x1+3*escala/4, y1+3*escala/4, '', escala/6, canvas, color='red')
    
def desenhar_oval(x, y, texto, escala, canvas, color='orange'):
    a = escala/1.4
    b = escala/2.8
    x0 = x - a
    y0 = y - b
    x1 = x + a
    y1 = y + b
 
    canvas.create_oval(x0, y0, x1, y1, outline = 'black', fill = color, width=2)
    canvas.create_text(x, y, text = texto, fill = 'white', anchor = 'center', font = 'Arial {} bold'.format(int(escala/5)))
    
def desenhar_ponto(x, y, canvas, numero, posicao, cor):
    r=3
    canvas.create_oval(x-r, y-r, x+r, y+r, fill = cor)
    
    if posicao == 'N':
        canvas.create_text(x, y-10, text = str(numero), fill = 'black', anchor = 'center', font = 'Arial 10')
    elif posicao == 'E':
        canvas.create_text(x+5, y, text = str(numero), fill = 'black', anchor = 'w', font = 'Arial 10')
    elif posicao == 'W':
        canvas.create_text(x-5, y, text = str(numero), fill = 'black', anchor = 'e', font = 'Arial 10')