import time

from utils.analytics import *
from utils.helpers import *
from utils.tracking import *


def storeDocuments():
    """
    Store the scanned and annotated document in the system
    :return: None
    """
    # useful variables
    gui.PAUSE = config.MEDIUM
    incDocCount()

    # wait for the status bar to appear, then extrapolate other positions
    statusBar = waitToClick('images/docStauts.png', 70, 0)
    fileTypeBar = (statusBar[0] + 230, statusBar[1])
    descriptionBar = (statusBar[0] + 610, statusBar[1])
    storeButton = (statusBar[0] + 620, statusBar[1] + 568)


    # set document type and information
    setDocInfo(fileTypeBar, descriptionBar, statusBar)

    # save progress
    saveProgress(7)

    # ask for permission to store
    getPermission()
    # store the file
    gui.click(storeButton)

    # get total scanning time
    stopTimer()

    # move the file
    moveFile()

    # update a few variables for the next scan
    config.subType = ''
    saveProgress(0)
    viewSpeed()



# helper functions ---------------------------------------------------------------------------------------------------


def setDocInfo(fileTypeBar, descriptionBar, statusBar):
    # once the status bar is found, enter the information corresponding to the loan type
    gui.PAUSE = config.FAST
    if config.documentType == 'SLP':
        gui.click(fileTypeBar)
        gui.press('r')
        gui.click(waitToClick('images/preFundingPackage.png'))

    # save the pdf as a note
    elif config.documentType == 'Note':
        gui.click(fileTypeBar)
        gui.press('o')
        gui.click(waitToClick('images/note.png'))

    # save the file as a FNMA
    elif config.documentType == 'FNMA' or config.documentType == 'GNMA':
        saveFNMA(fileTypeBar, descriptionBar, statusBar)

    # save the file as a settlement
    elif config.documentType == 'settlement':
        gui.click(fileTypeBar)
        gui.press('g')
        gui.click(waitToClick('images/finalSettlementStatement.png'))


def saveFNMA(fileTypeBar, descriptionBar, statusBar):
    """
    Save a file as a FNMA document
    :param fileTypeBar: (tuple) center of the file type bar
    :param descriptionBar: (tuple) center of the description bar
    :param statusBar: (tuple) center of the status bar
    :return: None
    """
    # if the document is a FNMA, select a from the status menu
    if config.documentType == 'FNMA':
        gui.click(statusBar)
        gui.press('a')

    # move on to file type
    gui.doubleClick(fileTypeBar)
    if config.subType == '':
        config.subType = getDeed()

    # save the file as a title policy
    if config.subType == 'Title Policy':
        gui.press('g')
        gui.click(waitToClick('images/finalTitlePolicy.png'))

    # save the file as a recorded security
    else:
        gui.press('s')
        gui.click(waitToClick('images/recordedSecurity.png'))
        if config.documentType == 'FNMA':
            gui.click(descriptionBar)
            gui.hotkey('ctrl', 'a')
            gui.typewrite(config.subType)


def getPermission():
    """
    Requests permission from the user to finish the scanning process
    :return: None
    """
    # check if permission is even necessary
    if config.permissionRequired:
        permission = False
        gui.PAUSE = 10

        # wait until permission to continue has been granted
        while permission is False:
            permission = 'Would you like me to store', config.subType, config.pdfName, '?'
            confirmed = gui.confirm(permission, 'Winston', ['Yes', 'No'])

            if confirmed == 'Yes':
                permission = True
                gui.PAUSE = config.FAST


def stopTimer():
    """
    Computes the total scanning time, handling errors and interruptions
    :return: None
    """
    # stop the timer
    scanSpeed = time.perf_counter() - config.startTime

    # if there was an interruption and scanning went too long, save the scanning speed as a rough average
    if scanSpeed > 500:
        if config.documentType == 'SLP':
            scanSpeed = 220
        else:
            scanSpeed = 62

    # update scanning statistics
    modStats(scanSpeed)