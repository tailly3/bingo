import random
import PySimpleGUI as sg

chose_numbers = []
chose = 0

def btn():
    while True:
        global chose
        chose = random.randint(1,75)
        if chose not in chose_numbers:
            chose_numbers.append(chose)
            break
    
layout = [[sg.Text("ビンゴ司会システム")], 
          [sg.Button("実行", key="-start-")],
          [sg.Text(key="-kazu1-", font=("Arial",50))],
          [sg.Text("選ばれた数")],
          [sg.Text(key="-kazu2-")]]
window = sg.Window("ビンゴ数生成", layout, size=(600, 600))

while True:
    event, values = window.read()
    if event == "-start-":
        btn()
        window["-kazu1-"].update(value=f"{chose}")    
        window["-kazu2-"].update(value=f"{chose_numbers}")
            
    if event == sg.WIN_CLOSED:
        break
