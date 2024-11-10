import tkinter as tk
from tkinter import Frame, Label, Entry, Button, font, messagebox
from PIL import Image, ImageTk


class TelaInicial(Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.pack(fill="both", expand=True)  # Preenche a tela com a imagem

        # Carregar e exibir a imagem do logo
        self.load_logo()

        # Evento de clique em qualquer lugar para ir para a próxima página
        self.bind("<Button-1>", self.ir_para_unidade_entrega)

    def load_logo(self):
        """ Carrega e exibe a imagem do logo grande na tela inicial """
        try:
            # Carregar a imagem do logo
            logo_image = Image.open("imagens/logo_aureo2.png")  # Altere o caminho para a sua imagem
            logo_image = logo_image.resize((500, 500), Image.LANCZOS)  # Redimensiona a imagem se necessário
            logo_photo = ImageTk.PhotoImage(logo_image)

            # Exibe a imagem no centro da tela
            logo_label = Label(self, image=logo_photo)
            logo_label.image = logo_photo  # Mantém a referência da imagem
            logo_label.pack(expand=True)  # Centraliza a imagem na tela

            logo_label.bind("<Button-1>", self.ir_para_unidade_entrega)

        except Exception as e:
            print(f"Erro ao carregar o logotipo: {e}")

    def ir_para_unidade_entrega(self, event):
        """ Vai para a página UnidadeEntregaPage ao clicar na tela """
        print("Clicou na tela!")  # Adicionei um print para verificar se o clique está sendo capturado
        self.app.show_page(UnidadeEntregaPage)

class UnidadeEntregaPage(Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app  # Referência ao aplicativo principal para trocar de página
        self.unidade_entrega = None

        # Configuração de fonte
        titulo_font = font.Font(family="Helvetica", size=14, weight="bold")
        
        # Logotipo "Aureo"
        self.load_logo()

        # Título
        titulo_label = Label(self, text="INFORME A UNIDADE DE ENTREGA", font=titulo_font)
        titulo_label.pack(pady=(10, 5))

        # Caixa de entrada
        self.entry = Entry(self, width=10, font=("Helvetica", 16), justify="center")
        self.entry.pack(pady=10)

        # Frame para o teclado numérico
        keypad_frame = Frame(self)
        keypad_frame.pack(pady=10)

        # Criar botões do teclado numérico
        buttons = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [0]
        ]
        for i, row in enumerate(buttons):
            for j, num in enumerate(row):
                button = Button(keypad_frame, text=str(num), width=5, height=2, 
                                   command=lambda num=num: self.on_button_click(num))
                button.grid(row=i, column=j, padx=5, pady=5)

        # Botão Enter para salvar o valor e mudar de página
        enter_button = Button(self, text="Enter", width=10, height=2, command=self.salvar_e_navegar)
        enter_button.pack(pady=10)

    def load_logo(self):
        """ Carrega e exibe o logotipo na interface """
        try:
            # Carregar a imagem do logotipo
            logo_image = Image.open("imagens/logo_aureo2.png")  # Caminho para o logotipo
            logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Redimensiona, se necessário
            logo_photo = ImageTk.PhotoImage(logo_image)
            
            # Label para exibir a imagem
            logo_label = Label(self, image=logo_photo)
            logo_label.image = logo_photo  # Armazena uma referência da imagem para não ser removida pelo garbage collector
            logo_label.pack(pady=(10, 5))
        except Exception as e:
            print(f"Erro ao carregar o logotipo: {e}")

    def on_button_click(self, numero):
        """ Adiciona o número clicado na caixa de entrada """
        self.entry.insert(tk.END, str(numero))

    def salvar_e_navegar(self):
        """ Salva o valor da unidade de entrega e muda para a próxima página """
        self.unidade_entrega = self.entry.get()
        print("Unidade de entrega salva:", self.unidade_entrega)
        self.entry.delete(0, tk.END)  # Limpa a entrada após salvar

        # Navega para a próxima página
        self.app.show_page(CompartimentoPage)

class CompartimentoPage(Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app  # Referência ao aplicativo principal para voltar ou avançar
        
        # Centraliza o conteúdo vertical e horizontalmente usando pack
        self.pack(fill="both", expand=True)

        # Exemplo de conteúdo para a próxima página
        label = Label(self, text="Coloque a entrega dentro do compartimento e ao finalizar clique no botão abaixo.", 
                    font=("Helvetica", 16),
                    wraplength=300)
        # Centraliza verticalmente e horizontalmente
        label.pack(pady=20, fill="y", expand=True)

        # Botão de Enter para ir para a página de confirmação
        enter_button = Button(self, text="Enter", width=10, height=2, command=self.navegar_confirmacao)
        enter_button.pack(pady=20, expand=True)

    def navegar_confirmacao(self):
        """ Navega para a página de confirmação de entrega """
        self.app.show_page(ConfirmacaoEntreguePage)

class ConfirmacaoEntreguePage(Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app  # Referência ao aplicativo principal para voltar ou avançar
        
        # Exemplo de conteúdo para a página de confirmação
        label = Label(self, text="Entrega confirmada!", font=("Helvetica", 16))
        label.pack(pady=20, expand=True)

        try:
            # Carregar a imagem de piscar
            self.blinking_image = Image.open("imagens/blinking.gif")  # Caminho do GIF animado

            # Cria um rótulo para exibir a animação
            self.blinking_label = Label(self)
            self.blinking_label.pack(expand=True)  # Centraliza a imagem na tela

            # Inicia a animação
            self.animate_gif(0)

        except Exception as e:
            print(f"Erro ao carregar o blinking: {e}")

        # Botão de Enter para ir para a página de confirmação
        enter_button = Button(self, text="Tela inicial", width=10, height=2, command=self.voltar)
        enter_button.pack(pady=20, expand=True)

        # Definir um atraso de 10 segundos para voltar automaticamente para a página de confirmação
        self.after(10000, self.voltar)  # 10000 milissegundos = 10 segundos

    def animate_gif(self, index):
        """ Função para atualizar os quadros do GIF """
        try:
            # Move para o próximo quadro no GIF
            self.blinking_image.seek(index)
            frame = ImageTk.PhotoImage(self.blinking_image)
            self.blinking_label.config(image=frame)
            self.blinking_label.image = frame  # Mantém a referência para evitar limpeza do quadro

            # Programar para o próximo quadro
            self.after(300, self.animate_gif, (index + 1) % self.blinking_image.n_frames)
        except EOFError:
            pass

    def voltar(self):
        """ Volta para a página UnidadeEntregaPage """
        self.app.show_page(TelaInicial)
