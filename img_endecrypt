import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        
        # Header Section
        header_label = tk.Label(root, text="Image Encryption Tool", font=("Helvetica", 16))
        header_label.pack()

        # Footer Section
        footer_frame = tk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=10)

        linkedin_logo = tk.PhotoImage(file="linkedin.png")
        linkedin_button = tk.Button(footer_frame, image=linkedin_logo, command=self.open_linkedin)
        linkedin_button.image = linkedin_logo
        linkedin_button.grid(row=0, column=0, padx=10)

        github_logo = tk.PhotoImage(file="github.png")
        github_button = tk.Button(footer_frame, image=github_logo, command=self.open_github)
        github_button.image = github_logo
        github_button.grid(row=0, column=1, padx=10)

        # Main Section
        main_frame = tk.Frame(root)
        main_frame.pack()

        load_button = tk.Button(main_frame, text="Load Image", command=self.load_image)
        load_button.grid(row=0, column=0, pady=10)

    def open_linkedin(self):
        import webbrowser
        webbrowser.open("https://www.linkedin.com/in/orpheusdark")

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/orpheusdark/PRODIGY_CS_02")

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            self.show_image(file_path)

    def show_image(self, file_path):
        image = Image.open(file_path)

        # Resize image for fixed size preview
        fixed_size = (300, 200)
        resized_image = image.resize(fixed_size)

        # Popup Window 1
        popup_window_1 = tk.Toplevel(self.root)
        popup_window_1.title("Image Encryption/Decryption")
        popup_window_1.geometry("800x600")

        # Display the resized image in Popup Window 1
        tk.Label(popup_window_1, image=ImageTk.PhotoImage(resized_image)).pack()

        # Encryption and Decryption Buttons
        encrypt_button = tk.Button(popup_window_1, text="Encrypt", command=lambda: self.encrypt_image(image))
        encrypt_button.pack(pady=10)

        decrypt_button = tk.Button(popup_window_1, text="Decrypt", command=lambda: self.decrypt_image(image))
        decrypt_button.pack(pady=10)

    def encrypt_image(self, image):
        # Implement your encryption logic here
        # For simplicity, let's just invert the pixel values
        encrypted_image = Image.eval(image, lambda x: 255 - x)

        # Popup Window 2
        popup_window_2 = tk.Toplevel(self.root)
        popup_window_2.title("Encrypted Image")
        popup_window_2.geometry("800x600")

        # Display the encrypted image in Popup Window 2
        tk.Label(popup_window_2, image=ImageTk.PhotoImage(encrypted_image)).pack()

        # Save Button
        save_button = tk.Button(popup_window_2, text="Save Encrypted Image", command=lambda: self.save_image(encrypted_image))
        save_button.pack(pady=10)

    def decrypt_image(self, image):
        # Implement your decryption logic here
        # For simplicity, let's just invert the pixel values again
        decrypted_image = Image.eval(image, lambda x: 255 - x)

        # Popup Window 3
        popup_window_3 = tk.Toplevel(self.root)
        popup_window_3.title("Decrypted Image")
        popup_window_3.geometry("800x600")

        # Display the decrypted image in Popup Window 3
        tk.Label(popup_window_3, image=ImageTk.PhotoImage(decrypted_image)).pack()

        # Save Button
        save_button = tk.Button(popup_window_3, text="Save Decrypted Image", command=lambda: self.save_image(decrypted_image))
        save_button.pack(pady=10)

    def save_image(self, image):
        file_path = filedialog.asksaveasfilename(title="Save Image As", defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if file_path:
            image.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()
