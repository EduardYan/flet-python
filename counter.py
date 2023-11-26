import flet as ft
import time


def main(page: ft.Page):

    page.title = "Mi contador con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_number = ft.TextField(
        value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus(e):
        text_number.value = str(int(text_number.value) - 1)
        text_number.update()

    def plus(e):
        text_number.value = str(int(text_number.value) + 1)
        text_number.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=plus),
                ft.ElevatedButton(text = "Say my name")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    # for i in range(100):
    #     text_number.value = f"Setp {i}"
    #     text_number.update()
    #     time.sleep(1)


ft.app(main)
