import time

from utils.tracking import *
from utils.helpers import *
from utils.format import addChar

def replaceFile():
    # initialize local variables
    exito = False
    gui.PAUSE = config.FAST

    # update pdf name
    if config.pdfName == '' or config.pdfName is None:
        replaceName = getLoanNumber()
    else:
        replaceName = config.pdfName

    while not exito:
        # check for replacement file error
        time.sleep(1)
        needTo = gui.locateOnScreen('images/replaceFilePop.png', grayscale=True, confidence=0.85)

        # if the pop up appears
        if needTo is not None:
            # close the pop up
            calibrateExit = gui.center(needTo)
            gui.click(calibrateExit[0] + 360, calibrateExit[1])

            # double click on the pdf
            if config.pdfReady == () or config.pdfReady is None:
                config.pdfReady = waitToClick('images/pdfLogo.png')
            gui.PAUSE = config.MEDIUM
            gui.click(config.pdfReady[0], config.pdfReady[1] + 30)
            gui.click(config.pdfReady[0], config.pdfReady[1] + 30)

            # update name
            replaceName = addChar(replaceName, '0')
            gui.typewrite(replaceName)
            gui.PAUSE = config.FAST
            gui.press('enter')

            # try moving the file again
            moveFile()

        else:
            exito = True