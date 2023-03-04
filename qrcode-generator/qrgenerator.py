import qrcode

subscribe_url = f"https://www.youtube.com/channel/UCjg1f871TXM4W-8chsh-uag"

qr = qrcode.QRCode(
    box_size=10,
    border=4
)

qr.add_data(subscribe_url)

qr.make(fit=True)

qr.make_image(fill_color = "#B4E4FF", back_color= "#95BDFF").save("qr4.png")
