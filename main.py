import sys
import os
import datetime
from pathlib import Path

from PySide6.QtCore import QThread, Slot
from PySide6.QtWidgets import QApplication, QWidget
from UI.DrawingModeUI.ui_form import Ui_Widget
from TCP_Client.TCP import clsTCPClient
from Clewin.clewinv2 import clsClewinAutomation
from JobListCreator.JobListCreator import createANewJobList

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Initialise the UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #Disable the start drawing button and the Ready for exposures button.
        self.ui.pushButton_StartDrawing.setEnabled(False)
        self.ui.pushButton_ReadyForExposures.setEnabled(False)
        #Disable the line edit for the output image pixel size
        self.ui.lineEdit_PixelSizeUM.setEnabled(False)
        #Connect the button to the functions
        #Start a connection button
        self.ui.pushButtonMW3Connect.clicked.connect(self.estabilishAConnection)
        #Connect the start drawing button
        self.ui.pushButton_StartDrawing.clicked.connect(self.outputImageAndDrawing)
        #Connect the ready for exposure button
        self.ui.pushButton_ReadyForExposures.clicked.connect(self.readyForExposures)

        #Initial the global parameter
        self.currentStatus = ''

    def estabilishAConnection(self):
        #Start a new connection to MW3
        #Read the user input port number
        self.portNumber  = int(self.ui.lineEdit_MW3PortNumber.text())
        self.newConnection = clsTCPClient(self.portNumber)
        #Create a QThread object
        self.thread = QThread()
        #Move the processing to the thread
        self.newConnection.moveToThread(self.thread)
        #Connect signals and slots
        self.thread.started.connect(self.newConnection.makeNewConnection)
        self.newConnection.finished.connect(self.thread.quit)
        self.newConnection.finished.connect(self.newConnection.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.newConnection.signalIsConnected.connect(self.afterFirstTimeConnection)
        self.newConnection.signalResponseFromMW3.connect(self.reportCurrentStatus)
        
        #Start the thread
        self.thread.start()

    @Slot()
    def afterFirstTimeConnection(self):
        self.ui.pushButtonMW3Connect.setEnabled(False)
        self.ui.pushButtonMW3Connect.setText('Connected')
        self.ui.lineEdit_MW3PortNumber.setEnabled(False)
        self.ui.pushButton_StartDrawing.setEnabled(True)
        self.ui.lineEdit_PixelSizeUM.setEnabled(True)
    
    @Slot()
    def reportCurrentStatus(self, currentStatus):
        print(currentStatus)
        self.currentStatus = currentStatus
    
    @Slot()
    def outputImageAndDrawing(self):
        #Disable the VMA first
        self.newConnection.sendACommand('VMAOff()')
        #Get the user input pixel size
        self.userInputPixelSizeUM = self.ui.lineEdit_PixelSizeUM.text()
        #Create a output file folder path
        now = datetime.datetime.now()
        self.outputFileFolderName = now.strftime("%H%M%S%d%m%Y")
        #Create a folder
        self.outputFileFolderPath = os.path.join('C:', os.sep, 'Users', os.getlogin(), 'Documents', 'MW3Drawing', self.outputFileFolderName)
        Path(self.outputFileFolderPath).mkdir(parents=True, exist_ok=True)
        #Create the final output image path
        self.pathOutputImage = os.path.join(self.outputFileFolderPath, 'OutputImage.bmp')    
        self.newConnection.outputImage(self.userInputPixelSizeUM, self.pathOutputImage)

        #Start Clewin
        self.newClewin = clsClewinAutomation()
        self.newClewin.newDrawing(self.pathOutputImage, float(self.userInputPixelSizeUM))

        #Disable the Start drawing button. Enable the Ready for exposures button.
        self.ui.pushButton_StartDrawing.setEnabled(False)
        self.ui.pushButton_ReadyForExposures.setEnabled(True)
        #Disable the pixel size input
        self.ui.lineEdit_PixelSizeUM.setEnabled(False)

    @Slot()
    def readyForExposures(self):
        #Save the Clewin file
        #Save the file in the same folder with the previously exported bmp file
        outputCIFFileName = 'DesignPattern.cif'
        pathOutputCIFFile = os.path.join(self.outputFileFolderPath, outputCIFFileName)
        self.newClewin.saveFile(pathOutputCIFFile)
        #Build a job list for exposure
        #Get the current lens in use and the corresponding resolution beam
        self.newConnection.sendACommand('Lens()')
        currentBeam = self.currentStatus.split("/",1)[1]
        currentBeam = currentBeam.strip()
        #Create a job list
        outputJobListName = 'jobList.xml'
        pathOutputJobList = os.path.join(self.outputFileFolderPath, outputJobListName)
        createANewJobList(currentBeam, self.outputFileFolderPath, outputCIFFileName, pathOutputJobList)
        #Delete all existing jobs
        self.newConnection.sendACommand('DeleteAllJobs()')
        #Open the saved job list
        self.newConnection.sendACommand('OpenJobList({})'.format(pathOutputJobList))
        #Show the AlignWafer panel
        self.newConnection.sendACommand('ShowAlignWafer()')
        #Enable VMA
        self.newConnection.sendACommand('VMAOn()')

        #Reset the UI buttons
        self.ui.pushButton_ReadyForExposures.setEnabled(False)
        self.ui.pushButton_StartDrawing.setEnabled(True)
        self.ui.lineEdit_PixelSizeUM.setEnabled(True)        

if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()

    sys.exit(app.exec())