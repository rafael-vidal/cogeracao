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

import numpy as np
from inc.Ciclo import ciclo 

def graphic(params, graphic_params):
    
    tm, cv, ce, fb, pci, T1, dT, T15, p1, dp, p4, p6, m1, a1, a2, nc, nb1, nb2, nt1, nt2, configuracao = params
    x, x0, x1, y = graphic_params
    
    x0 = float(x0)
    x1 = float(x1)
    
    var = {'Taxa de moagem [t cana / h]': tm,
           'Consumo de vapor no processo [kg vapor / t cana]': cv, 
           'Consumo de energia no processo [kWh / t cana]': ce,
           'Fração de bagaço na cana [%]': fb,
           'PCI do bagaço [MJ / kg bagaço]': pci,
           '(1) Temperatura de saída da caldeira [oC]': T1,
           '(1)-(2) Redução de temperatura na linha [oC]': dT,
           '(15) Temperatura de saída do processo [oC]': T15,
           '(1) Pressão de saída da caldeira [bar]': p1,
           '(1)-(2) Perda de carga na linha [bar]': dp,
           '(4) Pressão de saída da Turbina 1 [bar]': p4,
           '(6) Pressão de saída da Turbina 2 [bar]': p6,
           '(1) Vazão mássica na caldeira [t/h]': m1,
           'Fração da vazão mássica de (1) que vai a (5)': a1,
           'Fração da vazão mássica de (8) que vai a (9)': a2,
           'Eficiência da caldeira [%]': nc,
           'Eficiência da Bomba 1 [%]': nb1,
           'Eficiência da Bomba 2 [%]': nb2,
           'Eficiência da Turbina 1 [%]': nt1, 
           'Eficiência da Turbina 2 [%]': nt2}
    
    y_index = {'Bagaço produzido': 0,
               'Bagaço consumido': 1,
               'Bagaço excedente': 2,
               'Taxa de calor fornecido à caldeira [MW]': 3,
               'Taxa de calor perdido para o ambiente [MW]': 4,
               'Taxa de calor fornecido ao processo': 5,
               'Taxa de calor removido no condensador': 6,
               'Geração da Turbina 1 [MW]': 7,
               'Geração da Turbina 2 [MW]': 8,
               'Consumo da Bomba 1 [MW]': 9,
               'Consumo da Bomba 2 [MW]': 10,
               'Geração líquida do ciclo [MW]': 11,
               'Consumo de potência elétrica no processo [MW]': 12,
               'Excedente comercializável de potência [MW]': 13,
               'FUE': 14,
               'IPE': 15,
               'EEC': 16,
               'IGP': 17,
               'RPC': 18}
    
    
    ind = {k:i for i,k in enumerate(var.keys())}
    indx = ind[x]
    
    
    div = 101
    y_graphic = []
    x_graphic = np.linspace(x0, x1, div).tolist()
    for v in x_graphic:
        params[indx] = v
        y_graphic.append(ciclo(params)[0][y_index[y]])
        
    return x_graphic, y_graphic