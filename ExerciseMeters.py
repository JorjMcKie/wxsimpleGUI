from time import *
import wxsimpleGUI_Extended as sgui

# ========================================================================== #
#  Sample program demonstrating all features of the simpleGUI Progress Meter #
#                                                                            #
#  Two types of meters - Single open and update call                         #
#                        Separate open and update calls                      #
#  The calling program can cancel meters that are in progress                #
#  Meters demonstrated here:                                                 #
#   1 - Single line function call. Meter 1 to 88. Autocloses                 #
#   2 - Single line function call. Meter 1 to 30. Waits at 30 for close      #
#   3 - Two line call, object version of meter. Cancels meter at 30 of 50
# ========================================================================== #

#-------------------------  First meter               ------------------------- #
# ------------------------- Uses 'single call' meter  ------------------------- #
max_value=88
for i in range(max_value):
    not_cancelled = sgui.ProgressMeterEasyCreateAndUpdate(f'My FIRST Single-Line Progress Meter',
                                                      f'This meter will go to {max_value} and will auto-close\nCount is {i+1} of {max_value}', i+1, max_value, True)
    if not_cancelled is False:
        print(f'Canelled with Count = {i}')
        break
    sleep(.1)

#-------------------------  Second meter                               ------------------------- #
# ------------------------- Single-call meter that does not autoclose  ------------------------- #
max_value=50
for i in range(max_value):
    not_cancelled = sgui.ProgressMeterEasyCreateAndUpdate(f'My SECOND Single-Line Progress Meter',
                                                          f'{i+1} of {max_value}\nThis meter will go to {max_value} and wait for user to close',
                                                          i+1, max_value, AutoClose=False)
    if not_cancelled is False:
        print(f'Canelled with Count = {i}')
        break
    sleep(.1)

# -------------------------  Third meter                                --------------------- #
# -------------------------  Uses Object Open/Update model              --------------------- #
# -------------------------  Cancels at 250 of 300                      --------------------- #
max_value=300
mymeter = sgui.ProgessMeter('THIRD Meter using object-style calls', 'Best to use the 2-line version of Progress Bar is a long delay before starting\nLike you are experiencing now', max_value, True)
sleep(5)
for i in range(max_value):
    not_cancelled = mymeter.Update(f'My SECOND meter is moving along.\nIt will abort soon at 250\nCount is {i+1}', i+1)
    if not_cancelled is False:
        print(f'Canelled second meter with Count = {i}')
        mymeter = None       # delete the meter object
        break
    if i == 250:             # simulate something event that requires Meter be cancelled early
        mymeter.Cancel()
        break
    sleep(.01)

#------------------------- Fourth meter                                      ------------------------- #
# ------------------------ Single-call meter that cancels at 100 of 300      ------------------------- #
max_value=300
for i in range(max_value):
    not_cancelled = sgui.ProgressMeterEasyCreateAndUpdate(f'LAST meter', f'My last meter is moving...and cancels itself at 100\nCount is {i+1}', i+1, max_value)
    if not_cancelled is False:
        print(f'Canelled third time with Count = {i}')
        break
    if i == 100:
        print('We\'re canceling the meter early...')
        sgui.ProgressMeterEasyCancel()
        break
    sleep(.05)

max_value = 100
mymeter = sgui.ProgessMeter('Title here', 'About to start doing something....', max_value, AutoClose=True)
for index in range(100):
    mymeter.Update(f'Meter is moving.  Now at {index+1} of {max_value}', index+1)

mymeter = []                    #  this destroy's the meter and thus closes


