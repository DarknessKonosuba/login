import PySimpleGUI as sg

# Tema de la interfaz
sg.theme('DarkPurple1')

# Función para validar el inicio de sesión
def iniciar_sesion(usuario, clave):
    inicio = False
    if(usuario == '' or clave == ''):
        sg.popup_error("Debes rellenar los campos")
        inicio = False
    else:
        if (usuario == 'moreno@gmail.com' and clave == '1234'):
            # si los datos son correctos se muestra un mensaje
            #sg.popup_ok('Usuario y Clave correctos')
            inicio = True
        else:
            # si los datos son incorrectos se muestra un mensaje
            sg.popup_error('Usuario o Clave incorrectos')
            inicio = False
    return inicio
            
# Defino una interfaz con una imagen, cajas de texto y botones.
layout = [
    [sg.Image(filename='login.png', pad=((95,0), (10,10)))],  # imagen
    [sg.Text('Usuario: ', size=(100, 1), justification='center')], # usuario
    [sg.InputText('', pad=((0,0), (0,0)), key='usuario')], # caja de texto usuario
    [sg.Text('Clave: ', size=(100, 1), justification='center')], # clave
    [sg.InputText('', password_char='*', key='clave')], # caja de texto clave y oculto con *
    [sg.Text(size=(0,0))], # espacio en blanco
    [sg.Button('Iniciar Sesión', size=(10,1), key='login'), sg.Button('Cancelar',size=(10,1), key='close')] # botones
]

# Cargo la ventana con la interfaz
window = sg.Window('Login', layout, size=(300, 300))

# Bucle principal
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif event == 'login':
        if iniciar_sesion(values['usuario'], values['clave']):
            # segunda ventana (Chat)
            layout2 = [
                [sg.Text('Correo: ',size=(10,1)), sg.Input('', key='-correo-')],
                [sg.Text(size=(0,0))], # espacio en blanco
                [sg.Text('Tu mensaje irá aquí: ')], 
                [sg.Multiline(size=(100,20), key='-mensaje-')],
                # [sg.Input('', size=(100, 400), font=('Arial', 10), key='-mensaje-', justification='center')],
                [sg.Text(size=(0,0))], # espacio en blanco
                [sg.Button('Enviar')],
            ]

            # Cargo la segunda ventana
            window2 = sg.Window('Chat', layout2, font=('Arial', 10), size=(500,500))
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED:
                break
            elif event2 == 'Enviar':
                mensaje = values2['-mensaje-']
                correo = values2['-correo-']
                sg.popup('Mensaje enviado a {}'.format(correo))
                # actualizo las cajas de texto para que queden en blanco
                window2.find_element('-mensaje-').update('')
                window2.find_element('-correo-').update('')
                window.find_element('usuario').update('')
                window.find_element('clave').update('')
    
        
    