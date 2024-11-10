from tkinter import messagebox

class Warnings:
    def __init__(self, app):
        self.app = app  # Referência ao aplicativo principal para acesso ao root
    
        self.avisos = {
            "t": "Temperatura acima do limite.",
            "p": "Compartimento aberto, por favor feche antes de concluir.",
            "q": "Tropecei no caminho, minha localidade foi enviada para o aplicativo.",
            "b": "Bateria fraca, verifique meu carregamento."
            # Adicione outros avisos e teclas conforme necessário
        }
        # Captura de eventos de teclado em toda a janela principal
        self.app.root.bind_all("<KeyPress>", self.verificar_tecla)

    def verificar_tecla(self, event):
        """ Exibe uma mensagem de aviso com base na tecla pressionada """
        # Obtém o caractere da tecla pressionada e verifica se existe um aviso para essa tecla
        aviso = self.avisos.get(event.char)
        if aviso:
            messagebox.showwarning("Aviso de Perigo", aviso)