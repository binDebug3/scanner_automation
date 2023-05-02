import pyautogui as gui

import config


def convertDoc(scanType):
    """
    Converts the scan type to the corresponding document type
    :param scanType: (string) the type of document to scan
    :return: 
    """
    if scanType == 'Pre Funding Package':
        return 'SLP'
    elif scanType == 'Note':
        return 'Note'
    elif scanType == 'FNMA':
        return 'FNMA'
    elif scanType == 'GNMA':
        return 'GNMA'
    elif scanType == 'Final Settlement':
        return 'settlement'
    else:
        return ''
    
    
def addChar(pdfNamePar, insert):
    """
    Adds a character to the pdf name
    :param pdfNamePar: (string) the name of the pdf
    :param insert: (string) the character to insert
    :return: (string) the new pdf name
    """
    # initialize local variables
    length = len(pdfNamePar)
    firstNum = 0
    
    # find the first number in the pdf name
    for i in range(length):
        if pdfNamePar[i].isdigit():
            firstNum = i
            break
            
    # remove the asterisk from the pdf name
    pdfNamePar.replace('*', '')
    
    # insert the character and return
    return pdfNamePar[:firstNum].upper() + insert + pdfNamePar[firstNum:]


def enterByName():
    """
    Enters the buyer's name and the property name
    :return: None
    """
    gui.PAUSE = config.FAST

    # enter the buyer's name and the property name
    config.buyerFirst = gui.prompt('Okay. Input the buyer\'s first name then, or hit Enter to skip', 'Winston')
    if config.buyerFirst is None:
        config.buyerFirst = ''

    # enter the buyer's last name
    config.buyerLast = gui.prompt('Now write the buyer\'s last name, or hit Enter again to skip', 'Winston')
    if config.buyerLast is None:
        config.buyerLast = ''

    # enter the property name
    config.propertyName = gui.prompt('Almost done. Go ahead and type the property name, or hit Enter to skip', 'Winston')
    if config.propertyName is None:
        config.propertyName = ''
        
        
def formatDate(day):
    """
    Formats the date to be in the format MM/DD/YYYY
    :param day: (string) the date to format
    :return: (string) the formatted date
    """
    return day[0] + day[1] + '/' + day[2] + day[3] + '/20' + day[4] + day[5]