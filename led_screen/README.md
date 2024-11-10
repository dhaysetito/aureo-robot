![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Licença](https://img.shields.io/badge/licença-GPL--3.0-red)
![Última Atualização](https://img.shields.io/github/dhaysetito/aureo-robot)

# Aplicação de Unidade de Entrega

Este projeto é uma interface gráfica de monitoramento e alerta para uma aplicação de unidades de entrega, desenvolvida com Python e Tkinter. Ele exibe várias páginas de interação, incluindo uma página inicial, uma interface de entrada de unidade, e alertas visuais para possíveis perigos.

## Estrutura do Projeto

O projeto é organizado nos seguintes arquivos:

- **main.py**: Inicia a aplicação e exibe a janela principal.
- **app.py**: Define a classe principal `App`, responsável por gerenciar as páginas da aplicação.
- **pages.py**: Define as várias páginas (`Frame`s) que compõem a interface do usuário, incluindo:
  - `TelaInicial`: Página inicial com logo e navegação para a página de entrada.
  - `UnidadeEntregaPage`: Página para inserir a unidade de entrega usando um teclado numérico.
  - `CompartimentoPage`: Página para confirmar a entrega no compartimento.
  - `ConfirmacaoEntreguePage`: Página de confirmação de entrega com uma animação GIF.
- **warnings_robot.py**: Define a classe `Warnings` para exibir alertas de aviso ao pressionar teclas específicas.

## Funcionalidades

1. **Interface gráfica com várias páginas**:
   - A aplicação consiste em várias páginas, navegáveis, cada uma com um propósito específico.
   
2. **Alertas de Aviso**:
   - O programa exibe mensagens de alerta quando certas teclas são pressionadas.
   - Por exemplo, ao pressionar "T", um alerta avisa sobre uma temperatura acima do limite, e ao pressionar "P", um alerta informa sobre o compartimento aberto.

3. **Animação de GIF na página de confirmação**:
   - A página de confirmação exibe um GIF animado para indicar uma entrega bem-sucedida.

## Classes Principais

### `App` (app.py)

A classe principal `App` é responsável por:
- Inicializar e exibir a janela principal do Tkinter.
- Gerenciar a transição entre as diferentes páginas da interface.
- Instanciar a classe `Warnings` para ativar os alertas de aviso ao pressionar teclas.

### `Warnings` (warnings_robot.py)

A classe `Warnings` exibe mensagens de alerta com base em teclas pressionadas. Ela monitora as teclas "T" e "P" e exibe uma `messagebox` de aviso quando detecta um possível perigo.

### `TelaInicial`, `UnidadeEntregaPage`, `CompartimentoPage`, `ConfirmacaoEntreguePage` (pages.py)

Estas classes são responsáveis por diferentes telas da aplicação:

- **TelaInicial**: Página de boas-vindas com o logotipo. Ao clicar nela, o usuário é levado à página de entrada de unidade.
- **UnidadeEntregaPage**: Página para inserir a unidade de entrega usando um teclado numérico. Após inserir o valor, o usuário pode confirmar e ir para a próxima página.
- **CompartimentoPage**: Página de confirmação para garantir que o item foi colocado no compartimento.
- **ConfirmacaoEntreguePage**: Página de confirmação final que exibe uma animação de GIF e um botão para retornar à tela inicial.


## Pré-requisitos

- Python 3.x
- Bibliotecas:
  - `tkinter`: Incluída na instalação padrão do Python.
  - `Pillow`: Para manipulação e exibição de imagens e GIFs. Instale-a com:
    ```bash
    pip install pillow
    ```

## Estrutura de Diretórios

A estrutura esperada dos arquivos é a seguinte:

```
.
├── app.py
├── main.py
├── pages.py
├── warnings_robot.py
└── imagens
    ├── blinking.gif         
    └── logo_aureo2.png      
```

**Nota**: Certifique-se de que os arquivos de imagem estão no diretório `imagens`, conforme especificado nos caminhos do código.

## Como Executar

1. **Clone ou baixe o repositório**.
2. **Navegue até o diretório `led_screen`**.
3. **Instale as dependências** usando o `pip` (apenas `Pillow` é necessário).
4. **Execute o programa** com o comando:
   ```bash
   python main.py
   ```

## Funcionamento

- A aplicação começa na `TelaInicial`.
- Clicar na tela inicial leva o usuário à `UnidadeEntregaPage`, onde ele pode inserir a unidade de entrega.
- Após inserir o valor e clicar em "Enter", o usuário é levado à `CompartimentoPage`.
- Na `CompartimentoPage`, o usuário confirma a entrega clicando em "Enter", o que leva à `ConfirmacaoEntreguePage`.
- A `ConfirmacaoEntreguePage` exibe uma animação GIF e, após 10 segundos, retorna à `TelaInicial`.

## Exemplo de Uso

Durante o uso, pressione as teclas para ver os avisos:
- **Tecla T**: Exibe "Temperatura acima do limite."
- **Tecla P**: Exibe "Compartimento aberto, por favor feche antes de concluir."

## Personalização

Para adicionar mais alertas, edite o dicionário `avisos` na classe `Warnings` em `warnings_robot.py`:

```python
self.avisos = {
    "t": "Temperatura acima do limite.",
    "p": "Compartimento aberto, por favor feche antes de concluir.",
    "f": "Falha no sistema detectada."  # Exemplo adicional
}
```

## Observações

- Certifique-se de que as imagens necessárias estão no caminho correto.
- O GIF na página de confirmação pode ser substituído por outra animação alterando o caminho em `ConfirmacaoEntreguePage` na função `animate_gif`.
