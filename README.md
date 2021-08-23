# MultiMedia


## UI file to py file
  
  **enter this code at terminal**
   
   ![Make PY file](https://github.com/201524495/MultiMedia/blob/main/image/UItoPY.JPG)
   
      pyuic5 -x _uiFiles/example.ui -o modules/UI.py

**before** : using UI

   ![using ui file](https://github.com/201524495/MultiMedia/blob/main/image/before.JPG)

**after** : using PY

   ![using py file](https://github.com/201524495/MultiMedia/blob/main/image/after.JPG)


## Make EXE file

  **enter this code at terminal**
  
  move to "modules" folder -> typo this code
  
   ![Make EXE file](https://github.com/201524495/MultiMedia/blob/main/image/makeEXE.JPG)
   
    cd modules
    
    pyinstaller -w -F basics.py
    
 **Project File**

   ![show project files](https://github.com/201524495/MultiMedia/blob/main/image/projcet.JPG)

 ## Always On Top
 
 ![OnTop](https://github.com/201524495/MultiMedia/blob/main/image/alwaysOnTop.JPG)
 
 ## Keyboard Event
 
  Stop or Exit Video Player
 
 ![Keyboard Event](https://github.com/201524495/MultiMedia/blob/main/image/keyboardEvent.JPG)
  
  Control UI
 
 ![Keyboard Event](https://github.com/201524495/2021_MultiMedia/blob/main/image/keyboardEvent2.JPG)
 
  More Sensitive Keyboard Press
 
 ![Keyboard Event](https://github.com/201524495/2021_MultiMedia/blob/main/image/keyboardEvent3.JPG)
 
 ## Question Box
 
 ![Question Box](https://github.com/201524495/2021_MultiMedia/blob/main/image/QuestionBox.JPG)
 
 ## Mouse Tracking

 ![Clicked Code](https://github.com/201524495/MultiMedia/blob/main/image/mouseClicked.JPG)

 ![Show UI](https://github.com/201524495/MultiMedia/blob/main/image/location_X_Y.JPG)
 
 
## File Open
  
  ![File Open](https://github.com/201524495/2021_MultiMedia/blob/main/image/fileOpen.JPG)
  
  we have to read path in Edit Text Box.
  
  1st sentence is "Find File Path"
  
  2nd sentence is "Convert List to String"
  
  3rd sentence is "Append Later Finding"
  

## File Size Down

  ![File Size Down](https://github.com/201524495/2021_MultiMedia/blob/main/image/sizeDownCode.JPG)
  
   ~~pyinstaller -F -w --exclude pandas, --exclude numpy basi.py~~
    
  ![Result](https://github.com/201524495/2021_MultiMedia/blob/main/image/fileSize.JPG)

  ~~we can Size Down 290MB -> 57MB~~
  
  * But we use cv2, it need numpy.  so other method apply to reduce size...
  
  
  ### Fix
  
  * Make Virtual Enviroment in PyCharm
  
  ![In Virtual](https://github.com/201524495/2021_MultiMedia/blob/main/image/sizeDownCodeVirtual.JPG)
  
  ![Eorror with latest version](https://github.com/201524495/2021_MultiMedia/blob/main/image/ErrorWithVirtualEnv.JPG)
  
      error: (-27:Null pointer) NULL window: 'video_1' in function 'cvMoveWindow'
  
  ![checkVersion](https://github.com/201524495/2021_MultiMedia/blob/main/image/openCVversion.JPG)
  
  latest version occured with my code.\
  so call back last version.
  
  * Result
  
  ![Result](https://github.com/201524495/2021_MultiMedia/blob/main/image/SizeDown.JPG)
