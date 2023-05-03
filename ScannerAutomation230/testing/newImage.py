import pyautogui as gui
gui.FAILSAFE = True

windows = ['Scanner', 'Byte Search', 'Byte File', 'Store File', 'Other']
scannerImages = ['Clear Button','Name a File', 'No Paper Error', 'Paper Stream Error','Save PDF', 'Progress Bar',
                 'Scan Button', 'Scanning Window', 'Cancel']
searchImages = ['Byte Clear Button', 'Not Responding Error', 'Search Bar', 'Search Result', 'Result File Name', 'Cancel']
byteImages = ['Document Date Button', 'Shipping Duplicate', 'Shipping Notes', 'Empty Date', 'Close Button', 'Cancel']
storeImages = ['Description', 'Status', 'Type', 'Title Policy', 'Note', 'Pre Funding', 'RSI', 'Store', 'Cancel']
otherImages = ['Fake', 'File Folder', 'PDF Image', 'Cancel']

def takeSnapShot(imageName):
    gui.alert('Move the cursor to the top left corner of the area you would like to capture, then hit \'Enter\'')
    topLeft = gui.position()
    gui.alert('Now move the cursor to the bottom right corner of the area you would like to capture, and hit \'Enter\'')
    bottomRight = gui.position()
    width = bottomRight[0] - topLeft[0]
    height = bottomRight[1] - topLeft[1]
    newImage = gui.screenshot(region=(topLeft[0], topLeft[1], width, height))
    newImage.save(r'C:\Users\scannerpc\PycharmProjects\ScannerAutomation230\\' + imageName + '.png')


def instructions():
    gui.alert('The instructions have not been written yet.')


def convertName(imageName):
    if imageName == 'Byte Clear Button':
        return 'clearButton'
    elif imageName == 'Fake':
        return 'fake'
    elif imageName == 'Clear Button':
        return 'clearPDFButton'
    elif imageName == 'Description':
        return 'docDescription'
    elif imageName == 'Document Date Button':
        return 'docsDate'
    elif imageName == 'Status':
        return 'docStauts'
    elif imageName == 'Type':
        return 'docType'
    elif imageName == 'Empty Date':
        return 'emptyDate'
    elif imageName == 'File Folder':
        return 'fileLogo'
    elif imageName == 'Result File Name':
        return 'fileName'
    elif imageName == 'Title Policy':
        return 'finalTitlePolicy'
    elif imageName == 'Name a File':
        return 'nameSavedFileBar'
    elif imageName == 'No Paper Error':
        return 'noPaper'
    elif imageName == 'Note':
        return 'note'
    elif imageName == 'Not Responding Error':
        return 'notResponding'
    elif imageName == 'Paper Stream Error':
        return 'paperStreamError'
    elif imageName == 'PDF Image':
        return 'pdfLogo'
    elif imageName == 'Pre Funding':
        return 'preFundingPackage'
    elif imageName == 'RSI':
        return 'recordedSecurity'
    elif imageName == 'Close Button':
        return 'returnToSearch'
    elif imageName == 'Save PDF':
        return 'savePDFile'
    elif imageName == 'Progress Bar':
        return 'savePdfProgress'
    elif imageName == 'Scan Button':
        return 'scanButton'
    elif imageName == 'Scanning Window':
        return 'scanWindow'
    elif imageName == 'Search Bar':
        return 'searchBar'
    elif imageName == 'Search Result':
        return 'searchResult'
    elif imageName == 'Shipping Duplicate':
        return 'shippingDup'
    elif imageName == 'Shipping Notes':
        return 'shippingNotes'
    elif imageName == 'Store':
        return 'storeNewDocuments'
    else:
        print('Error converting names')
        return 'error'


def removeButton(imageName):
    if imageName in scannerImages:
        scannerImages.remove(imageName)
    elif imageName in byteImages:
        byteImages.remove(imageName)
    elif imageName in storeImages:
        storeImages.remove(imageName)
    elif imageName in otherImages:
        otherImages.remove(imageName)
    elif imageName in searchImages:
        searchImages.remove(imageName)
    else:
        print('Error removing the button')



def runMenu():
    keepSaving = True
    imageName = 'Cancel'
    while keepSaving:
        while imageName == 'Cancel':
            imageLoc = gui.confirm('Which window is the image in?', 'Select Window', windows)
            if imageLoc == 'Scanner':
                imageName = gui.confirm('Select an image to retake:', 'Scanner Images', scannerImages)
            elif imageLoc == 'Byte Search':
                imageName = gui.confirm('Select an image to retake:', 'Byte Search Images', searchImages)
            elif imageLoc == 'Byte File':
                imageName = gui.confirm('Select an image to retake:', 'Byte File Images', byteImages)
            elif imageLoc == 'Store File':
                imageName = gui.confirm('Select an image to retake:', 'Store File Images', storeImages)
            elif imageLoc == 'Other':
                imageName = gui.confirm('Select an image to retake:', 'Store File Images', otherImages)
            else:
                break
        if imageName is None or imageLoc is None:
            break
        removeButton(imageName)
        pngName = convertName(imageName)
        takeSnapShot(pngName)
        okay = gui.confirm('Would you like to save another image?')
        imageName = 'Cancel'
        if okay == 'Cancel' or okay is None:
            keepSaving = False

instructions()
runMenu()
