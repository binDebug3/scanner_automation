import random

from utils.fun import funCompliments
from utils.tracking import *
from utils.format import *
    
    
def printDetails():
    """
    Print out scanning status and details on a note
    :return: None
    """
    gui.PAUSE = config.FAST
    
    # look for the comment box
    if config.enterComment is None or config.enterComment == ():
        commentBox = gui.locateOnScreen('images/commentBox.png', grayscale=True, confidence=0.9)
        
        if commentBox is not None:
            config.enterComment = gui.center(commentBox)
            
    # Print the details
    if config.enterComment is not None and config.enterComment != ():
        gui.click(1335, config.enterComment[1] - 35)

        # clear the comment box
        gui.hotkey('ctrl', 'a')
        gui.press('backspace')

        # update pdfName and subType
        if config.pdfName == '':
            config.pdfName = getLoanNumber()
        if config.subType == '':
            config.subType = getDeed()
            
        # Document Details
        typeDocument()
        # Status Report
        typeStatus()
        # Scanning Speed
        typeSpeed()
        # Compliment
        typeCompliment()

    # if the comment box is not found, alert the user
    else:
        gui.alert('Hey! I want to talk to you! Would you mind opening my notepad? It\'s labeled \'Winston\'', 'Winston',
                  'Oops')


def typeDocument():
    """
    Helper function to print document details
    :return: None
    """
    # print document type and pdf name
    gui.typewrite('Hey! It\'s Winston again. I value transparency so here\'s what I\'ve got.\n\n'
                  'Document Type: ' + config.documentType + '\nLoan Number: ' + config.pdfName + '\n')

    # print subtype and date
    if config.documentType == 'FNMA':
        gui.typewrite('Deed: ' + config.subType + '\nDate: ' + formatDate(config.enterDate) + '\n')


def typeStatus():
    """
    Helper function to print scanning status
    :return: None
    """
    # start status report
    gui.typewrite('Status: ')
    printProgress = getProgress(False)

    # check the success of the last scan and report step number
    if config.resumePosition == 0:
        gui.typewrite('Forced restart')
    elif 0 < config.resumePosition < 8 and 0 < printProgress < 8:
        gui.typewrite('Started at step ' + str(config.resumePosition))
    elif 8 > config.resumePosition > 0 == printProgress:
        gui.typewrite('Normal start')
    else:
        gui.typewrite('Auto-resume (' + str(config.firstStep) + ')')

    gui.typewrite('\n')


def typeSpeed():
    """
    Helper function to print scanning speed
    :return: None
    """
    # open speed data
    with open('pickles/scanLastSpeed.pk', 'rb') as fi:
        scanSpeed = pickle.load(fi)

    # append seconds if they are less than 60
    if scanSpeed < 60:
        first = round(scanSpeed, 2)
        displaySpeed = str(first) + ' seconds'

    # otherwise, convert to minutes
    else:
        seconds = int(scanSpeed % 60)
        disMinutes = int((scanSpeed - seconds) / 60)
        if disMinutes > 10:
            print('Weird result:  ScanSpeed: ' + str(scanSpeed) + ' | Seconds: ' + str(seconds)
                  + ' | DisMinutes: ' + str(disMinutes))
            displaySpeed = '<error>'

        else:
            if seconds < 10:
                zero = '0'
            else:
                zero = ''

            displaySpeed = str(disMinutes) + ':' + zero + str(seconds) + ' minutes'

    gui.typewrite('Last scan: ' + displaySpeed + '\n')


def typeCompliment():
    """
    Helper function to print a compliment
    :return: None
    """
    # initialize indices for compliments and fun facts
    if config.complimentOn:
        if config.startIndex == 0:
            config.startIndex = 600
        else:
            config.startIndex = 0

        # build a fun fact string
        index = random.randint(config.startIndex, len(funCompliments) - 1)
        if index > 106:
            insert = 'Also, did you know? :D\n'
            end = '.'
            factID = '#' + str(index - 104)

        # build a compliment string
        else:
            insert = 'Anyways, I was just thinking\n'
            end = ' :)'
            factID = ''

        # output compliment and fun fact
        gui.typewrite('\n\n' + insert + funCompliments[index] + end + '\n' + factID)
    config.detailsPrinted = True
        
        
def printMessage(message):
    """
    Prints a message to the comment box
    :param message: (string) the message to print
    :return: None
    """
    gui.PAUSE = config.FAST

    # look for comment box
    if config.enterComment is None or config.enterComment == ():
        commentBox = gui.locateOnScreen('images/commentBox.png', grayscale=True, confidence=0.9)
        if commentBox is not None:
            config.enterComment = gui.center(commentBox)

    # click on comment box and print message
    if config.enterComment is not None and config.enterComment != ():
        gui.click(1335, config.enterComment[1] - 35)
        gui.typewrite('\n' + message)