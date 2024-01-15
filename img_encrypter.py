from tkinter import *
from tkinter import filedialog, messagebox
import os
from PIL import Image
from Crypto.Cipher import AES
import hashlib
import binascii
import numpy as np

global password

def load_image(name):
    return Image.open(name)

def prepare_message_image(image, size):
    if size != image.size:
        image = image.resize(size, Image.ANTIALIAS)
    return image

def generate_secret(size, secret_image=None):
    width, height = size
    new_secret_image = Image.new(mode="RGB", size=(width * 2, height * 2))

    for x in range(0, 2 * width, 2):
        for y in range(0, 2 * height, 2):
            color1 = np.random.randint(255)
            color2 = np.random.randint(255)
            color3 = np.random.randint(255)
            new_secret_image.putpixel((x, y), (color1, color2, color3))
            new_secret_image.putpixel((x + 1, y), (255 - color1, 255 - color2, 255 - color3))
            new_secret_image.putpixel((x, y + 1), (255 - color1, 255 - color2, 255 - color3))
            new_secret_image.putpixel((x + 1, y + 1), (color1, color2, color3))

    return new_secret_image

def generate_ciphered_image(secret_image, prepared_image):
    width, height = prepared_image.size
    ciphered_image = Image.new(mode="RGB", size=(width * 2, height * 2))
    for x in range(0, width * 2, 2):
        for y in range(0, height * 2, 2):
            sec = secret_image.getpixel((x, y))
            msssg = prepared_image.getpixel((int(x / 2), int(y / 2)))
            color1 = (msssg[0] + sec[0]) % 256
            color2 = (msssg[1] + sec[1]) % 256
            color3 = (msssg[2] + sec[2]) % 256
            ciphered_image.putpixel((x, y), (color1, color2, color3))
            ciphered_image.putpixel((x + 1, y), (255 - color1, 255 - color2, 255 - color3))
            ciphered_image.putpixel((x, y + 1), (255 - color1, 255 - color2, 255 - color3))
            ciphered_image.putpixel((x + 1, y + 1), (color1, color2, color3))

    return ciphered_image

def generate_image_back(secret_image, ciphered_image):
    width, height = secret_image.size
    new_image = Image.new(mode="RGB", size=(int(width / 2), int(height / 2)))
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            sec = secret_image.getpixel((x, y))
            cip = ciphered_image.getpixel((x, y))
            color1 = (cip[0] - sec[0]) % 256
            color2 = (cip[1] - sec[1]) % 256
            color3 = (cip[2] - sec[2]) % 256
            new_image.putpixel((int(x / 2), int(y / 2)), (color1, color2, color3))

    return new_image

def level_one_encrypt(Imagename):
    message_image = load_image(Imagename)
    size = message_image.size
    width, height = size

    secret_image = generate_secret(size)
    secret_image.save("secret.jpeg")

    prepared_image = prepare_message_image(message_image, size)
    ciphered_image = generate_ciphered_image(secret_image, prepared_image)
    ciphered_image.save("2-share_encrypt.jpeg")

def construct_enc_image(ciphertext, relength, width, height):
    asciicipher = binascii.hexlify(ciphertext)

    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    reps = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
            'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
            'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    asciiciphertxt = replace_all(asciicipher.decode('utf-8'), reps)

    step = 3
    encimageone = [asciiciphertxt[i:i + step] for i in range(0, len(asciiciphertxt), step)]
    if int(encimageone[len(encimageone) - 1]) < 100:
        encimageone[len(encimageone) - 1] += "1"
    if len(encimageone) % 3 != 0:
        while len(encimageone) % 3 != 0:
            encimageone.append("101")

    encimagetwo = [(int(encimageone[int(i)]), int(encimageone[int(i + 1)]), int(encimageone[int(i + 2)])) for i in
                   range(0, len(encimageone), step)]

    while int(relength) != len(encimagetwo):
        encimagetwo.pop()

    encim = Image.new("RGB", (int(width), int(height)))
    encim.putdata(encimagetwo)
    encim.save("visual_encrypt.jpeg")

def encrypt(imagename, password):
    plaintext = list()
    plaintextstr = ""

    im = Image.open(imagename)
    pix = im.load()

    width = im.size[0]
    height = im.size[1]

    for y in range(0, height):
        for x in range(0, width):
            for channel in range(3):
                 aa = pix[x, y][channel] + 100
                 plaintextstr = plaintextstr + str(aa)

  


    relength = len(plaintext)
    plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"

    while len(plaintextstr) % 16 != 0:
        plaintextstr = plaintextstr + "n"

    iv = b'This is an IV456'  # Convert IV to bytes
    key = hashlib.sha256(password).digest()

    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(plaintextstr.encode('utf-8'))

    cipher_name = imagename + ".crypt"
    with open(cipher_name, 'wb') as g:
        g.write(ciphertext)

    construct_enc_image(ciphertext, relength, width, height)
    print("Visual Encryption done.......")
    level_one_encrypt("visual_encrypt.jpeg")
    print("2-Share Encryption done.......")



def decrypt(ciphername, password):
    secret_image = Image.open("secret.jpeg")
    ima = Image.open("2-share_encrypt.jpeg")
    new_image = generate_image_back(secret_image, ima)
    new_image.save("2-share_decrypt.jpeg")
    print("2-share Decryption done....")
    with open(ciphername, 'rb') as cipher:
        ciphertext = cipher.read()

    obj2 = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    decrypted = obj2.decrypt(ciphertext)

    decrypted = decrypted.decode('utf-8').replace("n", "")

    newwidth = decrypted.split("w")[1]
    newheight = decrypted.split("h")[1]

    heightr = "h" + str(newheight) + "h"
    widthr = "w" + str(newwidth) + "w"
    decrypted = decrypted.replace(heightr, "")
    decrypted = decrypted.replace(widthr, "")

    step = 3
    finaltextone = [decrypted[i:i + step] for i in range(0, len(decrypted), step)]
    finaltexttwo = [(int(finaltextone[int(i)]) - 100, int(finaltextone[int(i + 1)]) - 100,
                     int(finaltextone[int(i + 2)]) - 100) for i in range(0, len(finaltextone), step)]

    newim = Image.new("RGB", (int(newwidth), int(newheight)))
    newim.putdata(finaltexttwo)
    newim.save("visual_decrypt.jpeg")
    print("Visual Decryption done......")

def pass_alert():
    messagebox.showinfo("Password Alert", "Please enter a password.")

def image_open():
    global file_path_e

    enc_pass = passg.get()
    if enc_pass == "":
        pass_alert()
    else:
        password = hashlib.sha256(enc_pass.encode('utf-8')).digest()
        filename = filedialog.askopenfilename()
        file_path_e = os.path.dirname(filename)
        encrypt(filename, password)

def cipher_open():
    global file_path_d

    dec_pass = passg.get()
    if dec_pass == "":
        pass_alert()
    else:
        password = hashlib.sha256(dec_pass.encode('utf-8')).digest()
        filename = filedialog.askopenfilename()
        file_path_d = os.path.dirname(filename)
        decrypt(filename, password)

class App:
    def __init__(self, master):
        global passg
        title = "Image Encryption"
        author = "Nirant Chavda"
        msgtitle = Message(master, text=title)
        msgtitle.config(font=('helvetica', 17, 'bold'), width=200)
        msgauthor = Message(master, text=author)
        msgauthor.config(font=('helvetica', 10), width=200)

        canvas_width = 200
        canvas_height = 50
        w = Canvas(master, width=canvas_width, height=canvas_height)
        msgtitle.pack()
        msgauthor.pack()
        w.pack()

        passlabel = Label(master, text="Enter Encrypt/Decrypt Password:")
        passlabel.pack()
        passg = Entry(master, show="*", width=20)
        passg.pack()

        self.encrypt = Button(master, text="Encrypt", fg="black", command=image_open, width=25, height=5)
        self.encrypt.pack(side=LEFT)
        self.decrypt = Button(master, text="Decrypt", fg="black", command=cipher_open, width=25, height=5)
        self.decrypt.pack(side=RIGHT)

# MAIN
root = Tk()
root.wm_title("Image Encryption")
app = App(root)
root.mainloop()
