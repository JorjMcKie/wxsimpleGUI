import time
import wxsimpleGUI as sgui

# ========================================================================== #
#  Sample program demonstrating all features of the simpleGUI Progress Meter #
#  Two types of meters:  a single function call and traditional object call  #
# ========================================================================== #

#-------------------------  First meter counts to 30  ------------------------- #
# ------------------------- Uses 'single call' meter  ------------------------- #
for i in range(30):
    not_cancelled = sgui.ProgressMeterCreateAndUpdate(f'This is my FIRST meter',
                                                      f'My meter is moving along\nand will compelte\nCount is {i+1}', i+1, 30)
    if not_cancelled is False:
        print(f'Canelled with Count = {i}')
        break
    time.sleep(.1)

# -------------------------  Second meter aborts at 100 out of 300  ------------------------- #
# -------------------------  Uses 'traditional call' meter          ------------------------- #

mymeter = sgui.ProgressMeterCreate('SECOND Old style', 'message', 300)
for i in range(300):
    not_cancelled = mymeter.Update(f'My SECOND meter is moving along.\nIt will abort soon at 100\nCount is {i+1}', i+1)
    if not_cancelled is False:
        print(f'Canelled second meter with Count = {i}')
        mymeter = None
        break
    if i == 100:             # simulate something event that requires Meter be cancelled early
        mymeter.Cancel()
        break
    time.sleep(.1)
#------------------------- Third meter counts to 300 aborts at 50  ------------------------- #
# ------------------------- Uses 'single call' meter               ------------------------- #
for i in range(300):
    not_cancelled = sgui.ProgressMeterCreateAndUpdate(f'THIRD meter', f'My #3 meter is moving along and cancels at 50\nCount is {i+1}', i+1, 300)
    if not_cancelled is False:
        print(f'Canelled third time with Count = {i}')
        break
    if i == 50:
        print('simulated program cancel')
        # to end a meter early, set current item = total items
        sgui.ProgressMeterCreateAndUpdate(f'THIRD meter', f'Ending meter early', 300, 300)
        break
    time.sleep(.1)
