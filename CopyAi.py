import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import re

app = ttk.Window(themename="darkly")
app.title("CopyAI")
app.geometry("900x500")


def clean_text():
    text = input_box.get("1.0", END)

    # ubah dash menjadi spasi
    text = re.sub(r'[-–—]', ' ', text)

    # hapus bullet / karakter aneh
    text = re.sub(r'[•*#]', '', text)

    # hapus spasi sebelum tanda baca
    text = re.sub(r'\s+([,.!?])', r'\1', text)

    # rapikan line break
    text = re.sub(r'\n+', ' ', text)

    # normalisasi semua spasi
    text = re.sub(r'\s+', ' ', text)

    text = text.strip()

    output_box.delete("1.0", END)
    output_box.insert(END, text)


def copy_text():
    result = output_box.get("1.0", END)
    app.clipboard_clear()
    app.clipboard_append(result)


# konfigurasi grid
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.rowconfigure(1, weight=1)


# label input
label_input = ttk.Label(app, text="Text Belum di Cleansing", font=("Segoe UI", 12))
label_input.grid(row=0, column=0, padx=20, pady=10, sticky="w")


# label output
label_output = ttk.Label(app, text="Text Sudah di Cleansing", font=("Segoe UI", 12))
label_output.grid(row=0, column=1, padx=20, pady=10, sticky="w")


# textbox input
input_box = ttk.Text(app)
input_box.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")


# textbox output
output_box = ttk.Text(app)
output_box.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")


# frame tombol bawah
button_frame = ttk.Frame(app)
button_frame.grid(row=2, column=0, columnspan=2, pady=15, sticky="e", padx=20)


# tombol clean
clean_button = ttk.Button(
    button_frame,
    text="Clean Text",
    bootstyle="primary",
    command=clean_text
)
clean_button.pack(side=LEFT, padx=10)


# tombol copy
copy_button = ttk.Button(
    button_frame,
    text="Copy Result",
    bootstyle="success",
    command=copy_text
)
copy_button.pack(side=LEFT, padx=10)


app.mainloop()