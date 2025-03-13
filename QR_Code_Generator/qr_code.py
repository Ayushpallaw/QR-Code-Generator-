# Here we can create QR Code in two ways. The first way in which no modification is avilable .It will Generally generate QR Code of any given Link.

# 1St Method

import qrcode as qr
# Here we will put the link of any websit etc. which we want to create the QR Code here.
img = qr.make("https://youtube.com/playlist?list=PLdOKnrf8EcP2TfGV0VZueHNye3_vp5fFw&si=-DVzbyzFkrgn1IsK")
# Here i will write the name  with which I want to save
img.save("ayush_pallaw.png")












# Here we can create QR Code in two ways. The Second way in which  modification is avilable .It will Generally generate QR Code of any given Link. In which we can modify it's box size , border size , background color and fill what color we want .


# 2nd Method 

import qrcode 
from PIL import Image
# Here i will modify the size which I want 
qr = qrcode.QRCode(version=1,error_correction = qrcode.constants.ERROR_CORRECT_H ,box_size = 10,border=4)
# Here we will put the link of any websit etc. which we want to create the QR Code here.
qr.add_data("https://youtube.com/playlist?list=PLdOKnrf8EcP2TfGV0VZueHNye3_vp5fFw&si=-DVzbyzFkrgn1IsK")
qr.make(fit=True)
# Here i will chose the color name  with which I want to fill
img=qr.make_image(fill_color="red",back_color="blue")
# Here i will write the name  with which I want to save
img.save("Ayush.png")