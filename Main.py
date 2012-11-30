# Mandelbrot Fractal Generator
# Created by Travis Hunt

# cool sample
# maxIterations = 10000
# x_center = -0.743166
# y_center = -0.168341
# width = .0004

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MandelbrotGui import *
from PIL import Image

class WindowForm(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainGui()
        self.ui.setupUi(self)
        self.loader = QMovie("loader.gif")
        self.ui.LoadingView.setMovie(self.loader)
        self.image = Fractal(self.ui.Viewer.width())
        self.imageThread = ImageThread(self.image)        
        self.connect(self.ui.GenerateBtn, SIGNAL("clicked()"), self.OnClick)

    def OnClick(self):
        self.ShowLoader()
        self.image.setMI(int(self.ui.MaxIterations.text()))
        self.image.setX(float(self.ui.XCenter.text()))
        self.image.setY(float(self.ui.YCenter.text()))
        self.image.setW(float(self.ui.Width.text()))
        self.imageThread.start()
        self.connect(self.imageThread, SIGNAL("ThreadDone()"), self.ShowImage)

    def ShowLoader(self):
        self.loader.start()
        self.ui.LoadingView.show()

    def ShowImage(self):
        self.img = QPixmap("image.png")
        self.ui.Viewer.setPixmap(self.img)
        self.loader.stop()
        self.ui.LoadingView.hide()
        

class ImageThread(QThread):
    def __init__(self,image,parent=None):
        super(ImageThread, self).__init__(parent)
        self.image = image
        
    def run(self):
        self.image.generate()
        self.emit(SIGNAL("ThreadDone()"))
        

class Fractal():
    def __init__(self,size,parent=None):
        self.Size = size
        self.MaxIterations = 100.0
        self.xCenter = 0.0
        self.yCenter = 0.0
        self.Width = 4.0
        
    def setMI(self,mi):
        self.MaxIterations = mi
        
    def setX(self,x):
        self.xCenter = x
        
    def setY(self,y):
        self.yCenter = y
        
    def setW(self,w):
        self.Width = w
        
    def generate(self):
        im = Image.new("RGB", (self.Size, self.Size))
        for i in range(self.Size):
            for j in range(self.Size):
                x,y = ( self.xCenter + self.Width*float(i-self.Size/2)/self.Size,
                        self.yCenter + self.Width*float(j-self.Size/2)/self.Size)
                a,b = (0.0, 0.0)
                iteration = 0
                while (a**2 + b**2 <= 4.0 and iteration < self.MaxIterations):
                    a,b = a**2 - b**2 + x, 2*a*b + y
                    iteration += 1
                if iteration < 0:
                    color_value = "0,0,0"            
                else:
                    n = (iteration%70)*10
                    if n <= 250:
                        num = 5+n
                        color_value = num, 0, 0
                    elif n <=500:
                        num = int(5+n-250)
                        color_value = 0, num, 0
                    else:
                        num = int(5+n-500)
                        color_value = 0, 0, num
                im.putpixel( (i,j), (color_value))
        im.save("image.png", "PNG")

        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    win = WindowForm()
    win.show()    
    sys.exit(app.exec_())
