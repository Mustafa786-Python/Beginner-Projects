import qrcode

website_link = ""

# making qr_code
qr = qrcode.QRCode(box_size=5, border=3)
qr.best_fit()
qr.add_data(website_link)
qr.make()

# making image
img = qr.make_image(fill_color="blue", back_color="white")
img.save('qrcode1.png')  # type: ignore
