import time

from utils.output import *
from utils.tracking import saveProgress


def scan():
    scanButton = lookFor('images/scanButton.png')
    clearButton = (scanButton[0] + 950, scanButton[1])

    if not config.progress.__contains__(3):
        # start the scan and then wait until the scanner indicates that it is done
        gui.PAUSE = config.MEDIUM
        gui.doubleClick(scanButton)
        saveProgress(3)

        if not config.detailsPrinted:
            printDetails()

        time.sleep(10)

    if not config.progress.__contains__(4):
        gui.PAUSE = 2
        moveOnInd = None
        scanWindow = gui.locateOnScreen('images/scanWindow.png', grayscale=True, confidence=0.93)
        confirmScan = ''

        while scanWindow is not None or moveOnInd is None:
            time.sleep(3)
            moveOnInd = gui.locateOnScreen('images/clearPDFButton.png', grayscale=False, confidence=0.93)
            scanWindow = gui.locateOnScreen('images/scanWindow.png', grayscale=True, confidence=0.93)
            scanError = gui.locateOnScreen('images/scanError.png', grayscale=False, confidence=0.78)

            if scanError is not None and scanError[1] > 400:
                gui.moveTo(gui.center(scanError))
                confirmScan = gui.confirm('Oh no! I noticed a scanning error. Rescan?', 'Winston', ['Rescan', 'No thanks'])

                if confirmScan == 'Rescan':
                    gui.press('enter')
                    gui.doubleClick(clearButton)
                    gui.press('enter')
                    saveProgress(2, True)
                    scan()
                    break

        # once it is done, save the pdf file
        if confirmScan != 'Rescan':
            gui.PAUSE = config.FAST
            gui.doubleClick(waitToClick('images/savePDFile.png', 0, 0, 0.93, False))
            gui.click(waitToClick('images/nameSavedFileBar.png', 0, -10))

            if config.pdfName == '' or config.pdfName is None:
                with open('pickles/loanNumber.pk', 'rb') as fi:
                    config.pdfName = pickle.load(fi)

            gui.typewrite(config.pdfName)
            gui.PAUSE = config.SLOW
            gui.press('enter')

            if not config.detailsPrinted:
                printDetails()

            gui.PAUSE = config.FAST
            # wait for the pdf to save, then clear the scanner pdf file
            pdfSaving = ()
            if config.documentType == 'SLP':
                time.sleep(6)

            while pdfSaving is not None:
                pdfSaving = gui.locateOnScreen('images/savePdfProgress.png', grayscale=True, confidence=0.93)

            gui.doubleClick(clearButton)
            gui.press('enter')

            saveProgress(4)