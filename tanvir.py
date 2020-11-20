import pyqrcode
import png
from pyqrcode import QRCode
str = "https://www.facebook.com/t.ahmed0001"
url = pyqrcode.create(str)
url.png("tab1.png2", scale=20)
#url.svg("my.svg",scale=20)