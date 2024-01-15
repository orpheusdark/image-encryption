import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEncryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")
        self.root.geometry("1900x1000")  # Set to full screen
        self.root.resizable(True, True)

        # Background image
        bg_image = Image.open("img1.jpg")
        bg_image = bg_image.resize((1920, 1080))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo

        # Load Image button
        load_btn = tk.Button(self.root, text="Load Image", command=self.load_image, font=("Helvetica", 14))
        load_btn.place(relx=0.1, rely=0.1, anchor="center")

        # Encrypt button
        encrypt_btn = tk.Button(self.root, text="Encrypt", command=self.encrypt_image, font=("Helvetica", 14))
        encrypt_btn.place(relx=0.5, rely=0.1, anchor="center")

        # Decrypt button
        decrypt_btn = tk.Button(self.root, text="Decrypt", command=self.decrypt_image, font=("Helvetica", 14))
        decrypt_btn.place(relx=0.9, rely=0.1, anchor="center")

        # Image display window
        self.canvas = tk.Canvas(self.root, width=800, height=600, bd=0, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((800, 600))
            photo = ImageTk.PhotoImage(image)
            self.canvas.config(width=image.width, height=image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

    def encrypt_image(self):
        # Implement your image encryption logic here
        pass

    def decrypt_image(self):
        # Implement your image decryption logic here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptor(root)
    root.mainloop()
