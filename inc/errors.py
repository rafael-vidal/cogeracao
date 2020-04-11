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


import tkinter.messagebox as tkMessageBox

class Error(Exception):

    def __init__(self, message):
        self.message = message
        tkMessageBox.showerror("Erro", self.message)
        pass