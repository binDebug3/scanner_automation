import time

from utils.analytics import *
from utils.helpers import *
from utils.tracking import *


def storeDocuments():
    # useful variables
    gui.PAUSE = config.MEDIUM
    incDocCount()
    statusBar = waitToClick('images/docStauts.png', 70, 0)
    fileTypeBar = (statusBar[0] + 230, statusBar[1])
    descriptionBar = (statusBar[0] + 610, statusBar[1])
    storeButton = (statusBar[0] + 620, statusBar[1] + 568)

    # once the status bar is found, enter the information corresponding to the loan type
    gui.PAUSE = config.FAST
    if config.documentType == 'SLP':
        gui.click(fileTypeBar)
        gui.press('r')
        gui.click(waitToClick('images/preFundingPackage.png'))

    elif config.documentType == 'Note':
        gui.click(fileTypeBar)
        gui.press('o')
        gui.click(waitToClick('images/note.png'))

    elif config.documentType == 'FNMA' or config.documentType == 'GNMA':
        if config.documentType == 'FNMA':
            gui.click(statusBar)
            gui.press('a')
        gui.doubleClick(fileTypeBar)

        if config.subType == '':
            config.subType = getDeed()

        if config.subType == 'Title Policy':
            gui.press('g')
            gui.click(waitToClick('images/finalTitlePolicy.png'))

        else:
            gui.press('s')
            gui.click(waitToClick('images/recordedSecurity.png'))
            if config.documentType == 'FNMA':
                gui.click(descriptionBar)
                gui.hotkey('ctrl', 'a')
                gui.typewrite(config.subType)

    elif config.documentType == 'settlement':
        gui.click(fileTypeBar)
        gui.press('g')
        gui.click(waitToClick('images/finalSettlementStatement.png'))

    saveProgress(7)

    # ask for permission to store
    if config.permissionRequired:
        permission = False
        gui.PAUSE = 10

        while permission is False:
            permission = 'Would you like me to store', config.subType, config.pdfName, '?'
            confirmed = gui.confirm(permission, 'Winston', ['Yes', 'No'])

            if confirmed == 'Yes':
                permission = True
                gui.PAUSE = config.FAST

    gui.click(storeButton)
    scanSpeed = time.perf_counter() - config.startTime

    if scanSpeed > 500:
        if config.documentType == 'SLP':
            scanSpeed = 220
        else:
            scanSpeed = 62

    moveFile()

    # update a few variables for the next scan
    config.subType = ''
    saveProgress(0)
    modStats(scanSpeed)
    viewSpeed()