from wxsimpleGUI import *


# ---------------------------------------------------------------------- #
#                           ProgressMeterEasyCreateAndUpdate             #
# Makes and/or updates an EASY progress meter                            #
# This is a ProgressMeter that does not require a "create" or open call  #
#   If user presses Cancel, function will close Meter for caller         #
#   To cancel early, set currentItemNumber = totalNumberItems            #
# ---------------------------------------------------------------------- #
def ProgressMeterEasyCreateAndUpdate(title, msg, currentItemNumber, totalNumberItems, AutoClose = False):
    global already_opened
    global pmeter
    # -------------------------  Trick to see if this is first time call  ------------------------- #
    if 'pmeter' not in globals():
        pmeter = ProgessMeter(title, msg, totalNumberItems, AutoClose)
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


# ---------------------------------------------------------------------- #
# ProgressMeterEasyCancel()                                              #
#   Cancels a previously made 'EASY Progress Bar'                        #
# ---------------------------------------------------------------------- #
def ProgressMeterEasyCancel():
    global pmeter

    if 'pmeter' in globals():
        pmeter.Cancel()

    return


