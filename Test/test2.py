import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEncryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.background_image = Image.open("img1.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image, font=("Helvetica", 16))
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_image, font=("Helvetica", 16))
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_image, font=("Helvetica", 16))
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, font=("Helvetica", 16))

        self.load_button.pack(side="left", padx=20, pady=20)
        self.encrypt_button.pack(side="left", padx=20, pady=20)
        self.decrypt_button.pack(side="left", padx=20, pady=20)
        self.save_button.pack(side="left", padx=20, pady=20)

        self.loaded_image = None
        self.encrypted_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.loaded_image = Image.open(file_path)
            self.show_image(self.loaded_image)

    def encrypt_image(self):
        if self.loaded_image:
            # Perform encryption operations here (e.g., swapping pixel values)
            # Example: self.encrypted_image = perform_encryption(self.loaded_image)
            self.show_image(self.encrypted_image)

    def decrypt_image(self):
        if self.encrypted_image:
            # Perform decryption operations here
            # Example: self.decrypted_image = perform_decryption(self.encrypted_image)
            self.show_image(self.decrypted_image)

    def save_image(self):
        if self.encrypted_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                # Save the encrypted or decrypted image
                self.encrypted_image.save(file_path)

    def show_image(self, img):
        img = img.resize((int(self.root.winfo_screenwidth() * 0.6), int(self.root.winfo_screenheight() * 0.6)))
        photo = ImageTk.PhotoImage(img)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptor(root)
    root.mainloop()
