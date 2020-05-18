import PySimpleGUI as sg

layout = [
    [sg.Text("Text")],
    [sg.Button("Quit")]
]
window = sg.Window("Title", layout)
while True:
    event, values = window.read()
    if event == "Quit":
        break
