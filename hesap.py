import tkinter as tk

class HesapMakinesi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hesap Makinesi")
        self.geometry("300x400")

        self.result = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result, font=("Arial", 24), justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, font=("Arial", 18), width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.result.set('')
        elif button == '=':
            try:
                expression = self.result.get()
                result = str(eval(expression))
                self.result.set(result)
            except Exception:
                self.result.set('Hata')
        else:
            current_expression = self.result.get()
            new_expression = current_expression + button
            self.result.set(new_expression)

if __name__ == "__main__":
    app = HesapMakinesi()
    app.mainloop()
