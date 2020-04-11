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


from tkinter import *
from tkinter import ttk
import os
from inc.ciclo import ciclo
from inc.grafico import grafico
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from inc.desenho_1 import desenho_1
from inc.desenho_2 import desenho_2
import ctypes
from inc.errors import Error

  
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.notebook = ttk.Notebook(width = 900, height = 662)
        self.add_tabs()
        self.notebook.grid(row=0)

 #       whnd = ctypes.windll.kernel32.GetConsoleWindow()
 #       if whnd != 0:
 #           ctypes.windll.user32.ShowWindow(whnd, 0)
        
    def add_tabs(self):
        self.tab1 = TabOne(self)
        self.tab2 = TabTwo(self)
        self.tab3 = TabThree(self)
        self.tab4 = TabFour(self)
        self.notebook.add(self.tab1,text="Simulação ")
        self.notebook.add(self.tab2,text="Resultados")
        self.notebook.add(self.tab3,text="Gráficos  ")
        self.notebook.add(self.tab4,text="Sobre     ")
        
    def calculate_cycle(self):
        params = self.tab1.get_params()

        if '' in params:
            raise(Error("Todos os parâmetros de entrada devem ser preenchidos."))

        try:
            params = list(map(lambda x: float(x), params))
        except:
            raise(Error("Os parâmetros de entrada devem ser numéricos."))

        results, df = ciclo(params)
        self.tab2.set_results(results, df)
        
    def calculate_graphic(self):
        params = self.tab1.get_params()
        params = list(map(lambda x: float(x), params))
        graphic_params = self.tab3.get_graphic_params()
        
        x_graphic, y_graphic = grafico(params, graphic_params)
        self.tab3.set_graphic(x_graphic, y_graphic)
        
  
class TabOne(Frame):
    def __init__(self,parent):
        Frame.__init__(self)
        self.parent = parent
        
        padx_ = 1
        pady_ = 2
        
        #############################
        ########## FRAME 0 ##########
        #############################
        
        self.frame0 = LabelFrame(self, text = 'Processo')
        self.frame0.grid(row = 1, column = 0, pady = 3, padx = 15)
        
        
        ########## ESPAÇO P1 ##########
        self.labelp1 = ttk.Label(self.frame0, text = 'Taxa de moagem [t cana / h]:                     ')
        self.labelp1.grid(row = 1, column = 0, sticky = W)
        
        self.entryp1 = ttk.Entry(self.frame0, width=10, justify = 'center')
        self.entryp1.grid(row = 1, column = 1, padx = padx_, pady = pady_)
        self.entryp1.insert(0, '286')
        
        
        ########## ESPAÇO P2 ##########
        self.labelp2 = ttk.Label(self.frame0, text = 'Consumo de vapor [kg vapor / t cana]:')
        self.labelp2.grid(row = 2, column = 0, sticky = W)
        
        self.entryp2 = ttk.Entry(self.frame0, width=10, justify = 'center')
        self.entryp2.grid(row = 2, column = 1, padx = padx_, pady = pady_)
        self.entryp2.insert(0, '454.53')
        
        
        ########## ESPAÇO P3 ##########
        self.labelp3 = ttk.Label(self.frame0, text = 'Consumo de energia [kWh / t cana]:')
        self.labelp3.grid(row = 3, column = 0, sticky = W)
        
        self.entryp3 = ttk.Entry(self.frame0, width=10, justify = 'center')
        self.entryp3.grid(row = 3, column = 1, padx = padx_, pady = pady_)
        self.entryp3.insert(0, '28')
        
        
        ########## ESPAÇO P4 ##########
        self.labelp4 = ttk.Label(self.frame0, text = 'Fração de bagaço na cana [%]:')
        self.labelp4.grid(row = 4, column = 0, sticky = W)
        
        self.entryp4 = ttk.Entry(self.frame0, width=10, justify = 'center')
        self.entryp4.grid(row = 4, column = 1, padx = padx_, pady = pady_)
        self.entryp4.insert(0, '28.5')
        
        
        ########## ESPAÇO P5 ##########
        self.labelp5 = ttk.Label(self.frame0, text = 'PCI do bagaço [MJ / kg bagaço]:')
        self.labelp5.grid(row = 5, column = 0, sticky = W)
        
        self.entryp5 = ttk.Entry(self.frame0, width=10, justify = 'center')
        self.entryp5.grid(row = 5, column = 1, padx = padx_, pady = pady_)
        self.entryp5.insert(0, '7.736')

       
        #############################
        ########## FRAME 1 ##########
        #############################
        
        self.frame1 = LabelFrame(self, text = 'Temperatura [°C]')
        self.frame1.grid(row = 3, column = 0, pady = 3, padx = 15)
        
        
        ########## ESPAÇO 1 ##########
        self.label1 = ttk.Label(self.frame1, text = '(1) Saída da caldeira:                                     ')
        self.label1.grid(row = 1, column = 0, sticky = W)
        
        self.entry1 = ttk.Entry(self.frame1, width=10, justify = 'center')
        self.entry1.grid(row = 1, column = 1, padx = padx_, pady = pady_)
        self.entry1.insert(0, '530')
        
        
        ########## ESPAÇO 2 ##########
        self.label2 = ttk.Label(self.frame1, text = '(1)-(2) Redução na linha:')
        self.label2.grid(row = 2, column = 0, sticky = W)
        
        self.entry2 = ttk.Entry(self.frame1, width=10, justify = 'center')
        self.entry2.grid(row = 2, column = 1, padx = padx_, pady = pady_)
        self.entry2.insert(0, '0')
        
        
        ########## ESPAÇO 3 ##########
        self.label3 = ttk.Label(self.frame1, text = '(15) Saída do processo:')
        self.label3.grid(row = 3, column = 0, sticky = W)
        
        self.entry3 = ttk.Entry(self.frame1, width=10, justify = 'center')
        self.entry3.grid(row = 3, column = 1, padx = padx_, pady = pady_)
        self.entry3.insert(0, '124.7')
        
        #############################
        ########## FRAME 2 ##########
        #############################
        
        self.frame2 = LabelFrame(self, text = 'Pressão [bar]')
        self.frame2.grid(row = 4, column = 0, pady = 3, padx = 15)
        
        ########## ESPAÇO 4 ##########
        self.label4 = ttk.Label(self.frame2, text = '(1) Saída da caldeira:                                     ')
        self.label4.grid(row = 4, column = 0, sticky = W)
        
        self.entry4 = ttk.Entry(self.frame2, width=10, justify = 'center')
        self.entry4.grid(row = 4, column = 1, padx = padx_, pady = pady_)
        self.entry4.insert(0, '78.6')
        
        
        ########## ESPAÇO 5 ##########
        self.label5 = ttk.Label(self.frame2, text = '(1)-(2) Perda de carga:')
        self.label5.grid(row = 5, column = 0, sticky = W)
        
        self.entry5 = ttk.Entry(self.frame2, width=10, justify = 'center')
        self.entry5.grid(row = 5, column = 1, padx = padx_, pady = pady_)
        self.entry5.insert(0, '10')
        
        
        ########## ESPAÇO 6 ##########
        self.label6 = ttk.Label(self.frame2, text = '(4) Saída da Turbina 1:')
        self.label6.grid(row = 6, column = 0, sticky = W)
        
        self.entry6 = ttk.Entry(self.frame2, width=10, justify = 'center')
        self.entry6.grid(row = 6, column = 1, padx = padx_, pady = pady_)
        self.entry6.insert(0, '2.45')
        
        
        ########## ESPAÇO 7 ##########
        self.label7 = ttk.Label(self.frame2, text = '(6) Saída da Turbina 2:')
        self.label7.grid(row = 7, column = 0, sticky = W)
    
        self.entry7 = ttk.Entry(self.frame2, width=10, justify = 'center')
        self.entry7.grid(row = 7, column = 1, padx = padx_, pady = pady_)
        self.entry7.insert(0, '0.07')
        
        
        #############################
        ########## FRAME 3 ##########
        #############################
        
        self.frame3 = LabelFrame(self, text = 'Vazão Mássica')
        self.frame3.grid(row = 5, column = 0, pady = 3, padx = 15)
        
        ########## ESPAÇO 8 ##########
        self.label8 = ttk.Label(self.frame3, text = '(1) Caldeira [t/h]:                                           ')
        self.label8.grid(row = 8, column = 0, sticky = W)
        
        self.entry8 = ttk.Entry(self.frame3, width=10, justify = 'center')
        self.entry8.grid(row = 8, column = 1, padx = padx_, pady = pady_)
        self.entry8.insert(0, '160')
        

        ########## ESPAÇO 9 ##########
        self.label9 = ttk.Label(self.frame3, text = 'Fração de (1) que vai a (5):')
        self.label9.grid(row = 10, column = 0, sticky = W)

        self.entry9 = ttk.Entry(self.frame3, width=10, justify = 'center')
        self.entry9.grid(row = 10, column = 1, padx = padx_, pady = pady_)
        self.entry9.insert(0, '0.1744')
        
        
        ########## ESPAÇO 10 ##########
        self.label10 = ttk.Label(self.frame3, text = 'Fração de (8) que vai a (9):')
        self.label10.grid(row = 11, column = 0, sticky = W)
        
        self.entry10 = ttk.Entry(self.frame3, width=10, justify = 'center')
        self.entry10.grid(row = 11, column = 1, padx = padx_, pady = pady_)
        self.entry10.insert(0, '0.093')
        
        
        #############################
        ########## FRAME 4 ##########
        #############################
        
        self.frame4 = LabelFrame(self, text = 'Eficiência [%]')
        self.frame4.grid(row = 6, column = 0, pady = 3, padx = 15)
        
        ########## ESPAÇO 11 ##########
        self.label11 = ttk.Label(self.frame4, text = 'Caldeira:                                                          ')
        self.label11.grid(row = 12, column = 0, sticky = W)
        
        self.entry11 = ttk.Entry(self.frame4, width=10, justify = 'center')
        self.entry11.grid(row = 12, column = 1, padx = padx_, pady = pady_)
        self.entry11.insert(0, '78')
        
        
        ########## ESPAÇO 12 ##########
        self.label12 = ttk.Label(self.frame4, text = 'Bomba 1:')
        self.label12.grid(row = 13, column = 0, sticky = W)
        
        self.entry12 = ttk.Entry(self.frame4, width=10, justify = 'center')
        self.entry12.grid(row = 13, column = 1, padx = padx_, pady = pady_)
        self.entry12.insert(0, '75')
        
        
        ########## ESPAÇO 13 ##########
        self.label13 = ttk.Label(self.frame4, text = 'Bomba 2:')
        self.label13.grid(row = 14, column = 0, sticky = W)
        
        self.entry13 = ttk.Entry(self.frame4, width=10, justify = 'center')
        self.entry13.grid(row = 14, column = 1, padx = padx_, pady = pady_)
        self.entry13.insert(0, '75')
        
        
        ########## ESPAÇO 14 ##########
        self.label14 = ttk.Label(self.frame4, text = 'Turbina 1')
        self.label14.grid(row = 15, column = 0, sticky = W)
        
        self.entry14 = ttk.Entry(self.frame4, width=10, justify = 'center')
        self.entry14.grid(row = 15, column = 1, padx = padx_, pady = pady_)
        self.entry14.insert(0, '84')
        
        
        ########## ESPAÇO 15 ##########
        self.label15 = ttk.Label(self.frame4, text = 'Turbina 2:')
        self.label15.grid(row = 16, column = 0, sticky = W)
        
        self.entry15 = ttk.Entry(self.frame4, width=10, justify = 'center')
        self.entry15.grid(row = 16, column = 1, padx = padx_, pady = pady_)
        self.entry15.insert(0, '85.8')
        
        
        #############################
        ########## FRAME 5 ##########
        #############################
        
        self.frame5 = LabelFrame(self, text = 'Ciclo')
        self.frame5.place(x = 420, y = 30)
        
        ########## ESCOLHA DO CICLO ##########
        self.label16 = ttk.Label(self.frame5, text = 'Configuração:')
        self.label16.grid(row = 0, column = 0, sticky = W)
        
        self.cbox = ttk.Combobox(self.frame5,
                                 values = ['Turbinas de contrapressão e condensação',
                                           'Turbina de extração-condensação'], 
                                 state='readonly', 
                                 justify='center',
                                 width = 40)
        
        self.cbox.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.cbox.bind("<<ComboboxSelected>>", self.update_cycle)
        self.cbox.current(0)
        
        
        ############################
        ########## CANVAS ##########
        ############################
        
        self.cycle_canvas = Canvas(self, width=500, height=500, bg = self.cget('bg'))
        self.cycle_canvas.place(x = 350, y = 100)
        
        desenho_1(self.cycle_canvas)
        
        
        #############################
        ########## SIMULAR ##########
        #############################
        
        # Button 1
        self.button1 = Button(self, text = 'Simular', command = lambda: self.parent.calculate_cycle(), width = 15)
        self.button1.grid(row = 7, column = 0, pady = 3)
        
        
    def get_params(self):
        
        dict_configuracao = {'Turbinas de contrapressão e condensação': 0,
                             'Turbina de extração-condensação': 1}
        
        return [self.entryp1.get(),
                self.entryp2.get(),
                self.entryp3.get(),
                self.entryp4.get(),
                self.entryp5.get(),
                self.entry1.get(),
                self.entry2.get(),
                self.entry3.get(),
                self.entry4.get(),
                self.entry5.get(),
                self.entry6.get(),
                self.entry7.get(),
                self.entry8.get(),
                self.entry9.get(),
                self.entry10.get(),
                self.entry11.get(),
                self.entry12.get(),
                self.entry13.get(),
                self.entry14.get(),
                self.entry15.get(),
                dict_configuracao[self.cbox.get()]]
        
    def update_cycle(self, event):
        
        dict_configuracao = {'Turbinas de contrapressão e condensação': 0,
                             'Turbina de extração-condensação': 1}
        
        cycle_type = dict_configuracao[self.cbox.get()]
        
        if cycle_type == 0:
            self.cycle_canvas.delete("all")
            desenho_1(self.cycle_canvas)
        elif cycle_type == 1:
            self.cycle_canvas.delete("all")
            desenho_2(self.cycle_canvas)
            
  
class TabTwo(Frame):
    def __init__(self,parent):
        Frame.__init__(self)
        self.label = Label(self, text="Hi This is Tab2")
        self.label.grid(row=1,column=0,padx=10,pady=10)
        self.parent = parent
        

        #############################
        ########## FRAME 1 ##########
        #############################   

        # LabelFrame 1
        self.frame1 = LabelFrame(self, text = 'Estados Termodinâmicos')
        self.frame1.grid(row = 1, column = 0, pady = 10, padx = 15)
        
        
        # Colunas        
        self.label_m = ttk.Label(self.frame1, text = 'm [t/h]', justify = 'center')
        self.label_m.grid(row = 0, column = 1)
        
        self.label_p = ttk.Label(self.frame1, text = 'p [bar]', justify = 'center')
        self.label_p.grid(row = 0, column = 2)
        
        self.label_T = ttk.Label(self.frame1, text = 'T [oC]', justify = 'center')
        self.label_T.grid(row = 0, column = 3)
        
        self.label_v = ttk.Label(self.frame1, text = 'v [m³/kg]', justify = 'center')
        self.label_v.grid(row = 0, column = 4)
        
        self.label_h = ttk.Label(self.frame1, text = 'h [kJ/kg]', justify = 'center')
        self.label_h.grid(row = 0, column = 5)
        
        self.label_s = ttk.Label(self.frame1, text = 's [kJ/kg.K]', justify = 'center')
        self.label_s.grid(row = 0, column = 6)
        
        
        # Linhas
        self.label1 = ttk.Label(self.frame1, text = '(1)', justify = 'center')
        self.label1.grid(row = 1, column = 0)
        
        self.label2 = ttk.Label(self.frame1, text = '(2)', justify = 'center')
        self.label2.grid(row = 2, column = 0)
        
        self.label3 = ttk.Label(self.frame1, text = '(3)', justify = 'center')
        self.label3.grid(row = 3, column = 0)
        
        self.label4 = ttk.Label(self.frame1, text = '(4)', justify = 'center')
        self.label4.grid(row = 4, column = 0)
        
        self.label5 = ttk.Label(self.frame1, text = '(5)', justify = 'center')
        self.label5.grid(row = 5, column = 0)
        
        self.label6 = ttk.Label(self.frame1, text = '(6)', justify = 'center')
        self.label6.grid(row = 6, column = 0)
        
        self.label7 = ttk.Label(self.frame1, text = '(7)', justify = 'center')
        self.label7.grid(row = 7, column = 0)
        
        self.label8 = ttk.Label(self.frame1, text = '(8)', justify = 'center')
        self.label8.grid(row = 8, column = 0)
        
        self.label9 = ttk.Label(self.frame1, text = '(9)', justify = 'center')
        self.label9.grid(row = 9, column = 0)
        
        self.label10 = ttk.Label(self.frame1, text = '(10)', justify = 'center')
        self.label10.grid(row = 10, column = 0)
        
        self.label11 = ttk.Label(self.frame1, text = '(11)', justify = 'center')
        self.label11.grid(row = 11, column = 0)
        
        self.label12 = ttk.Label(self.frame1, text = '(12)', justify = 'center')
        self.label12.grid(row = 12, column = 0)
        
        self.label13 = ttk.Label(self.frame1, text = '(13)', justify = 'center')
        self.label13.grid(row = 13, column = 0)
        
        self.label14 = ttk.Label(self.frame1, text = '(14)', justify = 'center')
        self.label14.grid(row = 14, column = 0)
        
        self.label15 = ttk.Label(self.frame1, text = '(15)', justify = 'center')
        self.label15.grid(row = 15, column = 0)
        
        self.label16 = ttk.Label(self.frame1, text = '(16)', justify = 'center')
        self.label16.grid(row = 16, column = 0)
        
        self.label17 = ttk.Label(self.frame1, text = '(17)', justify = 'center')
        self.label17.grid(row = 17, column = 0)
        
        
        # Vazões Mássicas
        self.entry_m1 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m1.grid(row = 1, column = 1, padx = 2, pady = 2)
        
        self.entry_m2 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m2.grid(row = 2, column = 1, padx = 2, pady = 2)
        
        self.entry_m3 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m3.grid(row = 3, column = 1, padx = 2, pady = 2)
        
        self.entry_m4 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m4.grid(row = 4, column = 1, padx = 2, pady = 2)
        
        self.entry_m5 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m5.grid(row = 5, column = 1, padx = 2, pady = 2)
        
        self.entry_m6 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m6.grid(row = 6, column = 1, padx = 2, pady = 2)
        
        self.entry_m7 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m7.grid(row = 7, column = 1, padx = 2, pady = 2)
        
        self.entry_m8 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m8.grid(row = 8, column = 1, padx = 2, pady = 2)
        
        self.entry_m9 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m9.grid(row = 9, column = 1, padx = 2, pady = 2)
        
        self.entry_m10 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m10.grid(row = 10, column = 1, padx = 2, pady = 2)
        
        self.entry_m11 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m11.grid(row = 11, column = 1, padx = 2, pady = 2)
        
        self.entry_m12 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m12.grid(row = 12, column = 1, padx = 2, pady = 2)
        
        self.entry_m13 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m13.grid(row = 13, column = 1, padx = 2, pady = 2)
        
        self.entry_m14 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m14.grid(row = 14, column = 1, padx = 2, pady = 2)
        
        self.entry_m15 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m15.grid(row = 15, column = 1, padx = 2, pady = 2)
        
        self.entry_m16 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m16.grid(row = 16, column = 1, padx = 2, pady = 2)
        
        self.entry_m17 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_m17.grid(row = 17, column = 1, padx = 2, pady = 2)
        
        
        # Pressões
        self.entry_p1 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p1.grid(row = 1, column = 2, padx = 2, pady = 2)
        
        self.entry_p2 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p2.grid(row = 2, column = 2, padx = 2, pady = 2)
        
        self.entry_p3 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p3.grid(row = 3, column = 2, padx = 2, pady = 2)
        
        self.entry_p4 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p4.grid(row = 4, column = 2, padx = 2, pady = 2)
        
        self.entry_p5 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p5.grid(row = 5, column = 2, padx = 2, pady = 2)
        
        self.entry_p6 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p6.grid(row = 6, column = 2, padx = 2, pady = 2)
        
        self.entry_p7 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p7.grid(row = 7, column = 2, padx = 2, pady = 2)
        
        self.entry_p8 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p8.grid(row = 8, column = 2, padx = 2, pady = 2)
        
        self.entry_p9 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p9.grid(row = 9, column = 2, padx = 2, pady = 2)
        
        self.entry_p10 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p10.grid(row = 10, column = 2, padx = 2, pady = 2)
        
        self.entry_p11 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p11.grid(row = 11, column = 2, padx = 2, pady = 2)
        
        self.entry_p12 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p12.grid(row = 12, column = 2, padx = 2, pady = 2)
        
        self.entry_p13 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p13.grid(row = 13, column = 2, padx = 2, pady = 2)
        
        self.entry_p14 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p14.grid(row = 14, column = 2, padx = 2, pady = 2)
        
        self.entry_p15 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p15.grid(row = 15, column = 2, padx = 2, pady = 2)
        
        self.entry_p16 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p16.grid(row = 16, column = 2, padx = 2, pady = 2)
        
        self.entry_p17 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_p17.grid(row = 17, column = 2, padx = 2, pady = 2)
        
        
        # Temperaturas
        self.entry_T1 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T1.grid(row = 1, column = 3, padx = 2, pady = 2)
        
        self.entry_T2 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T2.grid(row = 2, column = 3, padx = 2, pady = 2)
        
        self.entry_T3 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T3.grid(row = 3, column = 3, padx = 2, pady = 2)
        
        self.entry_T4 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T4.grid(row = 4, column = 3, padx = 2, pady = 2)
        
        self.entry_T5 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T5.grid(row = 5, column = 3, padx = 2, pady = 2)
        
        self.entry_T6 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T6.grid(row = 6, column = 3, padx = 2, pady = 2)
        
        self.entry_T7 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T7.grid(row = 7, column = 3, padx = 2, pady = 2)
        
        self.entry_T8 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T8.grid(row = 8, column = 3, padx = 2, pady = 2)
        
        self.entry_T9 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T9.grid(row = 9, column = 3, padx = 2, pady = 2)
        
        self.entry_T10 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T10.grid(row = 10, column = 3, padx = 2, pady = 2)
        
        self.entry_T11 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T11.grid(row = 11, column = 3, padx = 2, pady = 2)
        
        self.entry_T12 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T12.grid(row = 12, column = 3, padx = 2, pady = 2)
        
        self.entry_T13 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T13.grid(row = 13, column = 3, padx = 2, pady = 2)
        
        self.entry_T14 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T14.grid(row = 14, column = 3, padx = 2, pady = 2)
        
        self.entry_T15 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T15.grid(row = 15, column = 3, padx = 2, pady = 2)
        
        self.entry_T16 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T16.grid(row = 16, column = 3, padx = 2, pady = 2)
        
        self.entry_T17 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_T17.grid(row = 17, column = 3, padx = 2, pady = 2)
        
        
        # Volumes Específicos
        self.entry_v1 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v1.grid(row = 1, column = 4, padx = 2, pady = 2)
        
        self.entry_v2 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v2.grid(row = 2, column = 4, padx = 2, pady = 2)
        
        self.entry_v3 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v3.grid(row = 3, column = 4, padx = 2, pady = 2)
        
        self.entry_v4 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v4.grid(row = 4, column = 4, padx = 2, pady = 2)
        
        self.entry_v5 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v5.grid(row = 5, column = 4, padx = 2, pady = 2)
        
        self.entry_v6 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v6.grid(row = 6, column = 4, padx = 2, pady = 2)
        
        self.entry_v7 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v7.grid(row = 7, column = 4, padx = 2, pady = 2)
        
        self.entry_v8 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v8.grid(row = 8, column = 4, padx = 2, pady = 2)
        
        self.entry_v9 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v9.grid(row = 9, column = 4, padx = 2, pady = 2)
        
        self.entry_v10 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v10.grid(row = 10, column = 4, padx = 2, pady = 2)
        
        self.entry_v11 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v11.grid(row = 11, column = 4, padx = 2, pady = 2)
        
        self.entry_v12 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v12.grid(row = 12, column = 4, padx = 2, pady = 2)
        
        self.entry_v13 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v13.grid(row = 13, column = 4, padx = 2, pady = 2)
        
        self.entry_v14 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v14.grid(row = 14, column = 4, padx = 2, pady = 2)
        
        self.entry_v15 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v15.grid(row = 15, column = 4, padx = 2, pady = 2)
        
        self.entry_v16 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v16.grid(row = 16, column = 4, padx = 2, pady = 2)
        
        self.entry_v17 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_v17.grid(row = 17, column = 4, padx = 2, pady = 2)
        
        
        # Entalpias
        self.entry_h1 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h1.grid(row = 1, column = 5, padx = 2, pady = 2)
        
        self.entry_h2 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h2.grid(row = 2, column = 5, padx = 2, pady = 2)
        
        self.entry_h3 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h3.grid(row = 3, column = 5, padx = 2, pady = 2)
        
        self.entry_h4 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h4.grid(row = 4, column = 5, padx = 2, pady = 2)
        
        self.entry_h5 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h5.grid(row = 5, column = 5, padx = 2, pady = 2)
        
        self.entry_h6 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h6.grid(row = 6, column = 5, padx = 2, pady = 2)
        
        self.entry_h7 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h7.grid(row = 7, column = 5, padx = 2, pady = 2)
        
        self.entry_h8 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h8.grid(row = 8, column = 5, padx = 2, pady = 2)
        
        self.entry_h9 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h9.grid(row = 9, column = 5, padx = 2, pady = 2)
        
        self.entry_h10 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h10.grid(row = 10, column = 5, padx = 2, pady = 2)
        
        self.entry_h11 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h11.grid(row = 11, column = 5, padx = 2, pady = 2)
        
        self.entry_h12 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h12.grid(row = 12, column = 5, padx = 2, pady = 2)
        
        self.entry_h13 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h13.grid(row = 13, column = 5, padx = 2, pady = 2)
        
        self.entry_h14 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h14.grid(row = 14, column = 5, padx = 2, pady = 2)
        
        self.entry_h15 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h15.grid(row = 15, column = 5, padx = 2, pady = 2)
        
        self.entry_h16 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h16.grid(row = 16, column = 5, padx = 2, pady = 2)
        
        self.entry_h17 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_h17.grid(row = 17, column = 5, padx = 2, pady = 2)
        
        
        # Entropias
        self.entry_s1 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s1.grid(row = 1, column = 6, padx = 2, pady = 2)
        
        self.entry_s2 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s2.grid(row = 2, column = 6, padx = 2, pady = 2)
        
        self.entry_s3 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s3.grid(row = 3, column = 6, padx = 2, pady = 2)
        
        self.entry_s4 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s4.grid(row = 4, column = 6, padx = 2, pady = 2)
        
        self.entry_s5 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s5.grid(row = 5, column = 6, padx = 2, pady = 2)
        
        self.entry_s6 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s6.grid(row = 6, column = 6, padx = 2, pady = 2)
        
        self.entry_s7 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s7.grid(row = 7, column = 6, padx = 2, pady = 2)
        
        self.entry_s8 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s8.grid(row = 8, column = 6, padx = 2, pady = 2)
        
        self.entry_s9 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s9.grid(row = 9, column = 6, padx = 2, pady = 2)
        
        self.entry_s10 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s10.grid(row = 10, column = 6, padx = 2, pady = 2)
        
        self.entry_s11 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s11.grid(row = 11, column = 6, padx = 2, pady = 2)
        
        self.entry_s12 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s12.grid(row = 12, column = 6, padx = 2, pady = 2)
        
        self.entry_s13 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s13.grid(row = 13, column = 6, padx = 2, pady = 2)
        
        self.entry_s14 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s14.grid(row = 14, column = 6, padx = 2, pady = 2)
        
        self.entry_s15 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s15.grid(row = 15, column = 6, padx = 2, pady = 2)
        
        self.entry_s16 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s16.grid(row = 16, column = 6, padx = 2, pady = 2)
        
        self.entry_s17 = ttk.Entry(self.frame1, width=8, justify = 'center', state = 'readonly')
        self.entry_s17.grid(row = 17, column = 6, padx = 2, pady = 2)
        
        
        #############################
        ########## FRAME 2 ##########
        #############################
        
        self.frame2 = LabelFrame(self, text = 'Bagaço [t/h]')
        self.frame2.place(x = 420, y = 10)
        
        
        ########## ESPAÇO 1 ##########
        self.label1 = ttk.Label(self.frame2, text = 'Bagaço produzido:                     ')
        self.label1.grid(row = 1, column = 0, sticky = W)
        
        self.entry1 = ttk.Entry(self.frame2, width=10, justify = 'center', state = 'readonly')
        self.entry1.grid(row = 1, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 2 ##########
        self.label2 = ttk.Label(self.frame2, text = 'Bagaço consumido:')
        self.label2.grid(row = 2, column = 0, sticky = W)
        
        self.entry2 = ttk.Entry(self.frame2, width=10, justify = 'center', state = 'readonly')
        self.entry2.grid(row = 2, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 3 ##########
        self.label3 = ttk.Label(self.frame2, text = 'Bagaço excedente:')
        self.label3.grid(row = 3, column = 0, sticky = W)
        
        self.entry3 = ttk.Entry(self.frame2, width=10, justify = 'center', state = 'readonly')
        self.entry3.grid(row = 3, column = 1, padx = 2, pady = 2)
        
        
        #############################
        ########## FRAME 3 ##########
        #############################
        
        self.frame3 = LabelFrame(self, text = 'Taxa de Calor [MW]')
        self.frame3.place(x = 420, y = 131)
        
        
        ########## ESPAÇO 4 ##########
        self.label4 = ttk.Label(self.frame3, text = 'Fornecido à caldeira:                  ')
        self.label4.grid(row = 1, column = 0, sticky = W)
        
        self.entry4 = ttk.Entry(self.frame3, width=10, justify = 'center', state = 'readonly')
        self.entry4.grid(row = 1, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 5 ##########
        self.label5 = ttk.Label(self.frame3, text = 'Perdido para o ambiente:')
        self.label5.grid(row = 2, column = 0, sticky = W)
        
        self.entry5 = ttk.Entry(self.frame3, width=10, justify = 'center', state = 'readonly')
        self.entry5.grid(row = 2, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 6 ##########
        self.label6 = ttk.Label(self.frame3, text = 'Fornecido ao processo:')
        self.label6.grid(row = 3, column = 0, sticky = W)
    
        self.entry6 = ttk.Entry(self.frame3, width=10, justify = 'center', state = 'readonly')
        self.entry6.grid(row = 3, column = 1, padx = 2, pady = 2)
        

        ########## ESPAÇO 7 ##########
        self.label7 = ttk.Label(self.frame3, text = 'Removido no condensador:')
        self.label7.grid(row = 4, column = 0, sticky = W)
    
        self.entry7 = ttk.Entry(self.frame3, width=10, justify = 'center', state = 'readonly')
        self.entry7.grid(row = 4, column = 1, padx = 2, pady = 2)
        
        
        #############################
        ########## FRAME 4 ##########
        #############################
        
        self.frame4 = LabelFrame(self, text = 'Potência [MW]')
        self.frame4.place(x = 420, y = 278)
        
        
        ########## ESPAÇO 8 ##########
        self.label8 = ttk.Label(self.frame4, text = 'Geração da Turbina 1:')
        self.label8.grid(row = 1, column = 0, sticky = W)
        
        self.entry8 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry8.grid(row = 1, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 9 ##########
        self.label9 = ttk.Label(self.frame4, text = 'Geração da Turbina 2:')
        self.label9.grid(row = 2, column = 0, sticky = W)
        
        self.entry9 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry9.grid(row = 2, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 10 ##########
        self.label10 = ttk.Label(self.frame4, text = 'Consumo da Bomba 1:              ')
        self.label10.grid(row = 3, column = 0, sticky = W)
    
        self.entry10 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry10.grid(row = 3, column = 1, padx = 2, pady = 2)
        

        ########## ESPAÇO 11 ##########
        self.label11 = ttk.Label(self.frame4, text = 'Consumo da Bomba 2:')
        self.label11.grid(row = 4, column = 0, sticky = W)
    
        self.entry11 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry11.grid(row = 4, column = 1, padx = 2, pady = 2)
        
        ########## ESPAÇO 12 ##########
        self.label12 = ttk.Label(self.frame4, text = 'Geração líquida do ciclo:')
        self.label12.grid(row = 5, column = 0, sticky = W)
        
        self.entry12 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry12.grid(row = 5, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 13 ##########
        self.label13 = ttk.Label(self.frame4, text = 'Consumo do processo:')
        self.label13.grid(row = 6, column = 0, sticky = W)
        
        self.entry13 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry13.grid(row = 6, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 14 ##########
        self.label14 = ttk.Label(self.frame4, text = 'Excedente comercializável:')
        self.label14.grid(row = 7, column = 0, sticky = W)
    
        self.entry14 = ttk.Entry(self.frame4, width=10, justify = 'center', state = 'readonly')
        self.entry14.grid(row = 7, column = 1, padx = 2, pady = 2)
        

        
        #############################
        ########## FRAME 5 ##########
        #############################
        
        self.frame5 = LabelFrame(self, text = 'Índices de Desempenho')
        self.frame5.place(x = 688, y = 10)
        
        
        ########## ESPAÇO 15 ##########
        self.label15 = ttk.Label(self.frame5, text = 'FUE:                      ')
        self.label15.grid(row = 1, column = 0, sticky = W)
        
        self.entry15 = ttk.Entry(self.frame5, width=10, justify = 'center', state = 'readonly')
        self.entry15.grid(row = 1, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 16 ##########
        self.label16 = ttk.Label(self.frame5, text = 'IPE:')
        self.label16.grid(row = 2, column = 0, sticky = W)
        
        self.entry16 = ttk.Entry(self.frame5, width=10, justify = 'center', state = 'readonly')
        self.entry16.grid(row = 2, column = 1, padx = 2, pady = 2)
        
        
        ########## ESPAÇO 17 ##########
        self.label17 = ttk.Label(self.frame5, text = 'EEC:')
        self.label17.grid(row = 3, column = 0, sticky = W)
    
        self.entry17 = ttk.Entry(self.frame5, width=10, justify = 'center', state = 'readonly')
        self.entry17.grid(row = 3, column = 1, padx = 2, pady = 2)
        

        ########## ESPAÇO 18 ##########
        self.label18 = ttk.Label(self.frame5, text = 'IGP:')
        self.label18.grid(row = 4, column = 0, sticky = W)
    
        self.entry18 = ttk.Entry(self.frame5, width=10, justify = 'center', state = 'readonly')
        self.entry18.grid(row = 4, column = 1, padx = 2, pady = 2)
        
        ########## ESPAÇO 19 ##########
        self.label19 = ttk.Label(self.frame5, text = 'RPC:')
        self.label19.grid(row = 5, column = 0, sticky = W)
        
        self.entry19 = ttk.Entry(self.frame5, width=10, justify = 'center', state = 'readonly')
        self.entry19.grid(row = 5, column = 1, padx = 2, pady = 2)
        
    
    def set_entry(self, entry, value):
        entry.config(state = 'normal')
        entry.delete(0, END)
        entry.insert(0, value)
        entry.config(state = 'readonly')
    
    def set_results(self, results, df):
        
        ##########################################
        ########## TRATAMENTO DOS DADOS ##########
        ##########################################
        
        df['m [t/h]'] = df['m [t/h]'].apply(lambda x: np.round(x, 2))
        df['p [bar]'] = df['p [bar]'].apply(lambda x: np.round(x, 2))
        df['T [oC]'] = df['T [oC]'].apply(lambda x: np.round(x, 2))
        df['v [m³/kg]'] = df['v [m³/kg]'].apply(lambda x: np.round(x, 5))
        df['h [kJ/kg]'] = df['h [kJ/kg]'].apply(lambda x: np.round(x, 2))
        df['s [kJ/kg.K]'] = df['s [kJ/kg.K]'].apply(lambda x: np.round(x, 4))
        
        df = df.applymap(lambda x: '{:g}'.format(x))
        
        results[:9] = list(map(lambda x: np.round(x,2), results[:9]))
        results[9:11] = list(map(lambda x: np.round(x,3), results[9:11]))
        results[11:14] = list(map(lambda x: np.round(x,2), results[11:14]))
        results[14:] = list(map(lambda x: np.round(x,4), results[14:]))
        results = list(map(lambda x: '{:g}'.format(x), results))
        
        
        ########################################
        ########## INSERÇÃO DOS DADOS ##########
        ########################################
        
        # Vazão Mássica
        self.set_entry(self.entry_m1, df.loc[1, 'm [t/h]'])
        self.set_entry(self.entry_m2, df.loc[2, 'm [t/h]'])
        self.set_entry(self.entry_m3, df.loc[3, 'm [t/h]'])
        self.set_entry(self.entry_m4, df.loc[4, 'm [t/h]'])
        self.set_entry(self.entry_m5, df.loc[5, 'm [t/h]'])
        self.set_entry(self.entry_m6, df.loc[6, 'm [t/h]'])
        self.set_entry(self.entry_m7, df.loc[7, 'm [t/h]'])
        self.set_entry(self.entry_m8, df.loc[8, 'm [t/h]'])
        self.set_entry(self.entry_m9, df.loc[9, 'm [t/h]'])
        self.set_entry(self.entry_m10, df.loc[10, 'm [t/h]'])
        self.set_entry(self.entry_m11, df.loc[11, 'm [t/h]'])
        self.set_entry(self.entry_m12, df.loc[12, 'm [t/h]'])
        self.set_entry(self.entry_m13, df.loc[13, 'm [t/h]'])
        self.set_entry(self.entry_m14, df.loc[14, 'm [t/h]'])
        self.set_entry(self.entry_m15, df.loc[15, 'm [t/h]'])
        self.set_entry(self.entry_m16, df.loc[16, 'm [t/h]'])
        self.set_entry(self.entry_m17, df.loc[17, 'm [t/h]'])
        
        # Pressão
        self.set_entry(self.entry_p1, df.loc[1, 'p [bar]'])
        self.set_entry(self.entry_p2, df.loc[2, 'p [bar]'])
        self.set_entry(self.entry_p3, df.loc[3, 'p [bar]'])
        self.set_entry(self.entry_p4, df.loc[4, 'p [bar]'])
        self.set_entry(self.entry_p5, df.loc[5, 'p [bar]'])
        self.set_entry(self.entry_p6, df.loc[6, 'p [bar]'])
        self.set_entry(self.entry_p7, df.loc[7, 'p [bar]'])
        self.set_entry(self.entry_p8, df.loc[8, 'p [bar]'])
        self.set_entry(self.entry_p9, df.loc[9, 'p [bar]'])
        self.set_entry(self.entry_p10, df.loc[10, 'p [bar]'])
        self.set_entry(self.entry_p11, df.loc[11, 'p [bar]'])
        self.set_entry(self.entry_p12, df.loc[12, 'p [bar]'])
        self.set_entry(self.entry_p13, df.loc[13, 'p [bar]'])
        self.set_entry(self.entry_p14, df.loc[14, 'p [bar]'])
        self.set_entry(self.entry_p15, df.loc[15, 'p [bar]'])
        self.set_entry(self.entry_p16, df.loc[16, 'p [bar]'])
        self.set_entry(self.entry_p17, df.loc[17, 'p [bar]'])
        
        # Temperatura
        self.set_entry(self.entry_T1, df.loc[1, 'T [oC]'])
        self.set_entry(self.entry_T2, df.loc[2, 'T [oC]'])
        self.set_entry(self.entry_T3, df.loc[3, 'T [oC]'])
        self.set_entry(self.entry_T4, df.loc[4, 'T [oC]'])
        self.set_entry(self.entry_T5, df.loc[5, 'T [oC]'])
        self.set_entry(self.entry_T6, df.loc[6, 'T [oC]'])
        self.set_entry(self.entry_T7, df.loc[7, 'T [oC]'])
        self.set_entry(self.entry_T8, df.loc[8, 'T [oC]'])
        self.set_entry(self.entry_T9, df.loc[9, 'T [oC]'])
        self.set_entry(self.entry_T10, df.loc[10, 'T [oC]'])
        self.set_entry(self.entry_T11, df.loc[11, 'T [oC]'])
        self.set_entry(self.entry_T12, df.loc[12, 'T [oC]'])
        self.set_entry(self.entry_T13, df.loc[13, 'T [oC]'])
        self.set_entry(self.entry_T14, df.loc[14, 'T [oC]'])
        self.set_entry(self.entry_T15, df.loc[15, 'T [oC]'])
        self.set_entry(self.entry_T16, df.loc[16, 'T [oC]'])
        self.set_entry(self.entry_T17, df.loc[17, 'T [oC]'])
        
        # Volume Específico
        self.set_entry(self.entry_v1, df.loc[1, 'v [m³/kg]'])
        self.set_entry(self.entry_v2, df.loc[2, 'v [m³/kg]'])
        self.set_entry(self.entry_v3, df.loc[3, 'v [m³/kg]'])
        self.set_entry(self.entry_v4, df.loc[4, 'v [m³/kg]'])
        self.set_entry(self.entry_v5, df.loc[5, 'v [m³/kg]'])
        self.set_entry(self.entry_v6, df.loc[6, 'v [m³/kg]'])
        self.set_entry(self.entry_v7, df.loc[7, 'v [m³/kg]'])
        self.set_entry(self.entry_v8, df.loc[8, 'v [m³/kg]'])
        self.set_entry(self.entry_v9, df.loc[9, 'v [m³/kg]'])
        self.set_entry(self.entry_v10, df.loc[10, 'v [m³/kg]'])
        self.set_entry(self.entry_v11, df.loc[11, 'v [m³/kg]'])
        self.set_entry(self.entry_v12, df.loc[12, 'v [m³/kg]'])
        self.set_entry(self.entry_v13, df.loc[13, 'v [m³/kg]'])
        self.set_entry(self.entry_v14, df.loc[14, 'v [m³/kg]'])
        self.set_entry(self.entry_v15, df.loc[15, 'v [m³/kg]'])
        self.set_entry(self.entry_v16, df.loc[16, 'v [m³/kg]'])
        self.set_entry(self.entry_v17, df.loc[17, 'v [m³/kg]'])
     
        # Entalpia
        self.set_entry(self.entry_h1, df.loc[1, 'h [kJ/kg]'])
        self.set_entry(self.entry_h2, df.loc[2, 'h [kJ/kg]'])
        self.set_entry(self.entry_h3, df.loc[3, 'h [kJ/kg]'])
        self.set_entry(self.entry_h4, df.loc[4, 'h [kJ/kg]'])
        self.set_entry(self.entry_h5, df.loc[5, 'h [kJ/kg]'])
        self.set_entry(self.entry_h6, df.loc[6, 'h [kJ/kg]'])
        self.set_entry(self.entry_h7, df.loc[7, 'h [kJ/kg]'])
        self.set_entry(self.entry_h8, df.loc[8, 'h [kJ/kg]'])
        self.set_entry(self.entry_h9, df.loc[9, 'h [kJ/kg]'])
        self.set_entry(self.entry_h10, df.loc[10, 'h [kJ/kg]'])
        self.set_entry(self.entry_h11, df.loc[11, 'h [kJ/kg]'])
        self.set_entry(self.entry_h12, df.loc[12, 'h [kJ/kg]'])
        self.set_entry(self.entry_h13, df.loc[13, 'h [kJ/kg]'])
        self.set_entry(self.entry_h14, df.loc[14, 'h [kJ/kg]'])
        self.set_entry(self.entry_h15, df.loc[15, 'h [kJ/kg]'])
        self.set_entry(self.entry_h16, df.loc[16, 'h [kJ/kg]'])
        self.set_entry(self.entry_h17, df.loc[17, 'h [kJ/kg]'])
        
        # Entropia
        self.set_entry(self.entry_s1, df.loc[1, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s2, df.loc[2, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s3, df.loc[3, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s4, df.loc[4, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s5, df.loc[5, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s6, df.loc[6, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s7, df.loc[7, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s8, df.loc[8, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s9, df.loc[9, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s10, df.loc[10, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s11, df.loc[11, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s12, df.loc[12, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s13, df.loc[13, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s14, df.loc[14, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s15, df.loc[15, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s16, df.loc[16, 's [kJ/kg.K]'])
        self.set_entry(self.entry_s17, df.loc[17, 's [kJ/kg.K]'])
        
        # Resultados
        self.set_entry(self.entry1, results[0])
        self.set_entry(self.entry2, results[1])
        self.set_entry(self.entry3, results[2])
        self.set_entry(self.entry4, results[3])
        self.set_entry(self.entry5, results[4])
        self.set_entry(self.entry6, results[5])
        self.set_entry(self.entry7, results[6])
        self.set_entry(self.entry8, results[7])
        self.set_entry(self.entry9, results[8])
        self.set_entry(self.entry10, results[9])
        self.set_entry(self.entry11, results[10])
        self.set_entry(self.entry12, results[11])
        self.set_entry(self.entry13, results[12])
        self.set_entry(self.entry14, results[13])
        self.set_entry(self.entry15, results[14])
        self.set_entry(self.entry16, results[15])
        self.set_entry(self.entry17, results[16])
        self.set_entry(self.entry18, results[17])
        self.set_entry(self.entry19, results[18])
        
        
class TabThree(Frame):
    def __init__(self,parent):
        Frame.__init__(self)
        self.parent = parent
       
        self.define_canvas()
        

        
        #############################
        ########## FRAME X ##########
        #############################
        
        self.frame_x = LabelFrame(self, text = 'Eixo x')
        self.frame_x.place(x = 45, y = 20)
        
        
        ########## ESPAÇO 1 ##########
        self.label_x = ttk.Label(self.frame_x, text = 'Variável:')
        self.label_x.grid(row = 1, column = 0, sticky = W, pady = 10)
        
        #Combo Box
        x_graphic = StringVar()
        self.x_cbox = ttk.Combobox(self.frame_x, textvariable = x_graphic, values = ('Taxa de moagem [t cana / h]',
                                                                                     'Consumo de vapor no processo [kg vapor / t cana]', 
                                                                                     'Consumo de energia no processo [kWh / t cana]',
                                                                                     'Fração de bagaço na cana [%]',
                                                                                     'PCI do bagaço [MJ / kg bagaço]',
                                                                                     '(1) Temperatura de saída da caldeira [oC]',
                                                                                     '(1)-(2) Redução de temperatura na linha [oC]',
                                                                                     '(15) Temperatura de saída do processo [oC]',
                                                                                     '(1) Pressão de saída da caldeira [bar]',
                                                                                     '(1)-(2) Perda de carga na linha [bar]',
                                                                                     '(4) Pressão de saída da Turbina 1 [bar]',
                                                                                     '(6) Pressão de saída da Turbina 2 [bar]',
                                                                                     '(1) Vazão mássica na caldeira [t/h]',
                                                                                     'Fração da vazão mássica de (1) que vai a (5)',
                                                                                     'Fração da vazão mássica de (8) que vai a (9)',
                                                                                     'Eficiência da caldeira [%]',
                                                                                     'Eficiência da Bomba 1 [%]',
                                                                                     'Eficiência da Bomba 2 [%]',
                                                                                     'Eficiência da Turbina 1 [%]',
                                                                                     'Eficiência da Turbina 2 [%]'), state = 'readonly', justify='center', width = 45)
        self.x_cbox.grid(row = 1, column = 1, padx = 10)
        
        
        ########## ESPAÇO 2 ##########
        self.label_x0 = ttk.Label(self.frame_x, text = 'Limite inferior:')
        self.label_x0.grid(row = 2, column = 0, sticky = W)
        
        self.x0_entry = ttk.Entry(self.frame_x, width=10, justify = 'center')
        self.x0_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)
        
        
        ########## ESPAÇO 3 ##########
        self.label_x0 = ttk.Label(self.frame_x, text = 'Limite superior:')
        self.label_x0.grid(row = 3, column = 0, sticky = W)
        
        self.x1_entry = ttk.Entry(self.frame_x, width=10, justify = 'center')
        self.x1_entry.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

        
        
        #############################
        ########## FRAME Y ##########
        #############################
        
        self.frame_y = LabelFrame(self, text = 'Eixo y')
        self.frame_y.place(x = 455, y = 20)

        ########## ESPAÇO 1 ##########
        self.label_x = ttk.Label(self.frame_y, text = 'Variável:          ')
        self.label_x.grid(row = 1, column = 0, sticky = W, pady = 10)
        
        #Combo Box    
        y_graphic = StringVar()
        self.y_cbox = ttk.Combobox(self.frame_y, textvariable = y_graphic, values = ('FUE',
                                                                                     'IPE',
                                                                                     'EEC',
                                                                                     'IGP',
                                                                                     'RPC',
                                                                                     'Bagaço produzido',
                                                                                     'Bagaço consumido',
                                                                                     'Bagaço excedente',
                                                                                     'Taxa de calor fornecido à caldeira [MW]',
                                                                                     'Taxa de calor perdido para o ambiente [MW]',
                                                                                     'Taxa de calor fornecido ao processo',
                                                                                     'Taxa de calor removido no condensador',
                                                                                     'Geração da Turbina 1 [MW]',
                                                                                     'Geração da Turbina 2 [MW]',
                                                                                     'Consumo da Bomba 1 [MW]',
                                                                                     'Consumo da Bomba 2 [MW]',
                                                                                     'Geração líquida do ciclo [MW]',
                                                                                     'Consumo de potência elétrica no processo [MW]',
                                                                                     'Excedente comercializável de potência [MW]'), justify='center', state = 'readonly', width = 45)
        self.y_cbox.grid(row = 1, column = 1, padx = 10, pady = 10)

        ########## BUTTON ##########
        self.button = ttk.Button(self, text = 'Gerar gráfico', command = lambda: self.parent.calculate_graphic())
        self.button.place(x = 570, y = 115, width = 150)
        
        
    def define_canvas(self):
        
        self.fig = Figure(figsize=(6, 4.5), dpi=115)
        self.fig.patch.set_facecolor('#f0f0f0')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.fig.add_subplot(111)
        self.canvas.get_tk_widget().place(x = 450, y = 400, anchor = CENTER)
        
        
    def get_graphic_params(self):
        
        dict_configuracao = {'Turbinas de contrapressão e condensação': 0,
                             'Turbina de extração-condensação': 1}
        
        return [self.x_cbox.get(),
                self.x0_entry.get(),
                self.x1_entry.get(),
                self.y_cbox.get()]
        
    
    def set_graphic(self, x_graphic, y_graphic):
        
        self.define_canvas()
        
        ax = self.fig.add_subplot(1, 1, 1)
        ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter(useOffset=False))
        ax.plot(x_graphic, y_graphic)
        
        self.canvas.draw()
        
       
class TabFour(Frame):
    def __init__(self,parent):
        Frame.__init__(self)
        self.parent = parent
        self.projeto = get_path(r"inc\TCC_Rafael_Araujo_Vidal.pdf")
        
        # Text
        text = "      Este software foi desenvolvido por Rafael Araujo Vidal, sob "
        text += "orientação do Professor Sílvio Carlos Aníbal de Almeida,\n"
        text += "como parte do Projeto de Graduação em Engenharia Mecânica "
        text += "pela Universidade Federal do Rio de Janeiro.\n\n"
        
        text += "      Para acessar o projeto, clique no botão abaixo.\n\n"
        text += "      Para mais informações: rafael.vidal@poli.ufrj.br .\n\n"
        
        # Label
        self.label = Label(self, text=text, justify=LEFT)
        self.label.grid(row=1,column=0,padx=20,pady=20)
        self.parent = parent
        
        # Button
        self.button = Button(self, text = 'Acessar projeto', command = lambda: os.popen(self.projeto), width = 15)
        self.button.grid(row = 6, column = 0)
        
    def get_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
       
       
def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def cogeracao():
    app = App()
    app.title('Cogeração')
    app.iconbitmap(get_path(r"inc\icon\logo.ico"))
    app.mainloop()
