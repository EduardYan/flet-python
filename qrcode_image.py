import flet as ft
import qrcode

def main(page: ft.Page):

  def btn_click(e):
    codigo_qr = qrcode.QRCode(
      version = 1,
      box_size = 10,
      border = 4
    )

    codigo_qr.add_data(texto.value)
    imagen_qr = codigo_qr.make_image(fill_color ="black", back_color = "white")
    imagen_qr.save("codigo_qr.png")

    imagen_col.controls.append(ft.Image(
      src=f"codigo_qr.png",
      width=400,
      height=400,
      fit = ft.ImageFit.CONTAIN
    ))

    page.update()


  texto = ft.TextField(label = "Texto a convertir")
  boton = ft.ElevatedButton("Generar", on_click=btn_click)
  imagen_col = ft.Column(expand = 1, wrap = False, scroll="AUTO")

  page.add(texto, boton, imagen_col)


ft.app(target = main)