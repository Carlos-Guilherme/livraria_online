from PySimpleGUI import PySimpleGUI as sg
from pygame import WINDOWCLOSE
import webbrowser
    
def validate():
    sg.theme('reddit')
    result = [
        [sg.Text('Usuário', size = (8)), sg.Input(key='usuario', size = (30, 100))],
        [sg.Text('Senha', size = (8)), sg.Input(key='senha', password_char='*', size = (30, 100))],
        [sg.Text('')]
    ]

    layout_login = [
        [sg.Frame('LOGIN', layout = result, key = 'container')],
        [sg.Button('Entrar', size = (40))]
    ]
    return sg.Window('Login', layout = layout_login, finalize = True)
janela = validate()

def links_para_livros(): #trazer essa seção para uma nova janela e colocar uma ação ao clicar cada botão
    linha = [
        [sg.Text('Livros de Filosofia')],
        [sg.Button('ACESSAR 1', size = (35))],
        [sg.Text('Livros de Tecnologia')],
        [sg.Button('ACESSAR 2', size = (35))],
        [sg.Text('Livros de Inglês')],
        [sg.Button('ACESSAR 3', size = (35))],
        [sg.Text('Livros de Astronomia')],
        [sg.Button('ACESSAR 4', size = (35))],
        [sg.Text('Livros de Fisica')],
        [sg.Button('ACESSAR 5', size = (35))],
        [sg.Text('')]
        ]
    layout = [
        [sg.Frame('LINKS PARA LIVROS', layout = linha, key = 'container', size = (300, 400))],
    ]
    return sg.Window('Links', layout = layout, finalize = True)

tentativas = 3
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Entrar':
        if valores['usuario'] == 'carlos' and valores['senha'] == '123':
            janela.extend_layout(janela['container'], [[sg.Text('ACESSO APROVADO!')]])
            janela.close()
            janela = links_para_livros()
            while True:
                eventos2, valores2 = janela.read()
                if eventos2 == sg.WINDOW_CLOSED:
                    break
                elif eventos2 == 'ACESSAR 1':
                    webbrowser.open('www.google.com')
                elif eventos2 == 'ACESSAR 2':
                    webbrowser.open('www.google.com')
                elif eventos2 == 'ACESSAR 3':
                    webbrowser.open('www.google.com')
                elif eventos2 == 'ACESSAR 4':
                    webbrowser.open('www.google.com')
                elif eventos2 == 'ACESSAR 5':
                    webbrowser.open('www.google.com')
        elif valores['usuario'] != 'carlos' and valores['senha'] != '123':
            tentativas -= 1
            janela.extend_layout(janela['container'], [[sg.Text(f'usuário ou senha inválidos, tentativas restantes {tentativas}')]])
            if tentativas == 0:
                break
                
                
