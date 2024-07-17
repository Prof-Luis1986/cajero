import flet as ft

# Se declaran las variables iniciales
salfo_i = 1000
salfo_f = salfo_i

def main(page: ft.Page):
    # Se configura la página
    page.window.height = 600
    page.window.width = 400
    page.title = "Banco CETIS 50"
    page.padding = 20
    page.bgcolor = "green"
    
    label = ft.Text(
        "Bienvenido al Banco CETIS 50", 
        size=20, 
        weight=ft.FontWeight.BOLD
    )
    page.controls.append(label)
    
    btnDeposito = ft.ElevatedButton(
        text="Depositar",
        on_click=lambda e: deposito(page),
        color=ft.colors.RED,
        bgcolor=ft.colors.YELLOW_500
    )
    page.controls.append(btnDeposito)
    
    btnConsultar = ft.ElevatedButton(
        text="Consultar Saldo",
        on_click=lambda e: consultar(page),
        color=ft.colors.RED,
        bgcolor=ft.colors.YELLOW_500
    )
    page.controls.append(btnConsultar)
    
    btnRetirar = ft.ElevatedButton(
        text="Retirar",
        on_click=lambda e: retiro(page),
        color=ft.colors.RED,
        bgcolor=ft.colors.YELLOW_500    
    )
    page.controls.append(btnRetirar)
    
    btnSalir = ft.ElevatedButton(
        text="Salir",
        on_click=lambda e: salir(page),
        color=ft.colors.RED,
        bgcolor=ft.colors.YELLOW_500
    )
    page.controls.append(btnSalir)
    
    # Agregar imagen
    img_path = "https://i.ibb.co/njrp100/cajero.png"
    image = ft.Image(src=img_path, width=400, height=300)
    
    page.controls.append(image)
    page.update()
    
def deposito(page: ft.Page):
    def on_submit(e):
        global salfo_f
        deposito = float(input_box.value)
        salfo_f = salfo_f + deposito
        dialog.open = False
        page.update()
        page.snack_bar = ft.SnackBar(ft.Text("Depósito exitoso"))
        page.snack_bar.open = True
        page.update()
        
    input_box = ft.TextField(
        label="Ingrese su depósito",
        autofocus=True,
    )
    dialog = ft.AlertDialog(
        title=ft.Text("Depósito"),
        content=input_box,
        actions=[
            ft.TextButton("Ok", on_click=on_submit),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Diálogo cerrado")
    )
    page.overlay.append(dialog)
    dialog.open = True
    page.update()
    
def consultar(page: ft.Page):
    global salfo_f
    def close_dialog(e):
        dialog.open = False
        page.update()
        
    dialog = ft.AlertDialog(
        title=ft.Text("Consulta tu Saldo"),
        content=ft.Text(f"Su saldo es: {salfo_f}"),
        actions=[
            ft.TextButton("Ok", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(dialog)
    dialog.open = True
    page.update()
    
def retiro(page: ft.Page):
    def on_submit(e):
        global salfo_f
        retiro = float(input_box.value)
        if retiro > salfo_f:
            dialog.open = False
            page.snack_bar = ft.SnackBar(ft.Text("Saldo insuficiente"))
            page.snack_bar.open = True
            page.update()
        else:
            salfo_f = salfo_f - retiro
            dialog.open = False
            page.snack_bar = ft.SnackBar(ft.Text("Retiro exitoso"))
            page.snack_bar.open = True
            page.update()
            
    input_box = ft.TextField(
        label="Ingrese la cantidad a retirar",
        autofocus=True
    )
    dialog = ft.AlertDialog(
        title=ft.Text("Retiro"),
        content=input_box,
        actions=[
            ft.TextButton("Ok", on_click=on_submit),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Diálogo cerrado")
    )
    page.overlay.append(dialog)
    dialog.open = True
    page.update()
    
def salir(page: ft.Page):
    page.window.close()
    
#ft.app(target=main)
ft.app(target=main,view=ft.WEB_BROWSER)