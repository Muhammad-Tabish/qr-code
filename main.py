import pyqrcode
import png
from pyqrcode import QRCode
str = "www.youtube.com"
url = pyqrcode.create(str)
url.png("tabish.png", scale=20)
#url.svg("my.svg",scale=20)