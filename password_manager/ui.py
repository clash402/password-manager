from tkinter import *
from tkinter import messagebox
import pyperclip


class UI(Tk):
    def __init__(self, data_manager, password):
        super().__init__()

        self._data_manager = data_manager
        self._password = password

        self.title("Password Manager")
        self.config(padx=20, pady=20)

        self._draw()

    # DRAW METHODS
    def _draw(self):
        self._draw_canvas()
        self._draw_website_label()
        self._draw_username_label()
        self._draw_password_label()
        self._draw_website_input()
        self._draw_username_input()
        self._draw_password_input()
        self._draw_search_button()
        self._draw_generate_password_button()
        self._draw_add_button()

    # Canvas
    def _draw_canvas(self):
        self.logo_img = PhotoImage(file="./password_manager/resources/images/logo.png")
        canvas = Canvas(width=200, height=200)
        canvas.create_image(100, 100, image=self.logo_img)  # highlightthickness=0
        canvas.grid(column=1, row=0)

    # Labels
    def _draw_website_label(self):
        website_label = Label(text="Website:", font=("Arial", 16, "normal"))
        website_label.grid(column=0, row=1)

    def _draw_username_label(self):
        username_label = Label(text="Email/Username:", font=("Arial", 16, "normal"))
        username_label.grid(column=0, row=2)

    def _draw_password_label(self):
        password_label = Label(text="Password:", font=("Arial", 16, "normal"))
        password_label.grid(column=0, row=3)

    # Entries
    def _draw_website_input(self):
        self.website_input = Entry(width=21)
        self.website_input.grid(column=1, row=1)
        self.website_input.focus()

    def _draw_username_input(self):
        self.username_input = Entry(width=35)
        self.username_input.insert(0, "email@gmail.com")
        self.username_input.grid(column=1, row=2, columnspan=2)

    def _draw_password_input(self):
        self.password_input = Entry(width=21)
        self.password_input.grid(column=1, row=3)

    # Buttons
    def _draw_search_button(self):
        search_button = Button(text="Search", width=13, command=self._search_button_clicked, highlightthickness=0)
        search_button.grid(column=2, row=1)

    def _draw_generate_password_button(self):
        generate_password_button = Button(text="Generate Password", command=self._generate_password_button_clicked,
                                          highlightthickness=0)
        generate_password_button.grid(column=2, row=3)

    def _draw_add_button(self):
        add_button = Button(text="Add", width=36, command=self._add_button_clicked, highlightthickness=0)
        add_button.grid(column=1, row=4, columnspan=2)

    # CLEAR METHODS
    def _clear_entries(self):
        self.website_input.delete(0, END)
        self.password_input.delete(0, END)

    # EVENTS
    def _search_button_clicked(self):
        self._data_manager.find_website(self.website_input, messagebox)

    def _generate_password_button_clicked(self):
        password = self._password.generate()
        self.password_input.delete(0, END)
        self.password_input.insert(0, f"{password}")
        pyperclip.copy(password)

    def _add_button_clicked(self):
        self._data_manager.save(self.website_input, self.username_input, self.password_input, messagebox)
        self._clear_entries()
