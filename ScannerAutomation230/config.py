import pyautogui as gui
from datetime import date
gui.FAILSAFE = True


# You can change the variables below -----------------------------------------------------------------------------------

goFast = True
complimentOn = True                         # Get a compliment or fun fact with each scan
permissionRequired = True                  # True tells Winston to ask for permission before finishing
resumePosition = 0

# 0 to restart, -1, 8, or 9 to resume
documentType = 'Pre Funding Package'        # Copy and paste from the options below
enterDate = '102721'                        # Format: MMDDYY
userInitials = 'KS'

# Document Type Options:    Pre Funding Package   |   FNMA   |   GNMA   |   Note   |   Final Settlement


# End of the variables you can change ----------------------------------------------------------------------------------












# Set speeds
FAST = 2
MEDIUM = 2
SLOW = 3
if goFast:
    FAST = 0.1
    MEDIUM = 1
    SLOW = 3
# Instantiate input variables
duplicate = False
detailsPrinted = False
safeSpace = ()
pdfReady = ()
progress = ()
enterComment = ()
minimize = (1247, 11)
pdfName = ''
documentID = ''
subType = ''
buyerFirst = ''
buyerLast = ''
propertyName = ''
shippingDetails = ''
todaysDate = date.today().strftime("%m/%d/%Y")
fileName = 'pickles/progress.pk'
startDate = '05/25/22'
startTime = 0
firstStep = 0
startIndex = 0