from nicegui import ui
from P001 import p001_ui
from P002 import p002_ui

class Problem:
    def __init__(self):
        self.number = 1

def gen_dict(a, b):
    return dict(map(lambda x: (x, str(x)),range(a, b + 1)))

def show_problem(problem_number):
    problem.visible = problem_number > 0
    
    p001_ui.show_ui(problem_number == 1)
    p002_ui.show_ui(problem_number == 2)

    
problem = Problem()

with ui.row():
    with ui.column():
        ui.label('Select a problem:')
        problems = gen_dict(1, 50)
        ui.select(problems, on_change=lambda e: show_problem(e.value)).bind_value(problem, 'number')
        ui.separator()


ui.run(port=80)