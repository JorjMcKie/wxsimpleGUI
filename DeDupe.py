import hashlib
import os
import wxsimpleGUI as sgui


DEFAULT_INPUT_PATH = 'C:\\- PDFS -\\Pics - Holbens Extracted FAST'


# ====____====____==== FUNCTION DeDuplicate_folder(path) ====____====____==== #
# Function to de-duplicate the folder passed in                               #
# --------------------------------------------------------------------------- #
def DeDuplicate_folder(path):
    shatab = []
    dup_count = 0
    total = 0
    small = 2048
    small_count = 0
    pngdir = path
    if not os.path.exists(path):
        sgui.MsgBox('De-Dupe', '** Folder doesn\'t exist\n%s' % path)
        return
    pngfiles = os.listdir(pngdir)
    total_files = len(pngfiles)
    msg = f'Deduplicating 0 of {total_files} files'
    # pmeter = sgui.ProgressMeterCreate('Deduplication progress', msg, total_files)
    for idx, f in enumerate(pngfiles):
        msg = f'Deduplicating {idx+1} of {total_files} files\n' f'{dup_count} Dupes found\n' f'{small_count} Too small'
        not_cancelled = sgui.ProgressMeterCreateAndUpdate('De-dupe', msg, idx+1, total_files)
        # not_cancelled = pmeter.Update(msg, idx)
        if not not_cancelled:
            break
        if not f.endswith(".png") and not f.endswith(".jpg"):
            continue
        total += 1
        fname = os.path.join(pngdir, f)
        x = open(fname, "rb").read()

        if len(x) <= small:     # removing due to too small
            small_count += 1
            os.remove(fname)
            continue

        m = hashlib.sha256()
        m.update(x)
        f_sha = m.digest()
        if f_sha in shatab:     # DUPLICATE found so remove
            os.remove(fname)
            dup_count += 1
            continue
        shatab.append(f_sha)


    end_reason = ('**User Cancelled**', 'Completed Normally')[not_cancelled is True]
    msg = f'{end_reason}\n'\
          f'{total} Files processed\n'\
          f'{dup_count} Duplicates found\n'\
          f'{small_count} Removed because too small'
    sgui.MsgBox('Duplicate Finder Ended', msg)

# ====____====____==== Pseudo-MAIN program ====____====____==== #
# This is our main-alike piece of code                          #
#   + Starts up the GUI                                         #
#   + Gets values from GUI                                      #
#   + Runs DeDupe_folder based on GUI inputs                    #
# ------------------------------------------------------------- #
if __name__ == '__main__':
    source_folder = sgui.InputBox('DeDuplicate a Folder\'s image files', 'Please enter path to folder you wish to De-Duplicate', DEFAULT_INPUT_PATH)
    print('Exited GUI... Beginning de-dupe')
    if source_folder is not None:
        DeDuplicate_folder(source_folder)
    else:
        sgui.MsgBox('Cancelling', '*** Cancelling ***')
        print('Exiting without doing de-duplicate')
    exit(0)
