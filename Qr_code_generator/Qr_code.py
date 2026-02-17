import qrcode

website_link = "https://github.com/Mustafa786-Python/Beginner-Projects.git"

# making qr_code
qr = qrcode.QRCode(box_size=5, border=3)
qr.best_fit()
qr.add_data(website_link)
qr.make()

# making image
img = qr.make_image(fill_color="#F0EDCC", back_color="#02343F")
img.save('mygithub.png')  # type: ignore
