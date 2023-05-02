from utils.output import *

def mergePDF():
    gui.PAUSE = config.FAST

    # wait until you see the pdf, then drag it to the loan page
    config.pdfReady = waitToClick('images/pdfLogo.png')

    # look for safe space on the screen to print details
    gui.PAUSE = config.SLOW
    if config.safeSpace is None or config.safeSpace == ():
        config.safeSpace = waitToClick('images/safeSpace.png', 0, 0, 0.99, False)

    if not config.detailsPrinted:
        printDetails()

    # drag the pdf to the loan page
    gui.moveTo(config.pdfReady)
    gui.dragTo(config.safeSpace[0], config.safeSpace[1], 0.5, button='left')

    # save progress
    saveProgress(6)