import PySimpleGUI as sg
from tasks import task1,task2,task3



# layout for home Window
sg.theme('DarkBlue')
layout = [
    [sg.Text('This is a program for the IT-Security lecture')],
    [sg.Button('Urns experiment'), sg.Button(
        'OTP'), sg.Button('Padding'), sg.Button('AES-CBC-Block')],
    [sg.Button('close')]
]

# create Home Window
window = sg.Window('Home', layout, size=(800, 600))

# Eventloop for calling the different tasks
while True:
    event, values = window.read()
    # end the program if the window get's closed    
    if event in (None, 'close'):
        break
    elif event == 'Urns experiment':
        task1.create_task1()
    elif event == 'OTP':
        task2.create_task2()
    elif event == 'Padding':
        task3.create_task3()
window.close()
