# Project Viznet

## About The Project
Project Viznet is a neural network visualization program. It helps beginners visualize how a neural network works in 2d and 3d space. As well as provides an editor to modify the neural network architecture.

**WARNING:** This project currently has a decent amount of spaghetti code. But the program in its current working state I find to be valuable educationally. So I am releasing it before refactoring a lot of the code.

[![Project Viznet Demo Link](https://img.youtube.com/vi/GffIyL9l3gc/0.jpg)](https://www.youtube.com/watch?v=GffIyL9l3gc)

Base network implementation is a fork from https://github.com/TheIndependentCode/ that has been modified.

## Supported Neural Layers
- Dense(numInputNeurons, numOutputNeurons)
- Tanh()
- Sigmoid()
- Relu()
- LeakyRelu()

**NOTE:** The first Dense layer must have 2 inputs. And the final Dense layer must have 1 output. The number of outputs of the previous Dense layer must match the number of inputs in the subsequent layer

## Running The Program Via Exe
I have compiled a Windows executable for Project Viznet. You should just be able to download the executable called ```ProjectViznet-X.X.X.exe``` from the ```dist``` folder and run it locally. It will open a console window along with the visualization program itself. This console will give you epoch and error information when the network is training. Windows may give you a warning screen when trying to run the program. This is just because I didn't purchase a publisher certificate to distribute the executable.

## Compiling And Running From Source
Use QT designer to modify the dialog.ui file.  
Save the dialog.ui file.  
Compile the dialog.ui file to python with...   
```
pyuic5 dialog.ui > dialog.py
```

Then run the program...  
```
python application.py
```

## Known Limitations
- You cannot interact with the program window while the network is training. The program is single threaded and uses your cpu to train the network.

## Matplotlib Widgets
Promoted classes are used to add the matplotlib widgets.  
The promoted class name e.g. "Widget2dErrorGraph" specifies the widget class in the header file e.g. "widget_2derrorgraph". These names must match within the python project so that they can be linked to the UI. The associated "Canvas" class instead the header file can be named whatever you want.

## Distribution
Running...  
```
pyinstaller -F application.py
```  
Generates a single Windows executable in the dist folder.
The dist and build folders are both build files from pyinstaller. As is the application.spec file.  
https://pyinstaller.org/en/stable/usage.html  

## TODO
- "Select Architecture" and "Select Pretrained Network" buttons removed. To be re-added and implemented in future.
- Need to make the neural network run on a separate thread to not freeze the GUI.
- "Pause Training" and "Stop Training" buttons removed. To be re-added and implemented in future.
