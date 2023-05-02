import pyautogui as gui
import config

def moveFile():
    """
    Move the pdf into the folder
    :return: None
    """
    # put the pdf into its folder
    if config.pdfReady is None or config.pdfReady == ():
        config.pdfReady = lookFor('images/pdfLogo.png')

    # get the folder
    folderSelect = config.documentType + 'images/Folder.png'
    fileImage = lookFor(folderSelect)

    # if the folder is not found, take a new screenshot
    if fileImage is None:
        gui.alert('Ah! I couldn\'t find', folderSelect, '! If the folder looks empty instead of full of PDFs, '
                  'that\'s probably why. Please take a new screenshot of the folder and label it:', 'Winston',
                  'I\'ve taken a new screenshot')

    # move the pdf into the folder
    gui.moveTo(config.pdfReady)
    gui.dragTo(fileImage[0], fileImage[1] - 15, 0.3, button='left')


def waitToClick(pngName, xMod=0, yMod=0, conf=0.93, gray=True):
    """
    Wait for the png to appear, then click it
    :param pngName: (string) the name of the png to click
    :param xMod: (int) the x offset
    :param yMod: (int) the y offset
    :param conf: (float) the confidence
    :param gray: (boolean) whether the image is grayscale
    :return: (tuple) the center of the image
    """
    edges = None

    while edges is None:
        edges = gui.locateOnScreen(pngName, grayscale=gray, confidence=conf)

    clickLoc = gui.center(edges)

    return clickLoc[0] + xMod, clickLoc[1] + yMod


def lookFor(pngName):
    """
    Look for the png without clicking it
    :param pngName: (string) the name of the png to look for
    :return: (tuple) the center of the image
    """
    # if the file name is not visible, ask the user to make it visible
    center = gui.locateOnScreen(pngName, grayscale=True, confidence=0.93)

    if center is None:
        gui.alert('Huh. I couldn\'t find the ' + pngName + '. Please make sure it is visible, then click \'Ready\'',
                  'Winston', 'Ready')
        center = gui.locateOnScreen(pngName, grayscale=True, confidence=0.93)

    # return the center of the image
    return gui.center(center)