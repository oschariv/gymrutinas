"""
Clase pantalla principal,
Autor: Oscar Charro (oschariv)
Fecha: 26/06/2019
"""

import PySimpleGUI as sg

def iniciar_pantalla():
    # Creacion del Layout de la pantalla
    layout = [
        # Titulo de la aplicacion
        [sg.Text('Pantalla principal', size=(30, 1), font=("Helvetica", 25))],
        # Descripcion de la aplicacion
        [sg.Text('Bienvenido a Gymrutinas, \nuna aplicacion donde podras gestionar tus rutinas.', size=(35, 3), font=("Helvetica", 12))]
    ]

    window = sg.Window('GymRutinas', default_element_size=(40, 1)).Layout(layout) # Asociamos el Layout a la ventana
    button, values = window.Read()  # Inicializamos la lectura de la pantalla (Necesario para que la pantalla se muestre)
