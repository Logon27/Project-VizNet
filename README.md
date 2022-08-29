## Compiling And Running
---
Use QT designer to modify the dialog.ui file.  
Save the dialog.ui file.  
Compile the dialog.ui file to python with...   
pyuic5 dialog.ui > dialog.py

Then run the program...  
python application.py

## Matplotlib Widgets
---
Promoted classes are used to add the matplotlib widgets.  
The promoted class name e.g. "Widget2dErrorGraph" specifies the widget class in the header file e.g. "widget_2derrorgraph". These names must match within the python project so that they can be linked to the UI. The associated "Canvas" class instead the header file can be named whatever you want.