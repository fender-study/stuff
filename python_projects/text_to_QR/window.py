from tkinter import *
from tkinter import messagebox
import os
import qrcode

PATH = "image.png"


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("QR image generator")
        self.config(padx=50, pady=50)

        self.label = Label(text="Enter text here:")
        self.label.pack()

        self.entry = Entry(width=50)
        self.entry.pack()

        self.generate_button = Button(text="Generate QR", width=25, command=self.show_qr)
        self.generate_button.pack()

        self.exit_button = Button(text="Exit", width=25, command=self.exit)
        self.exit_button.pack()

        self.mainloop()

    def generate_qr(self):
        data = self.entry.get()
        qr_code = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_code.add_data(data)
        qr_code.make(fit=True)
        qr_img = qr_code.make_image(fill_color="black", back_color="white")
        qr_img.save(PATH)
        qr_image = PhotoImage(file=PATH)
        return qr_image, qr_code.modules_count

    def show_qr(self):
        if self.not_empty():
            qr_image, qr_size = self.generate_qr()

            new_window = Toplevel(self)
            new_window.title("QR code ({0}x{0})".format(qr_size))
            new_window.config(padx=20, pady=20)

            canvas = Canvas(new_window, height=500, width=500)
            canvas.pack()
            canvas.create_image(250, 250, image=qr_image)

            def close_window():
                new_window.destroy()
                os.remove(PATH)

            optional_button = Button(new_window, text="Exit", width=20, command=close_window)
            optional_button.pack()

            new_window.mainloop()
        else:
            messagebox.showinfo("No text provided.", "Please provide some data to generate QR code.")

    def exit(self):
        self.destroy()

    def not_empty(self):
        if len(self.entry.get()) == 0:
            return False
        else:
            return True
