from PySide6.QtCore import QThread, Signal
import socket

class clsTCPClient(QThread):
    signalIsConnected = Signal()
    signalResponseFromMW3 = Signal(str)
    finished = Signal()

    def __init__(self, portNumber) -> None:
        super().__init__()
        self.portNumber = portNumber
        #Creat a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def makeNewConnection(self):
        #Bind the socket to the port
        server_address = ('localhost', self.portNumber)
        print('Starting up on %s port %s' % server_address)
        try:
            self.sock.connect(server_address)
        except:
            reportMessage = "Connection failed."
            self.signalResponseFromMW3.emit(reportMessage)
            self.finished.emit()
            return

        #print(self.waitForResponseFromMicroWriter(self.sock))
        self.waitForResponseFromMicroWriter(self.sock)

    def waitForResponseFromMicroWriter(self, client):
        result=''
        response=client.recv(4096)

        finish=False

        while not finish:
            if response:
                a=response.decode().split("$")
                result+=a[0]
                if len(a)>1:
                    finish=True
            else:
                #print('Closing socket')
                result = 'Closing socket'
                client.close()
                finish=True
        
        #Check if the connection is established for the first time.
        if result[:5] == 'Hello':
            self.signalIsConnected.emit()

        #Report back the response from MW3.
        self.signalResponseFromMW3.emit(result)

        return result
    
    def outputImage(self, userInputMicroscopePixelSizeUM, outputImageFullPath):
        #Make the new origin
        self.sendACommand('PlaceMarker(1)')
        self.sendACommand('DeleteMarker(2)')
        self.sendACommand('DeleteMarker(3)')
        self.sendACommand('DeleteMarker(4)')
        self.sendACommand('CentreRectangular()')

        #Set pixel size of the output image
        self.sendACommand('MicroscopePixelSize({0})'.format(userInputMicroscopePixelSizeUM))
        #Save the image
        self.sendACommand('ExportMicroscope({0})'.format(outputImageFullPath))


    
    def sendACommand(self, command):
        self.sock.send((command + '\r\n').encode())
        
        #Update the current status
        self.waitForResponseFromMicroWriter(self.sock)

    def closingSock(self):
        self.sock.close
        self.finished.emit()