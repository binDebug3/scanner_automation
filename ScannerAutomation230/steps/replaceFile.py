import time

from utils.tracking import *
from utils.helpers import *
from utils.format import addChar

def replaceFile():
    exito = False
    gui.PAUSE = config.FAST

    if config.pdfName == '' or config.pdfName is None:
        replaceName = getLoanNumber()
    else:
        replaceName = config.pdfName
    while not exito:
        time.sleep(1)
        needTo = gui.locateOnScreen('images/replaceFilePop.png', grayscale=True, confidence=0.85)
        if needTo is not None:
            calibrateExit = gui.center(needTo)
            gui.click(calibrateExit[0] + 360, calibrateExit[1])
            if config.pdfReady == () or config.pdfReady is None:
                config.pdfReady = waitToClick('images/pdfLogo.png')
            gui.PAUSE = config.MEDIUM
            gui.click(config.pdfReady[0], config.pdfReady[1] + 30)
            gui.click(config.pdfReady[0], config.pdfReady[1] + 30)
            replaceName = addChar(replaceName, '0')
            gui.typewrite(replaceName)
            gui.PAUSE = config.FAST
            gui.press('enter')
            moveFile()
        else:
            exito = True