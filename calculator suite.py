import flet as ft

def main(page):
    page.title = "My Calculator App calculation suite"
    page.padding = 10

    number1 = ft.TextField(label="First Number")
    number2 = ft.TextField(label="Second Number")
    math_result = ft.Text("Waiting...", size=20)

    def do_math(e):
        try:
            a = float(number1.value)
            b = float(number2.value)
            if e.control.text == "+":
                math_result.value = f"= {a + b}"
            elif e.control.text == "-":
                math_result.value = f"= {a - b}"
            elif e.control.text == "×":
                math_result.value = f"= {a * b}"
            elif e.control.text == "÷":
                math_result.value = f"= {a / b}"
        except:
            math_result.value = "Oops! Enter numbers"
        page.update()

    tab1 = ft.Tab(
        text="Math",
        content=ft.Column([
            ft.Text("Basic Calculator", size=20),
            number1,
            number2,
            ft.Row([
                ft.ElevatedButton("+", on_click=do_math),
                ft.ElevatedButton("-", on_click=do_math),
                ft.ElevatedButton("×", on_click=do_math), 
                ft.ElevatedButton("÷", on_click=do_math)
            ]),
            math_result
        ])
    )

    weight = ft.TextField(label="Your Weight (kg)")
    height = ft.TextField(label="Your Height (m)")
    bmi_result = ft.Text("Your BMI will show here", size=20)

    def calc_bmi(e):
        try:
            w = float(weight.value)
            h = float(height.value)
            bmi_result.value = f"BMI: {w/(h*h):.1f}"
        except:
            bmi_result.value = "Enter numbers please!"
        page.update()

    tab2 = ft.Tab(
        text="BMI",
        content=ft.Column([
            ft.Text("BMI Calculator", size=20),
            weight,
            height,
            ft.ElevatedButton("Calculate BMI", on_click=calc_bmi),
            bmi_result
        ])
    )

    amount = ft.TextField(label="Amount")
    unit_from = ft.Dropdown(options=["cm","inches","kg","lbs"], value="cm")
    unit_to = ft.Dropdown(options=["cm","inches","kg","lbs"], value="inches")
    unit_result = ft.Text("Converted amount", size=20)

    def convert_units(e):
        try:
            val = float(amount.value)
            if unit_from.value == "cm" and unit_to.value == "inches":
                unit_result.value = f"= {val/2.54:.2f} inches"
            elif unit_from.value == "inches" and unit_to.value == "cm":
                unit_result.value = f"= {val*2.54:.2f} cm"
            elif unit_from.value == "kg" and unit_to.value == "lbs":
                unit_result.value = f"= {val*2.2:.2f} lbs"
            elif unit_from.value == "lbs" and unit_to.value == "kg":
                unit_result.value = f"= {val/2.2:.2f} kg"
            else:
                unit_result.value = "Pick different units"
        except:
            unit_result.value = "Enter a number!"
        page.update()

    tab3 = ft.Tab(
        text="Units",
        content=ft.Column([
            ft.Text("Unit Converter", size=20),
            amount,
            ft.Row([ft.Text("From:"), unit_from]),
            ft.Row([ft.Text("To:"), unit_to]),
            ft.ElevatedButton("Convert", on_click=convert_units),
            unit_result
        ])
    )

    all_tabs = ft.Tabs(tabs=[tab1, tab2, tab3])
    page.add(all_tabs)

ft.app(target=main)