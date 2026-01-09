import qrcode
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

logo_path = None  # Para guardar la ruta de la imagen

# Función para seleccionar logo
def seleccionar_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(
        title="Selecciona un logo",
        filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if logo_path:
        messagebox.showinfo("Logo seleccionado", f"Logo: {logo_path}")

# Función para generar QR
def generar_qr():
    url = entry.get()
    if url == "":
        messagebox.showwarning("Advertencia", "Por favor ingresa un link")
        return

    # Crear QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Muy alta corrección
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Si hay logo, lo añadimos
    if logo_path:
        logo = Image.open(logo_path)

        # Redimensionar logo al 20% del QR
        qr_width, qr_height = img_qr.size
        logo_size = int(qr_width * 0.2)
        logo = logo.resize((logo_size, logo_size))

        # Pegar logo en el centro
        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        img_qr.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    # Mostrar QR en ventana
    img_tk = ImageTk.PhotoImage(img_qr)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    # Guardar QR
    img_qr.save("mi_qr_con_logo.png")
    messagebox.showinfo("Listo", "QR generado y guardado como 'mi_qr_con_logo.png'")

# Crear ventana
ventana = Tk()
ventana.title("Generador de QR con Logo")
ventana.geometry("450x550")

Label(ventana, text="Ingresa tu link:").pack(pady=10)
entry = Entry(ventana, width=40)
entry.pack(pady=10)

Button(ventana, text="Seleccionar Logo", command=seleccionar_logo).pack(pady=10)
Button(ventana, text="Generar QR", command=generar_qr).pack(pady=10)

qr_label = Label(ventana)
qr_label.pack(pady=20)

ventana.mainloop()
