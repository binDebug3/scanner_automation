from utils.helpers import *
from utils.format import *
from utils.tracking import saveProgress


def inputDetails():
    """
    Inputs the details of the document
    :return: None
    """
    gui.PAUSE = config.FAST

    # find date button
    dateButton = getDateButton()

    # find save button
    saveDetails = lookFor('images/saveDetails.png')

    # check if this document needs to go to Carol
    checkForCarol()

    # only some documents need updates shipping information
    if config.documentType == 'SLP' or config.documentType == 'Note':
        updateShipping(dateButton, saveDetails)

    elif config.documentType == 'FNMA':
        updateFNMA(saveDetails)

    # save the progress
    saveProgress(5)


def getDateButton():
    """
    Finds the date button and clicks it
    :return: (tuple) the location of the date button
    """
    # Needs to be changed to docsDate3.png that has the two dots without checking above the dots
    dateButton = waitToClick('images/docsDate.png', 0, 20)
    config.safeSpace = (dateButton[0] + 40, dateButton[1] + 10)
    gui.click(config.safeSpace)

    return dateButton


def checkForCarol():
    """
    Checks if the document needs to go to Carol
    :return: None
    """
    carolDoc = gui.locateOnScreen('images/carol.png', grayscale=True, confidence=0.97)

    if carolDoc is not None:
        gui.alert('I just realized... this is a document for Carol!', 'Winston')


def updateShipping(dateButton, saveDetails):
    """
    Updates the shipping information for SLP and Note documents
    :param dateButton: (tuple) the location of the date button
    :param saveDetails: (tuple) the location of the save button
    :return: None
    """
    # update the date button if there is no date already
    if config.documentType == 'SLP':
        emptyDate = gui.locateOnScreen('images/emptyDate.png', grayscale=True, confidence=0.93)
        if emptyDate is not None:
            gui.doubleClick(dateButton)

    # paste the shipping information
    gui.click(waitToClick('images/shippingNotes.png', 485, 40))
    gui.typewrite(config.shippingDetails)
    gui.click(saveDetails)


def updateFNMA(saveDetails):
    """
    Updates the shipping information for FNMA documents
    :param saveDetails: (tuple) the location of the save button
    :return: None
    """
    # move to the shipping information
    slipnslide()

    # find empty deeds and titles
    deedEmpty = gui.locateOnScreen('images/blankDeedofTrust.png', grayscale=True, confidence=0.93)
    titleEmpty = gui.locateOnScreen('images/blankTitlePolicy.png', grayscale=True, confidence=0.93)

    # if there is no date, ask the user for the date
    if config.enterDate == '':
        config.enterDate = gui.prompt('Hmm. I couldn\'t find the date. Mind telling me?', 'Winston')

    # update deed
    if deedEmpty is not None:
        gui.click(gui.center(deedEmpty))
        gui.typewrite(formatDate(config.enterDate))
        if titleEmpty is None:
            gui.click(saveDetails)

    # update title
    if titleEmpty is not None:
        gui.click(gui.center(titleEmpty))
        gui.typewrite(formatDate(config.enterDate))
        gui.click(saveDetails)


def slipnslide():
    """
    Scroll to the shipping information
    :return:
    """
    gui.scroll(-100)
    startScroll = lookFor('images/hScrollBar.png')
    gui.moveTo(startScroll)
    gui.drag(230, 0, 0.2, button='left')