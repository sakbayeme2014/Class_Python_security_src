Use this program only with console
pip install qrcode  with Linux

> from qrcode import *       #library or module using for generate your qrcode image
> q_object = QRCode(version=20, error_correction=ERROR_CORRECT_L) #  qrcode functions
> q_object.add_data("data")                    # load data do you want
> q_object.make()                              # generate your qrcode 
> xxx_object = q_object.make_image()           # generate PIL image
> xxx_object.save("/root/image.png")           # save your qrcode after generating 

Very simple and advanced functions , and good code 
