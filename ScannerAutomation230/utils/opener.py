from utils.format import convertDoc
from utils.helpers import *
from utils.tracking import *


def openApps():
    """
    Opens the apps needed for the day
    :return: None
    """
    # wait for things to load
    gui.PAUSE = 1
    gui.click(config.minimize)
    scannerApp = waitToClick('images/scannerLogo.png')
    byteApp = lookFor('images/byteLogo.png')
    commentBox = lookFor('images/openCommentBox.png')

    # open the apps
    gui.doubleClick(commentBox)
    gui.doubleClick(scannerApp)
    gui.PAUSE = config.SLOW
    gui.doubleClick(byteApp)

    # wait for the user
    gui.alert('Good morning, Winston here! Please start by entering your byte password:', 'Winston', 'I signed in!')
    # scanTime = {'SLP': 0, 'FNMA': 0, 'GNMA': 0, 'settlement': 0, 'Note': 0}
    # with open('scanTime.pk', 'wb') as fi:
    #     pickle.dump(scanTime, fi)


def initialize():
    # open up required apps if they aren't already
    openApp = False
    if openApp:
        openApps()

    # check for incomplete scans
    if 0 <= config.resumePosition < 8:
        getProgress()
        saveProgress(config.resumePosition + 1, True)

    # reset variables based on progress
    config.firstStep = getProgress()
    config.documentType = convertDoc(config.documentType)
    config.shippingDetails = ' Scanned ' + config.documentType + ' ' + config.todaysDate + ' ' + config.userInitials


def minimize():
    gui.PAUSE = config.MEDIUM
    gui.click(config.minimize)
    config.detailsPrinted = False