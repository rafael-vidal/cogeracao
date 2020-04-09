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

from tkinter import *
from tkinter import ttk
import os
from inc.Ciclo import ciclo
from inc.Grafico import graphic
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from inc.desenho_1 import desenho_1
from inc.desenho_2 import desenho_2
from inc.cogeracao import cogeracao
import CoolProp.CoolProp as CP


if __name__ == '__main__':
    cogeracao()
       