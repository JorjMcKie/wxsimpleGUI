#!/usr/bin/python
# -*- coding: utf-8 -*-

import  wx.lib.layoutf as layoutf
import traceback, wx, os

#TODO Check to see if this is still needed. Don't think that it is now that eash func also calls
# app = wx.App()

#-----------------------------------------------------------------------------#
#                   SelectOne                                                 #
#-----------------------------------------------------------------------------#
def SelectOne(title, msg, lst, size = (-1, -1), icon = None):
    '''
    Show a list of strings.
    Arguments: title, message and a list of strings to be shown for selection.
    Return will be the selected string.
    '''
    app = wx.App()
    dlg = wx.SingleChoiceDialog(None, msg, title, lst, wx.CHOICEDLG_STYLE)
    dlg.Size = size
    if icon:
        dlg.SetIcon(icon.GetIcon())
    if dlg.ShowModal() == wx.ID_OK:
        sel = dlg.GetStringSelection()
    else:
        sel = None

    dlg.Destroy()
    del app
    return sel

#-----------------------------------------------------------------------------#
#                   SelectMult                                                #
#-----------------------------------------------------------------------------#
def SelectMult(title, msg, lst, preselect=None, size = (-1, -1), icon = None):
    '''
    Show a list of strings with a check box each.
    Args: title, message, list and an optional list of integers containing to
    indicate which items should appear as preselected.
    Return is a list of integers of the selected item index.
    '''
    app = wx.App()
    dlg = wx.MultiChoiceDialog(None, msg, title, lst)
    if icon:
        dlg.SetIcon(icon.GetIcon())
    if type(preselect) == type([]):
        dlg.SetSelections(preselect)

    dlg.Size = size
    if (dlg.ShowModal() == wx.ID_OK):
        selections = dlg.GetSelections()
    else:
        selections = None

    dlg.Destroy()
    del app
    return selections

#-----------------------------------------------------------------------------#
#                   DirDlg                                                    #
#-----------------------------------------------------------------------------#
def DirDlg(title="Choose a directory:",
           startdir = os.getcwd(), size =(-1, -1), icon = None):

    app = wx.App()

    dlg = wx.DirDialog(None, title, pos=(-1,-1),
                  style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST | \
                  wx.DD_CHANGE_DIR)
    if icon:
        dlg.SetIcon(icon.GetIcon())
    dlg.SetPath(startdir)
    dlg.Size = size

    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
    else:
        path = None
    dlg.Destroy()
    del app
    return path

#-----------------------------------------------------------------------------#
#                   OpenDlg                                                   #
#-----------------------------------------------------------------------------#
def OpenDlg(title="Choose files", mult = True, icon = None,
            startdir = os.getcwd(), wildcard = None, size = (-1, -1)):
    '''
    Returns a list of selected files.
    '''
    app = wx.App()

    if wildcard is None:
        wild = "Python Files (*.py*)|*.py*|"     \
                   "All Files (*.*)|*.*"
    else:
        wild = wildcard

    if mult:
        dlg = wx.FileDialog(None, message = title,
                        defaultDir = startdir,
                        defaultFile = "",
                        wildcard=wild,
                        style = wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR)
    else:
        dlg = wx.FileDialog(None, message = title,
                        defaultDir = startdir,
                        defaultFile = "",
                        wildcard = wild,
                        style = wx.FD_OPEN | wx.FD_CHANGE_DIR)

    dlg.Size = size
    if icon:
        dlg.SetIcon(icon.GetIcon())
    # Show the dialog and retrieve the user response.
    # If OK process data.
    if dlg.ShowModal() == wx.ID_OK:
        # This returns a Python list of files that were selected.
        paths = dlg.GetPaths()
    else:
        paths = None
    dlg.Destroy()
    del app
    return paths

#-----------------------------------------------------------------------------#
#                   ExcBox                                                    #
#-----------------------------------------------------------------------------#
def ExcBox(title="Exception"):
    '''
    Return a message box with traceback content of the last exception.
    '''
    app = wx.App()

    trc = traceback.format_exc()
    wx.MessageBox(trc, title)
    del app
    return

#-----------------------------------------------------------------------------#
#                   YesNoBox                                                  #
#-----------------------------------------------------------------------------#
def YesNoBox(title, msg="", icon = None):
    '''
    Show a YES/NO box and return True or False.
    '''
    app = wx.App()

    dlg = wx.MessageDialog(None, msg, title, wx.YES_NO | wx.ICON_QUESTION)
    if icon:
        dlg.SetIcon(icon.GetIcon())
    result = dlg.ShowModal()
    dlg.Destroy()
    del app
    if result == wx.ID_YES: return True
    return False

#-----------------------------------------------------------------------------#
#                   InputBox                                                  #
#-----------------------------------------------------------------------------#
def InputBox(title, msg, default="", icon = None):
    '''
    Returns:  user entered string.
              None if user cancelled
    '''
    app = wx.App()

    dlg = wx.TextEntryDialog(None, msg, title, default)
    if icon:
        dlg.SetIcon(icon.GetIcon())
    if dlg.ShowModal() == wx.ID_OK:
        rc = dlg.GetValue()
        if not rc: rc = None
    else:
        rc = None
    dlg.Destroy()
    del app
    return rc

#-----------------------------------------------------------------------------#
#                   MultInputBox                                              #
#-----------------------------------------------------------------------------#
def MultInputBox(title, msg_text, Label, Feld, icon = None):
    '''
    Show two lists: one with field labels and one with field contents. User
    entries will change the field contents. Can be used for simple data entries.
    '''
    class MyDialog(wx.Dialog):
        def __init__(self, parent=None, msg="", caption="",
                     pos=(-1,-1), size=(500,300),
                     style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | \
                     wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | \
                     wx.FULL_REPAINT_ON_RESIZE):
            wx.Dialog.__init__(self, parent, -1, caption, pos, size, style)

    app = wx.App()

    dlg = MyDialog()
    dlg.Position = (-1, -1)
    dlg.Title = title
    
    msg = wx.StaticText(dlg, -1, msg_text.ljust(100," "))
    okay = wx.Button(dlg, wx.ID_OK)			# OK btn
    okay.SetDefault()
    cancel = wx.Button(dlg, wx.ID_CANCEL)	# CANCEL btn
    sizer = wx.BoxSizer(wx.VERTICAL)		# Box Sizer
    sizer.Add(msg, 0, wx.ALL, 5)			# Zeile 1 = explanation
    sizer.Add(wx.StaticLine(dlg), 0, wx.EXPAND|wx.ALL, 5)	# then a line
    
    num_fields = len(Feld)
    if num_fields != len(Label):
        raise ValueError("unequal number of labels and fields")

    field_lbl = list(range(num_fields))
    field_cont = list(range(num_fields))

    fgs = wx.FlexGridSizer(rows=num_fields, cols=2, hgap=5, vgap=5)

    for i in range(num_fields):
        field_lbl[i] = wx.StaticText(dlg, -1, Label[i]) # label
        field_cont[i] = wx.TextCtrl(dlg)                # content
        field_cont[i].Value = Feld[i]                   # fill in supplied
        fgs.Add(field_lbl[i], 0, wx.ALIGN_RIGHT)        # label right aligned
        fgs.Add(field_cont[i], 0, wx.EXPAND)            # expand content

    fgs.AddGrowableCol(1)

    sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

    btns = wx.StdDialogButtonSizer()    # define button sizer
    btns.AddButton(okay) 
    btns.AddButton(cancel) 
    btns.Realize()
    sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5) # add btn size
    if icon:
        dlg.SetIcon(icon.GetIcon())
    dlg.SetSizer(sizer)  
    sizer.Fit(dlg)       
    dlg.Center()         

    rc = dlg.ShowModal() 

    if rc != wx.ID_OK:                  # do nothing
        dlg.Destroy()   
        return None     

    for i in range(num_fields):         # put inputs back
        Feld[i] = field_cont[i].Value

    dlg.Destroy() 
    del app
    return True   

#-----------------------------------------------------------------------------#
#                   MsgBox                                                    #
# TODO add option to play 'beep' sound. Currently ALWAYS beeping (annoying)   #
#-----------------------------------------------------------------------------#
def MsgBox(title, msg):
    app = wx.App()
    wx.MessageBox(msg, title)
    del app
    return

#-----------------------------------------------------------------------------#
#                   BusyInfo                                                  #
#-----------------------------------------------------------------------------#
def BusyInfo(title, msg, image = None):
    '''
    Show a "busy" message. Will not block but return the busy-object.
    Important: this will NEVER disappear - except when you delete this object!
    E.g. by setting busy = None oder del busy.
    '''
    import wx.lib.agw.pybusyinfo as PBI

    app = wx.App()

    if not image:
        img = wx.NullBitmap
    elif type(image) == type(u""):
        if image.endswith(".ico"):
            icon = wx.Icon(image, wx.BITMAP_TYPE_ICO)
            img = wx.BitmapFromIcon(icon)
        else:
            img = wx.Bitmap(image, wx.BITMAP_TYPE_ANY)
    else:
        img = image.GetBitmap()

    busy = PBI.PyBusyInfo(msg, parent=None, title=title, icon=img)
    wx.Yield()
    return busy

#-----------------------------------------------------------------------------#
#                   CodeBoxFF                                                 #
#-----------------------------------------------------------------------------#
class CodeBoxFF(wx.Dialog):

    def __init__(self, parent, msg, caption, FF=True, fsize = 10, icon = None,
                 pos=(-1,-1) , size=(500,300),
                 style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | \
                 wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | \
                 wx.FULL_REPAINT_ON_RESIZE):

        wx.Dialog.__init__(self, parent, -1, caption, pos, size, style)
        if icon:
            self.SetIcon(icon.GetIcon())
        # always center on screen
        self.CenterOnScreen(wx.BOTH)
        self.text = text = wx.TextCtrl(self, -1, msg,
                                       style=wx.TE_MULTILINE | wx.TE_READONLY)
        # default 10-point fixed font (DejaVu Sans Mono)
        if FF:
            self.text.SetFont(wx.Font(fsize, wx.MODERN, wx.NORMAL,
                                  wx.NORMAL, 0, "DejaVu Sans Mono"))
        else:
            self.text.SetFont(wx.Font(fsize, wx.MODERN, wx.NORMAL,
                                  wx.NORMAL, 0, "Calibri"))

        ok = wx.Button(self, wx.ID_OK, "OK")
        lc = layoutf.Layoutf('t=t5#1;b=t5#2;l=l5#1;r=r5#1', (self,ok))
        text.SetConstraints(lc)

        lc = layoutf.Layoutf('b=b5#1;x%w50#1;w!80;h*', (self,))
        ok.SetConstraints(lc)
        ok.SetDefault()
        self.SetAutoLayout(1)
        self.Layout()

#-----------------------------------------------------------------------------#
#                   CodeBox                                                   #
#-----------------------------------------------------------------------------#
def CodeBox(title, msg, size=(800,600), FF=True, icon = None):
    '''
    Show contents of a file or arbitrary text lines in a scrollable windows.
    Argument msg may be a (list of) string. If starting with "file=", then the
    rest is interpreted as a file name. This file will be displayed then.
    Use FF to control use of a mono spaced vs. proportional font.
    '''
    app = wx.App()

    if type(msg) in (list, tuple):
        msg_d = "\n".join(msg)
    elif msg.startswith("file="):   # den Inhalt einer Datei anzeigen
        fname = msg[5:]
        try:                        # wenn das mal gut geht ...
            fid = open(fname)
            msg_d = fid.read()
            fid.close()
        except:                     # hab's ja geahnt!
            msg_d = msg + "\nexistiert nicht!"
    else:
        msg_d = msg

    dlg = CodeBoxFF(None, msg_d, title, size=size, FF=FF, icon = icon)

    dlg.ShowModal()
    dlg.Destroy()
    del app
    return

# ------------------------------------------------------------------------- #
#                       ProgressMeter                                       #
# ------------------------------------------------------------------------- #
class ProgessMeter:
    '''
    Display a Progress Meter without blocking
    Provides an early cancelling
    '''
    #todo make an option to self-close on completion so won't block on update
    def __init__(self, title, msg, maxItems):
        self._maxItems = maxItems
        self._app = wx.App()
        self._meter = wx.ProgressDialog(title, msg, maxItems,
                                  style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME |
                                        wx.PD_SMOOTH | wx.PD_APP_MODAL | wx.PD_ESTIMATED_TIME)

    # ------------------------- Update ------------------------------------- #
    # Does the heavy lifting of calling the wxProgressDialog                 #
    # BLOCKING - Note that the update WILL block on the final call until     #
    # users presses CLOSE button                                             #
    # ---------------------------------------------------------------------- #
    # todo make an option to self-close on completion so won't block on update
    def Update(self, msg, currentItemNumber):
        if not self._meter:
            print("*** UPDATE - trying to update an invalid meter ***")
            return False
        # -------------------------  in a real pickle. user is beyond max. This stops the bar  ------------------------- #
        #todo user thinks processing is done but the user program will continue. for now claiming the user cancelled
        if currentItemNumber > self._maxItems:
            self.not_cancelled = False
            self.skip = False
        else:
            (self.not_cancelled, self.skip) = self._meter.Update(currentItemNumber, newmsg=msg)
        if (currentItemNumber == self._maxItems):       # if at the max, close everything down
            self.__del__()
            return True
        return self.not_cancelled

    # ------------------------- Cancel ------------------------------------- #
    # Gives caller ability to cancel a meter early                           #
    # Result is that resources are freed by calling the normal object del    #
    # ---------------------------------------------------------------------- #
    def Cancel(self):
        self.__del__()

    # ------------------------- Delete ------------------------------------- #
    # ---------------------------------------------------------------------- #
    def __del__(self):
        try:
            self._meter.Destroy()
            self._app.Destroy()
            self._meter = None
        except:
            pass    # trouble destroying something

# ------------------------------------------------------------------------- #
#                       ProgressMeterCreate                                 #
# ------------------------------------------------------------------------- #
def ProgressMeterCreate(title, msg, maxItems):
    '''
    Create a progress meter that can be updated asynchronously (it's non-hlocking)
    Provides an early cancelling mechanism that's passed back through update call
    Meter will automatically close itself
    Returns a ProgressMeter object
    While not required to do, if caller wants to close the window then do that by setting the previously
        returned meter object to null:
        meter = []
    '''
    meter = ProgessMeter(title, msg, maxItems)
    return meter


# ---------------------------------------------------------------------- #
#                           ProgressMeterCreateAndUpdate                 #
# This is a ProgressMeter that does not require a "create" or open call  #
#   If user presses Cancel, function will close Meter for caller         #
#   To cancel early, set currentItemNumber = totalNumberItems            #
# ---------------------------------------------------------------------- #
def ProgressMeterCreateAndUpdate(title, msg, currentItemNumber, totalNumberItems):
    global already_opened
    global pmeter
    # -------------------------  Trick to see if this is first time call  ------------------------- #
    if 'pmeter' not in globals():
        # print(f'*** Creating Meter (First Time Through) ***')
        pmeter = ProgressMeterCreate(title, msg, totalNumberItems)
    # if we have a good progress meter, update it (is this needed?)
    if pmeter:
        not_cancelled = pmeter.Update(msg, currentItemNumber)
    else:
        not_cancelled = False
    # ------------------------- If at the max, get rid of the meter entirely  ------------------------- #
    # ------------------------- Need to delete the meter object for the user  ------------------------- #
    if not_cancelled is False or currentItemNumber == totalNumberItems:
        pmeter = []
        del pmeter      # remove from global namespace so that we'll be back to initialized state
    return not_cancelled


# ------------------------------------------------------------------------- #
#                       set_icon                                            #
# ------------------------------------------------------------------------- #

def set_icon(dlg, icon):
    if not icon:
        return
    if type(icon) is str:
        ico = wx.Icon(icon)
        dlg.SetIcon(ico)
        return
    if type(icon) == type(wx.Icon()):
        dlg.SetIcon(ico)
        return
    if hasattr(icon, "GetIcon"):
        dlg.SetIcon(icon.GetIcon())
        return
    return

# ------------------------------------------------------------------------- #
#                       ProgressBar class                                   #
# ------------------------------------------------------------------------- #

class ProgessBar:
    '''
    Display a Progress Meter without blocking
    Provides an early cancelling
    '''

    def __init__(self, title, msg, maxItems, icon=None):
        self._app = wx.App()
        self._meter = wx.GenericProgressDialog(title, msg, maxItems,
                                               style=wx.PD_CAN_ABORT
                                                     | wx.PD_ELAPSED_TIME
                                                     | wx.PD_AUTO_HIDE
                                                     | wx.PD_REMAINING_TIME
                                                     | wx.PD_ESTIMATED_TIME)
        self.maxitems = maxItems
        set_icon(self._meter, icon)

    def update(self, msg, currentItemNumber):
        if currentItemNumber > self.maxitems:  # we have already been closed
            return False

        if currentItemNumber > self.maxitems:  # no exception if number too high
            currentItemNumber = self.maxitems

        keepGoing, _ = self._meter.Update(currentItemNumber, newmsg=msg)

        return keepGoing
