
# You can change the variables below -----------------------------------------------------------------------------------


goFast = True                           # True to go as fast as possible, or go slow enough for user intervention
complimentOn = True                     # True will print a compliment or fun fact with each scan
permissionRequired = True               # True tells Winston to ask for permission before finishing

# 0 to restart, -1, 8, or 9 to resume. 1-7 are specific steps (see README for more details)
resumePosition = 9                      # use this to tell Winston exactly where to restart, options above


# Document Type Options:    Pre Funding Package   |   FNMA   |   GNMA   |   Note   |   Final Settlement
documentType = 'Pre Funding Package'    # The type of document you want to scan. Copy and paste from the options above

enterDate = '051523'                    # Today's date in MMDDYY format

userInitials = 'LS'                     # your initials to sign your scanned documents with




# End of the variables you can change ----------------------------------------------------------------------------------










import pyautogui as gui
from datetime import date
gui.FAILSAFE = True

# Set click speeds
FAST = 2
MEDIUM = 2
SLOW = 3
if goFast:
    FAST = 0.1
    MEDIUM = 1
    SLOW = 3


# booleans for handling and tracking certain states or conditions
duplicate = False
detailsPrinted = False

# tuples for common click locations
safeSpace = ()
pdfReady = ()
progress = []
enterComment = ()
minimize = (1247, 11)

# strings for storing document information
pdfName = ''
documentID = ''
subType = ''
buyerFirst = ''
buyerLast = ''
propertyName = ''
shippingDetails = ''

# strings for storing scanning information that won't be modified
todaysDate = date.today().strftime("%m/%d/%Y")
fileName = 'pickles/progress.pk'

# integers for determining starting positions
startTime = 0
firstStep = 0
startIndex = 0
