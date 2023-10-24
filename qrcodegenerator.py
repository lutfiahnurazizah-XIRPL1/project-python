import qrcode # install library di cmd -> pip install qrcode
import image # install library di cmd -> pip install image 
qr = qrcode.QRCode(
    version = 15, #untuk versi qr codenya
    box_size = 10, #untuk ukuran qr codenya
    border = 5 #ukuran putih2nya qr code
)

data = "https://www.youtube.com/watch?v=Y7IH7mOzDM4" #link qr code
# yang akan ditampilkan 

qr .add_data(data)
qr .make(fit = True)
img = qr.make_image(fill="black", back_color = "white") #setting warna qr code
img.save("test.png") # untuk bulid qr ke gambar pngs