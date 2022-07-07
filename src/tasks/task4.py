import binascii
import PySimpleGUI as sg
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
# AES CBC encrypter with fixed key and IV


def aesEncrypt(message, key, iv):
    message = message.encode()
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    print(iv, key, message)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(message, AES.block_size))
    ct = binascii.hexlify(ct_bytes).decode()
    return ct

# Funtion to get a certain ciphertexted Xor with a message snipet


def getInittext(ct, block, snipet):
    if block == 1:
        block = 0
    else:
        block *= 32
    print(block)
    initial = bytes.fromhex(ct[block: block+32])
    print(initial)
    snipet = snipet.encode()
    print(snipet)
    cto = []
    for counter, i in enumerate(snipet):
        cto.append(hex(i ^ initial[counter])[2:])
        print(cto)
    return ''.join(cto)


def create_task4():
    # create task2 layout OTP
    layout = [
        [sg.Text('Padding')],
        [sg.Input('Message', key='-MESSAGE-')],
        [sg.Input('IV', key='-IV-')],
        [sg.Input('Key', key='-KEY-')],
        [sg.Input('Block', key='-BLOCK-')],
        [sg.Input('Text-Snipet', key='-SNIPET-')],
        [sg.Button('Submit')],
        [sg.InputText('Result!', key='-RESULT-',
                      use_readonly_for_disable=True, size=600)],
        [sg.Button('finish')]
    ]
    # create window for the task
    window_task3 = sg.Window('Padding', layout, size=(1200, 600))

    while True:
        event, values = window_task3.read()
        if event in (None, 'finish'):
            break
        elif event == 'Submit':
            message = str(values['-MESSAGE-'])
            iv = str(values['-IV-'])
            key = str(values['-KEY-'])
            block = int(values['-BLOCK-'])
            snipet = str(values['-SNIPET-'])
            ct = aesEncrypt(message, key, iv)
            result = getInittext(ct, block, snipet)
            window_task3['-RESULT-'].update(result)
    window_task3.close()
