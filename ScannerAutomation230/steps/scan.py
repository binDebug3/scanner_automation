import time

from utils.helpers import *
from utils.output import *
from utils.tracking import saveProgress


def scan():
    # find the button locations
    scanButton = lookFor('images/scanButton.png')
    clearButton = (scanButton[0] + 950, scanButton[1])

    # start scanning a new document
    if 3 not in config.progress:
        startScanner(scanButton)

    if 4 not in config.progress:

        # look for the scanning window
        gui.PAUSE = 2
        moveOnInd = None
        scanWindow = gui.locateOnScreen('images/scanWindow.png', grayscale=True, confidence=0.93)
        confirmScan = ''

        while scanWindow is not None or moveOnInd is None:
            # wait until the scanning indicator has disappeared
            time.sleep(3)
            moveOnInd = gui.locateOnScreen('images/clearPDFButton.png', grayscale=False, confidence=0.93)
            scanWindow = gui.locateOnScreen('images/scanWindow.png', grayscale=True, confidence=0.93)
            scanError = gui.locateOnScreen('images/scanError.png', grayscale=False, confidence=0.78)

            to_break = checkError(scanError, clearButton)
            if to_break:
                break

        # once it is done, save the pdf file
        if confirmScan != 'Rescan':
            savePDF()

            # output scanning details
            if not config.detailsPrinted:
                printDetails()

            # clear pdf file from scanner
            clearPDF(clearButton)

            # update progress
            saveProgress(4)



# helper function ----------------------------------------------------------------------------------------------------

def startScanner(scanButton):
    # start the scan and then wait until the scanner indicates that it is done
    gui.PAUSE = config.MEDIUM
    gui.doubleClick(scanButton)
    saveProgress(3)

    # output scanning details
    if not config.detailsPrinted:
        printDetails()

    # wait for scanner
    time.sleep(10)


def checkError(scanError, clearButton):
    # if a scan error appeared, notify the user
    if scanError is not None and scanError[1] > 400:
        gui.moveTo(gui.center(scanError))
        confirmScan = gui.confirm('Oh no! I noticed a scanning error. Rescan?', 'Winston', ['Rescan', 'No thanks'])

        # rescan if necessary
        if confirmScan == 'Rescan':
            rescan(clearButton)
            return True

    return False


def rescan(clearButton):
    gui.press('enter')
    gui.doubleClick(clearButton)
    gui.press('enter')

    # update progress status and scan
    saveProgress(2, True)
    scan()


def savePDF():
    gui.PAUSE = config.FAST
    gui.doubleClick(waitToClick('images/savePDFile.png', 0, 0, 0.93, False))
    gui.click(waitToClick('images/nameSavedFileBar.png', 0, -10))

    # update pdf name
    if config.pdfName == '' or config.pdfName is None:
        with open('pickles/loanNumber.pk', 'rb') as fi:
            config.pdfName = pickle.load(fi)

    # save pdf with pdf name
    gui.typewrite(config.pdfName)
    gui.PAUSE = config.SLOW
    gui.press('enter')


def clearPDF(clearButton):
    # wait for the pdf to save, then clear the scanner pdf file
    gui.PAUSE = config.FAST
    pdfSaving = ()
    if config.documentType == 'SLP':
        time.sleep(6)

    # wait for pdf saving animation to disappear
    while pdfSaving is not None:
        pdfSaving = gui.locateOnScreen('images/savePdfProgress.png', grayscale=True, confidence=0.93)

    # clear
    gui.doubleClick(clearButton)
    gui.press('enter')