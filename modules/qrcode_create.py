import pyqrcode
# import png

from pyqrcode import QRCode

Message = "Hi dears"

url = pyqrcode.create(Message)
url.svg("myqrcode.svg",scale=8)
# url.png('myqrcode.png')