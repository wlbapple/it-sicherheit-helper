import PySimpleGUI as sg


def otp_encrypt(message, key):
    key = bytes.fromhex(key)
    message = message.encode()
    message = bytes(message)
    cipher = []
    for counter, i in enumerate(message):
        cipher.append(hex(i ^ key[counter])[2:])
    return ''.join(cipher)


def create_task2():
    # create task2 layout OTP
    layout = [
        [sg.Text('One Time Pad')],
        [sg.Input('Message to encrypt', key='-MESSAGE-')],
        [sg.Input('Key for OTP', key='-KEY-')],
        [sg.Button('Submit')],
        [sg.InputText('Result!', key='-RESULT-',use_readonly_for_disable=True)],
        [sg.Button('finish')]
    ]
    # create window for the task
    window_task2 = sg.Window('One Time Pad', layout, size=(800, 600))

    while True:
        event, values = window_task2.read()
        if event in (None, 'finish'):
            break
        elif event == 'Submit':
            message = str(values['-MESSAGE-'])
            key = str(values['-KEY-'])
            result = otp_encrypt(message, key)
            window_task2['-RESULT-'].update(result)
    window_task2.close()
