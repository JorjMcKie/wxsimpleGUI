# wxsimpleGUI
A standard GUI collection written in wxPython

Use like `import wxsimpleGUI as sg`.

The following functions are currently implemented:

|name|purpose|
|----|-------|
|SelectOne|Select one string out of a list|
|SelectMult|Select multiple out of a list of strings|
|DirDlg|Standard directory selection|
|OpenDlg|Multiple file selection|
|ExcBox|Display tracback of last exception|
|YesNoBox|Return True or False|
|InputBox|Return entered string|
|MultInputBox|Simple multiple data input dialog|
|MsgBox|The standard one|
|BusyInfo|Display non-blocking info|
|CodeBox|Display files or lines in a scrollable windows|

# Example

```
import wxsimpleGUI as sg
answer = sg.YesNoBox("Do you smoke?", "an honest answer please!")
if answer:
    print("you are reducing your life expectancy!")
else:
    print("I hope you didn't lie ...")
''' 
