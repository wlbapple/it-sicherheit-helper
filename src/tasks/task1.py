import PySimpleGUI as sg


def calc(urn1r, urn1b, urn2r, urn2b, prob1, prob2, event):
    urn1 = urn1r + urn1b
    urn2 = urn2b + urn2r
    n = 0
    pru1a = 1
    pru1b = 1
    pru2a = 1
    pru2b = 1
    for draw in event:
        if n == len(event)-1:
            if draw == 'R':
                pru1a *= urn1r/urn1
                pru2a *= urn2r/urn2
                urn2 -= 1
                urn2r -= 1
                urn1 -= 1
                urn1r -= 1
            else:
                pru1a *= urn1b/urn1
                pru2a *= urn2b/urn2
                urn1 -= 1
                urn1b -= 1
                urn2 -= 1
                urn2b -= 1
        else:
            if draw == 'R':
                pru1a *= urn1r/urn1
                pru1b *= urn1r/urn1
                pru2a *= urn2r/urn2
                pru2b *= urn2r/urn2
                urn1 -= 1
                urn1r -= 1
                urn2 -= 1
                urn2r -= 1
            else:
                pru1a *= urn1b/urn1
                pru1b *= urn1b/urn1
                pru2a *= urn2b/urn2
                pru2b *= urn2b/urn2
                urn1 -= 1
                urn1b -= 1
                urn2 -= 1
                urn2b -= 1
        n += 1
    result = ((pru1a*prob1)+(pru2a*prob2))/((pru1b*prob1)+(pru2b*prob2))
    return result


def create_task1():
    # create task1 layoutUrn experiment
    layout = [
        [sg.Text('Urns experiment')],
        [sg.Input('Amount Urn1 red', key='-URN1R-'),
         sg.Input('Amount Urn1 black', key='-URN1B-')],
        [sg.Input('Amount Urn2 red', key='-URN2R-'),
         sg.Input('Amount Urn2 black', key='-URN2B-')],
        [sg.Input('Event?(BBR?)', key='-EVENT-')],
        [sg.Input('probability urn1', key='-PROB1-')],
        [sg.Input('probability urn2', key='-PROB2-')],
        [sg.Button('Submit')],
        [sg.InputText('Result!', key='-RESULT-',use_readonly_for_disable=True)],
        [sg.Button('finish')]
    ]
    # create window for the task
    window_task1 = sg.Window('2 Urn experiment', layout, size=(800, 600))

    while True:
        event, values = window_task1.read()
        if event in (None, 'finish'):
            break
        elif event == 'Submit':
            urn1r = float(values['-URN1R-'])
            urn1b = float(values['-URN1B-'])
            urn2r = float(values['-URN2R-'])
            urn2b = float(values['-URN2B-'])
            event = str(values['-EVENT-'])
            prob1 = float(values['-PROB1-'])
            prob2 = float(values['-PROB2-'])
            result = calc(urn1r, urn1b, urn2r, urn2b, prob1, prob2, event)
            window_task1['-RESULT-'].update(result)

    window_task1.close()
