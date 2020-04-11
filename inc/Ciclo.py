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


import CoolProp.CoolProp as CP
import pandas as pd
import numpy as np
from inc.errors import Error


def ciclo (params):

    tm, cv, ce, fb, pci, T1, dT, T15, p1, dp, p4, p6, m1, a1, a2, nc, nb1, nb2, nt1, nt2, configuracao = params

    if sum(1 for param in params if param < 0) > 0:
        raise(Error("Os parâmetros de entrada não podem ser negativos."))

    if fb > 100:
        raise(Error("A fração de bagaço na cana deve ser menor ou igual a 100%."))

    if sum(1 for param in [nc, nb1, nb2, nt1, nt2] if param > 100) > 0:
        raise(Error("A eficiência dos componentes deve ser menor ou igual a 100%."))

    
    #################################################
    ########## PROPRIEDADES TERMODINÂMICAS ##########
    #################################################
    
    # Definição dos vetores de propriedades
    m = np.zeros(18)
    p = np.zeros(18)
    T = np.zeros(18)
    h = np.zeros(18)
    s = np.zeros(18)
    d = np.zeros(18)
    
    # Conversões
    fb /= 100
    T1 += 273.15
    T15 += 273.15
    p1 *= 10**5
    dp *= 10**5
    p4 *= 10**5
    p6 *= 10**5
    m1 /= 3.6
    nc /= 100
    nb1 /= 100
    nb2 /= 100
    nt1 /= 100
    nt2 /= 100
    
    # Vazões mássicas
    m[15] = tm * cv / 1000 / 3.6
    
    m[1]  = m1
    m[2]  = m[1]
    
    if configuracao == 0:
        m[3] = (1-a1)*m[1]
    elif configuracao == 1:
        m[3] = m[1]
        
    m[4]  = m[3]    
    m[5]  = a1*m[1]
    m[6]  = m[5]
    m[7]  = m[5]
    m[8]  = m[5]
    m[9]  = a2*m[8]
    m[10] = (1-a2)*m[8]
    m[11] = (1-a1)*m[1]
    m[12] = m[15] - m[9]
    m[13] = m[11] - m[12]
    m[14] = m[15]
    m[16] = m[1]
    m[17] = m[1]

    if sum(1 for param in m if param < 0) > 0:
        raise(Error("Os parâmetros de entrada fornecidos levam a vazões mássicas negativas."))
    
    # Pressões
    p[1] = p1
    p[2]  = p[1] - dp
    p[3] = p[2]
    p[4] = p4

    if configuracao == 0:
        p[5] = p[2]
    elif configuracao == 1:
        p[5] = p[4]

    p[6] = p6
    p[7]  = p[6]
    p[8]  = p[4]
    p[9]  = p[4]
    p[10]  = p[4]
    p[11] = p[4]
    p[12] = p[4]
    p[13] = p[4]
    p[14] = p[4]
    p[15] = p[4]
    p[16] = p[4]
    p[17] = p[1]
    

    try:
        # Estado 1
        T[1] = T1
        h[1] = CP.PropsSI('H', 'P', p[1], 'T', T[1], 'Water')
        d[1] = CP.PropsSI('D', 'P', p[1], 'T', T[1], 'Water')
        s[1] = CP.PropsSI('S', 'P', p[1], 'T', T[1], 'Water')

        # Estado 2
        T[2] = T[1] - dT
        h[2] = CP.PropsSI('H', 'P', p[2], 'T', T[2], 'Water')
        d[2] = CP.PropsSI('D', 'P', p[2], 'T', T[2], 'Water')
        s[2] = CP.PropsSI('S', 'P', p[2], 'T', T[2], 'Water')

        # Estado 3
        T[3] = T[2]
        h[3] = h[2]
        d[3] = d[2]
        s[3] = s[2]

        # Estado 4
        h4s = CP.PropsSI('H', 'P', p[4], 'S', s[3], 'Water')
        h[4] = h[3] - nt1*(h[3] - h4s)
        T[4] = CP.PropsSI('T', 'P', p[4], 'H', h[4], 'Water')
        d[4] = CP.PropsSI('D', 'P', p[4], 'H', h[4], 'Water')
        s[4] = CP.PropsSI('S', 'P', p[4], 'H', h[4], 'Water')

        # Estado 5
        if configuracao == 0:
            T[5] = T[2]
            h[5] = h[2]
            d[5] = d[2]
            s[5] = s[2]
        elif configuracao == 1:
            T[5] = T[4]
            h[5] = h[4]
            d[5] = d[4]
            s[5] = s[4]      

        # Estado 6
        h6s = CP.PropsSI('H', 'P', p[6], 'S', s[5], 'Water')
        h[6] = h[5] - nt2*(h[5] - h6s)
        T[6] = CP.PropsSI('T', 'P', p[6], 'H', h[6], 'Water')
        d[6] = CP.PropsSI('D', 'P', p[6], 'H', h[6], 'Water')
        s[6] = CP.PropsSI('S', 'P', p[6], 'H', h[6], 'Water')

        # Estado 7
        x7 = 0
        h[7] = CP.PropsSI('H', 'P', p[7], 'Q', x7, 'Water')
        T[7] = CP.PropsSI('T', 'P', p[7], 'Q', x7, 'Water')
        d[7] = CP.PropsSI('D', 'P', p[7], 'Q', x7, 'Water')
        s[7] = CP.PropsSI('S', 'P', p[7], 'Q', x7, 'Water')    

        # Estado 8
        h8s = h[7] + 1/d[7] * (p[8] - p[7])
        h[8] = h[7] + (h8s - h[7])/nb1
        T[8] = CP.PropsSI('T', 'P', p[8], 'H', h[8], 'Water')
        d[8] = CP.PropsSI('D', 'P', p[8], 'H', h[8], 'Water')
        s[8] = CP.PropsSI('S', 'P', p[8], 'H', h[8], 'Water')

        # Estado 9
        T[9] = T[8]
        h[9] = h[8]
        d[9] = d[8]
        s[9] = s[8]    

        # Estado 10
        T[10] = T[8]
        h[10] = h[8]
        d[10] = d[8]
        s[10] = s[8]

        # Estado 11
        T[11] = T[4]
        h[11] = h[4]
        d[11] = d[4]
        s[11] = s[4]

        # Estado 12
        T[12] = T[11]
        h[12] = h[11]
        d[12] = d[11]
        s[12] = s[11]

        # Estado 13
        T[13] = T[11]
        h[13] = h[11]
        d[13] = d[11]
        s[13] = s[11]

        # Estado 14
        h[14] = (m[9]*h[9] + m[12]*h[12])/m[14]
        T[14] = CP.PropsSI('T', 'P', p[14], 'H', h[14], 'Water')
        d[14] = CP.PropsSI('D', 'P', p[14], 'H', h[14], 'Water')
        s[14] = CP.PropsSI('S', 'P', p[14], 'H', h[14], 'Water')

        # Estado 15
        T[15] = T15
        h[15] = CP.PropsSI('H', 'P', p[15], 'T', T[15], 'Water')
        d[15] = CP.PropsSI('D', 'P', p[15], 'T', T[15], 'Water')
        s[15] = CP.PropsSI('S', 'P', p[15], 'T', T[15], 'Water')


        # Estado 16
        h[16] = (m[10]*h[10] + m[13]*h[13] + m[15]*h[15])/m[16]
        T[16] = CP.PropsSI('T', 'P', p[16], 'H', h[16], 'Water')
        d[16] = CP.PropsSI('D', 'P', p[16], 'H', h[16], 'Water')
        s[16] = CP.PropsSI('S', 'P', p[16], 'H', h[16], 'Water')

        # Estado 17
        h17s = h[16] + 1/d[16] * (p[17] - p[16])
        h[17] = h[16] + (h17s - h[16])/nb2
        T[17] = CP.PropsSI('T', 'P', p[17], 'H', h[17], 'Water')
        d[17] = CP.PropsSI('D', 'P', p[17], 'H', h[17], 'Water')
        s[17] = CP.PropsSI('S', 'P', p[17], 'H', h[17], 'Water')  

    except ValueError:
        raise(Error("Os parâmetros de entrada fornecidos não estão no domínio de validade das correlações utilizadas para os cálculos das propriedades termodinâmicas."))
    
    
    ##########################################
    ########## CÁLCULOS POSTERIORES ##########
    ##########################################
    
    # Bagaço produzido
    bp = tm * fb
    
    # Taxa de calor fornecido à caldeira
    Qc = m[1]*(h[1] - h[17]) / nc / 10**6
    
    # Bagaço consumido
    bc = Qc / pci / 10**3 * 3600
    
    # Bagaço excedente
    be = bp - bc
    
    # Taxa de calor perdido para o ambiente
    Qa = Qc*(1-nc) + m[1]*(h[1] - h[2]) / 10**6
    
    # Taxa de calor fornecido ao processo
    Qp = m[14]*(h[14] - h[15]) / 10**6
    
    # Taxa de calor removido no condensador
    Qcd = m[6]*(h[6] - h[7]) / 10**6
    
    # Geração de energia na Turbina 1
    Wt1 = m[3]*(h[3] - h[4]) / 10**6
    
    # Geração de energia na Turbina 2
    Wt2 = m[5]*(h[5] - h[6]) / 10**6
    
    # Geração total das turbinas
    Wt = Wt1 + Wt2
    
    # Consumo de energia na Bomba 1
    Wb1 = m[7]*(h[8] - h[7]) / 10**6
    
    # Consumo de energia na Bomba 2
    Wb2 = m[16]*(h[17] - h[16]) / 10**6
    
    # Consumo total de energia nas bombas
    Wb = Wb1 + Wb2
    
    # Geração líquida de potência
    Wl = Wt - Wb
    
    # Consumo do processo
    Wp = tm * ce / 1000
    
    # Excedente comercializável de potência
    We = Wl - Wp
    

    ###########################################
    ########## ÍNDICES DE DESEMPENHO ##########
    ###########################################
    
    # FUE
    FUE = (Wl + Qp)/(Qc)
    
    # IPE
    n_term_ref = 0.4
    n_cald_ref = 0.77
    IPE = Qc / (Wl / n_term_ref + Qp / n_cald_ref)
    
    # EEC
    EEC = 1 - IPE
    
    # IGP
    IGP = Wl / (Qc - Qp/nc)
    
    # RPC
    RPC = Wl / Qp
    
    #############################
    ########## OUTPUTS ##########
    #############################
    
    # Conversões
    m = list(map(lambda x: x * 3.6, m[1:]))
    p = list(map(lambda x: x / 10**5, p[1:]))
    T = list(map(lambda x: x - 273.15, T[1:]))
    v = list(map(lambda x: 1/x, d[1:]))
    h = list(map(lambda x: x / 10**3, h[1:]))
    s = list(map(lambda x: x / 10**3, s[1:]))
    
    df = pd.DataFrame()
    df['m [t/h]'] = m
    df['p [bar]'] = p
    df['T [oC]'] = T
    df['v [m³/kg]'] = v
    df['h [kJ/kg]'] = h
    df['s [kJ/kg.K]'] = s
    df.index = range(1,18)
    
    results = [bp, bc, be, Qc, Qa, Qp, Qcd, Wt1, Wt2, Wb1, Wb2, Wl, Wp, We, FUE, IPE, EEC, IGP, RPC]
    
    
    return results, df