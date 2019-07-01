"""
Pantalla principal de la aplicacion GymRutinas
@author Oscar Charro (oschariv)
"""

import PySimpleGUI as sg

# Creacion del Layout de la pantalla
layout = [
    [sg.Text('Pantalla principal', size=(30, 1), font=("Helvetica", 25))], # Titulo de la aplicacion 
    [sg.Text('Bienvenido a Gymrutinas, \nuna aplicacion donde podras gestionar tus rutinas.', size=(35, 3), font=("Helvetica", 12))] # Descripcion de la aplicacion
]

window = sg.Window('GymRutinas', default_element_size=(40, 1)).Layout(layout) # Asociamos el Layout a la ventana
button, values = window.Read() # Inicializamos la lectura de la pantalla (Necesario para que la pantalla se muestre)
