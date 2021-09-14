import qrcode

data = input("Enter the data to generate a QR code:- ")
qr = qrcode.QRCode(version= 1, box_size =10, border = 5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'yellow', back_color = 'red')
img.save('D:/vs codes/python/generated_qrcode.png')       