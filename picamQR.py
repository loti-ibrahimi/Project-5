from SimpleCV import Color,Camera,Display

cam = Camera()  #starts the camera
display = Display() 

while(display.isNotDone()):
 
 img = cam.getImage() #gets image from the camera

 barcode = img.findBarcode() #finds barcode data from image
 if(barcode is not None): #if there is some data processed
   barcode = barcode[0] 
   result = str(barcode.data)
   print result #prints result of barcode in python shell
   barcode = [] #reset barcode data to empty set

 img.save(display) #shows the image on the screen