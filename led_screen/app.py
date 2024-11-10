from tkinter import Frame
from pages import TelaInicial
from warnings_robot import Warnings

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Unidade de Entrega")
        self.root.geometry("800x500")  # Ajuste conforme necessário

        self.perigos = Warnings(self)
        
        # Iniciar com a primeira página
        self.current_page = None
        self.show_page(TelaInicial)

    def show_page(self, page_class):
        """Troca para uma nova página."""
        if self.current_page is not None:
            self.current_page.destroy()
        
        # Inicializa e exibe a nova página
        self.current_page = page_class(self.root, self)
        self.current_page.pack(fill="both", expand=True)
