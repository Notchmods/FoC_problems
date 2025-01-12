import pyqrcode
from PIL import Image
import png

#Get the link for the website you wanna generate from
website= input("Enter the link that you want to generate QR from: ")
name=input("What do you want the file name to be: ")
#Create QR code
qr=pyqrcode.create(website)
#Create the file that has the QR Code on it
qr.png(name+".png",scale=5)
#Open the image file
im=Image.open(name+".png")
im.show()
