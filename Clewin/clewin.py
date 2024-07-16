import win32com.client

clewin = win32com.client.Dispatch("CleWin.Application")
clewin.FileNew()
#clewin.Open(r"C:\Users\Jung-WeiLiao\OneDrive - Durham Magneto Optics Ltd\Document\Qt\Contacts maker\Example file\DMO test chip single v3 Layer 0.cif")
clewin.LoadBackgroundImage(r"C:\Users\Jung-WeiLiao\OneDrive - Durham Magneto Optics Ltd\Document\Qt\Contacts maker\Example file\export background 1.bmp", -100, 80, 1)
clewin.ViewZoomAll()

clewin.Visible = True