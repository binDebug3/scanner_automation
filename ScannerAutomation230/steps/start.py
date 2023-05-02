import time

from utils.output import *


def start():
    # useful variables
    confirm = None
    config.duplicate = False
    config.firstStep = 0
    gui.PAUSE = config.FAST

    # while we haven't gotten the input we need...
    while confirm is None:

        # Get the document type, (and deed type if applicable), and set the shipping details
        if config.documentType == 'FNMA':
            while config.subType == '' or config.subType is None:
                config.subType = gui.confirm('Hey there! Please enter the deed type', 'Winston',
                                      ['Original', 'Copy', 'Title Policy', 'Quit'])
            if config.subType == 'Quit':
                break

        # start the timer
        config.startTime = time.perf_counter()

        # get the loan number
        config.pdfName = gui.prompt(
            'Hi! Winston here. I\'m your personal scanning assistant :)\nbrought to you by Dallin Stewart (2022)\n\n'
            'Please enter the loan number in lowercase ex: \trce123456\n'
            'or enter \'1\' to search for the previous loan number, or \'4\' to skip', 'Winston')
        confirm = ''

        # update variables that modify future actions slightly, and get personal info if necessary
        if config.pdfName == '4':
            enterByName()
            config.documentID = '4'
            confirm = ''
            continue

        elif config.pdfName == '1':
            config.pdfName = getLoanNumber()
            confirm = ''

        elif config.pdfName is None:
            config.subType = 'Quit'
            break

        elif not config.pdfName[len(config.pdfName) - 3].isdigit():
            confirm = None
            continue

        # save details and progress
        saveDetails()
        saveProgress(1)


def saveDetails():
    """
    Saves the pdf name and the deed type to pickles
    :return: None
    """
    # format the loan number and pdf name with capitalization and * as needed
    config.documentID = addChar(config.pdfName, '*')
    config.pdfName = addChar(config.pdfName, '')

    # check if the pdf name is a duplicate
    if config.pdfName == getLoanNumber():
        config.pdfName = addChar(config.pdfName, '0')
        config.duplicate = True

    # save the pdfName and the subtype to pickles
    with open('pickles/loanNumber.pk', 'wb') as fi:
        pickle.dump(config.pdfName, fi)
    with open('pickles/deed.pk', 'wb') as fi:
        pickle.dump(config.subType, fi)