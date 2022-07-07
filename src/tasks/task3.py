import PySimpleGUI as sg
import binascii


def padding(message, block):
    if (len(message) % block) == 0:
        padding = 16
    else:
        padding = block - (len(message) % block)
    message = message.encode()
    message = binascii.hexlify(message).decode()
    for i in range(padding):
        message += hex(padding).replace("x", "")
    return message


def create_task3():
    # create task2 layout OTP
    layout = [
        [sg.Text("Padding")],
        [sg.Input("Message", key="-MESSAGE-")],
        [sg.Input("Block length", key="-LENGTH-")],
        [sg.Button("Submit")],
        [
            sg.InputText(
                "Result!", key="-RESULT-", use_readonly_for_disable=True, size=600
            )
        ],
        [sg.Button("finish")],
    ]
    # create window for the task
    window_task3 = sg.Window("Padding", layout, size=(1200, 600))

    while True:
        event, values = window_task3.read()
        if event in (None, "finish"):
            break
        elif event == "Submit":
            message = str(values["-MESSAGE-"])
            block = int(values["-LENGTH-"])
            result = padding(message, block)
            window_task3["-RESULT-"].update(result)
    window_task3.close()
