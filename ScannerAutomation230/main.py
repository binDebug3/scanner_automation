from utils.analytics import *
from utils.output import *
from steps import search, inputDetails, start, mergePDF, scan, replaceFile, store


def run():
    """
    This is the main function that runs the program. It will run through the steps of the program and then exit.
    :return:
    """
    openApp = False
    if openApp:
        openApps()

    if 0 <= config.resumePosition < 8:
        getProgress()
        saveProgress(config.resumePosition + 1, True)

    config.firstStep = getProgress()
    config.documentType = convertDoc(config.documentType)
    config.shippingDetails = ' Scanned ' + config.documentType + ' ' + config.todaysDate + ' ' + config.userInitials

    keepScanning = True
    while keepScanning:
        gui.PAUSE = config.MEDIUM
        gui.click(config.minimize)
        config.detailsPrinted = False

        if not config.progress.__contains__(1):
            replaceFile.replaceFile()
            start.start()

        if config.subType != 'Quit':
            if not config.progress.__contains__(2):
                search.search()

            scan.scan()

            if not config.progress.__contains__(5):
                inputDetails.inputDetails()

            if not config.progress.__contains__(6):
                mergePDF.mergePDF()

            if not config.progress.__contains__(7):
                store.storeDocuments()

        else:
            keepScanning = False

        viewCount()




try:
    run()
finally:
    gui.alert('Ah! Something in me broke!', 'Winston', 'RIP')
