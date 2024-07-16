import win32com.client

from PySide6.QtCore import QThread, Signal

from PIL import Image

class clsClewinAutomation(QThread):
    finished = Signal()
    clewin = None

    def __init__(self) -> None:
        super().__init__()
        #self.outputImageFileFullPath = outputImageFileFullPath
        #self.outputImagePixelSize = outputImagePixelSize
    
    def newDrawing(self, outputImageFileFullPath, outputImagePixelSize):
        self.clewin = win32com.client.Dispatch("CleWin.Application")
        self.clewin.FileNew()
        #Find the image centre position
        im = Image.open(outputImageFileFullPath)
        imageSizeW, imageSizeH = im.size
        topLeftImagePositionXUM = -(imageSizeW/outputImagePixelSize)/2
        topLeftImagePositionYUM = (imageSizeH/outputImagePixelSize)/2
        self.clewin.LoadBackgroundImage(outputImageFileFullPath, topLeftImagePositionXUM, topLeftImagePositionYUM, outputImagePixelSize)
        self.clewin.ViewZoomAll()

        self.clewin.Visible = True
    
    def saveFile(self, outputCIFFileFullPath):
        self.clewin.SaveAs(outputCIFFileFullPath, 1)
        self.clewin = None
        