import PySimpleGUI as sg

label_feet = sg.Text("Enter Feet: ", key="feet")
input_feet = sg.Input("", key="feet_input")
label_inches = sg.Text("Enter Inches: ", key="inches")
input_inches = sg.Input("", key="inches_input")
button_convert = sg.Button("Convert", key="conversion")
label_output = sg.Text("", key="output")

window = sg.Window("Convertor", layout=[[label_feet, input_feet], [label_inches, input_inches],
                                        [button_convert, label_output]])

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    feet = int(values['feet_input'])
    inches = int(values['inches_input'])
    output: float = float(feet * 0.3 + inches * 0.025)
    window["output"].update(value=f'{output} meters')

# You can use 1 ft = . 3 m and 1 in. = .025 m and multiply to convert manually
