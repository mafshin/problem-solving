from nicegui import ui
from P001.p001 import *
from P002.p002 import add, divide, multiply, subtract

class Options:
    def __init__(self):
        self.visible = False 
        self.first = True

options = Options()

def show_ui(visible):
    options.visible = visible
    if options.first:
        options.first = False
        create_ui()
    
def create_ui():
    with ui.column().bind_visibility_from(options, 'visible') as root:
        numberInput1 = ui.input('Number 1')
        numberInput2 = ui.input('Number 2')
        with ui.row():
            ui.button('+', on_click=lambda e: calculate(e))
            ui.button('-', on_click=lambda e: calculate(e))
            ui.button('/', on_click=lambda e: calculate(e))
            ui.button('*', on_click=lambda e: calculate(e))
        output = ui.label()

    def calculate(e):
        operation = e.sender.text
        number1 = int(numberInput1.value)
        number2 = int(numberInput2.value)

        if operation == '+':
            result = add(number1, number2)
        elif operation == '-':
            result = subtract(number1, number2)
        elif operation == '/':
            result = divide(number1, number2)
        elif operation == '*':
            result = multiply(number1, number2)

        output.text = result

if __name__ in {"__main__", "__mp_main__"}:
    show_ui(True)
    ui.run()