import time

from utils.output import *
from utils.helpers import *
from utils.tracking import *
from utils.format import *


def search():
    """
    Searches for the loan in the system
    :return: 
    """
    # if we are scanning a different document for the same loan, skip the search step
    gui.PAUSE = config.SLOW
    yaSearch = gui.locateOnScreen('images/clearButton.png', grayscale=True, confidence=0.93)
    
    if config.duplicate and yaSearch is None:
        printDetails()
        gui.doubleClick(waitToClick('images/shippingDup.png', 0, -4, 0.93, False))
        
    else:
        # return to the search screen
        if yaSearch is None:
            returnToSearch()
            
        # update all the click locations
        printDetails()
        clearButton = waitToClick('images/clearButton.png')
        searchQuery = lookFor('images/searchBar.png')
        searchQuery = (searchQuery[0] + 50, searchQuery[1])
        firstNameBar = (searchQuery[0], searchQuery[1] + 25)
        lastNameBar = (searchQuery[0], searchQuery[1] + 50)
        propertyNameBar = (searchQuery[0], searchQuery[1] + 75)
        
        # get the search result
        resultRegion, rEdges = getEdges()
        searchResult, searchDone, im = getSearchResult(resultRegion, rEdges)
        
        # modify the documentID to be searchable
        if config.documentID == '':
            config.documentID = addChar(getLoanNumber(), '*')

        # clear the last search and input the new search information
        clear(clearButton)
        
        # input the search query
        if config.documentID == '4':
            inputQuery(firstNameBar, lastNameBar, propertyNameBar)
        else:
            gui.doubleClick(searchQuery)
            gui.write(config.documentID)
            
        # press enter to search
        gui.press('enter')
        time.sleep(2)
        
        # get the search result
        clickResult(im, searchResult, searchDone)
            
    # save the progress
    saveProgress(2)



    
# helper functions-----------------------------------------------------------------------------------------------
    
def returnToSearch():
    """
    Return to the search screen
    :return: 
    """
    removeButton = waitToClick('images/returnToSearch.png')
    gui.PAUSE = config.MEDIUM
    gui.moveTo(removeButton)
    removeButton = waitToClick('images/returnToSearch.png')
    gui.PAUSE = config.FAST
    gui.doubleClick(removeButton)
    
    
def getSearchResult(resultRegion, rEgdes):
    """
    Get the result of the search
    :param resultRegion: (tuple) the region to search for the result
    :param rEgdes: (tuple) the edges of the result region
    :return: searchDone: (boolean) whether or not the search is done
    :return: searchResult: (tuple) the center of the searchResult image
    """
    im = gui.screenshot(region=resultRegion)
    im.save(r'C:\Users\scannerpc\PycharmProjects\ScannerAutomation230\resultRegion.png')
    
    searchDone = gui.locateOnScreen(im, grayscale=True, confidence=0.98)
    
    searchResult = gui.center(rEgdes)
    searchResult = (searchResult[0], searchResult[1] + 18)
    
    return searchDone, searchResult, im


def inputQuery(firstNameBar, lastNameBar, propertyNameBar):
    """
    Input the search query
    :param firstNameBar: (tuple) the center of the firstNameBar
    :param lastNameBar: (tuple) the center of the lastNameBar
    :param propertyNameBar: (tuple) the center of the propertyNameBar
    :return: None
    """
    # input first name
    gui.doubleClick(firstNameBar)
    gui.write(config.buyerFirst)

    # input last name
    gui.doubleClick(lastNameBar)
    gui.write(config.buyerLast)

    # input property
    gui.doubleClick(propertyNameBar)
    gui.write(config.propertyName)
    
    
def getEdges():
    """
    Get the edges of the search result
    :return: (tuple) the edges of the search result
    :return: (tuple) the region to search for the result
    """
    # look for file name on the screen
    rEgdes = gui.locateOnScreen('images/fileName.png', grayscale=True, confidence=0.93)

    # if the file name is not visible, ask the user to make it visible
    if rEgdes is None:
        gui.alert('Huh. I couldn\'t find the fileName.png. Please make sure it is visible, then click \'Ready\'',
                  'Winston', 'Ready')
        rEgdes = gui.locateOnScreen('images/fileName.png', grayscale=True, confidence=0.93)
    resultRegion = (rEgdes[0], rEgdes[1] + rEgdes[3], rEgdes[2] * 8, rEgdes[3] * 2)

    # return the region and the edges
    return resultRegion, rEgdes


def clear(clearButton):
    """
    Clears the search bar
    :param clearButton: 
    :return: 
    """
    # press the clear button
    gui.PAUSE = config.MEDIUM
    gui.click(clearButton)
    gui.PAUSE = config.FAST
    
    
def clickResult(im, searchResult, searchDone):
    """
    Clicks on the search result
    :param im: (image) the image of the search result
    :param searchResult: (tuple) the center of the searchResult image
    :param searchDone: (boolean) whether the search is done
    :return: None
    """
    # wait until the search result section refreshes, then click on the first result
    while searchDone is not None:
        searchDone = gui.locateOnScreen(im, grayscale=True, confidence=0.93)

    # if there are no results or too many results, alert the user
    noResults = gui.locateOnScreen('images/noLoanFiles.png', grayscale=True, confidence=0.93)
    multipleResults = gui.locateOnScreen('images/multipleResults.png', grayscale=True, confidence=0.95)

    # if no results appeared after the search, inform the user
    if noResults is not None:
        gui.alert('Uh oh. I don\'t see any loan files in the search results. Would you mind double checking the'
                  ' search query? Once your ready, click \'Ready\' after the search returns correctly', 'Winston',
                  'Ready')

    # if multiple results appeared after the search, inform the user
    elif multipleResults is not None:
        gui.alert('Ah! There are too many search results! This is above my pay grade. '
                  'Please select the correct loan for me.', 'Winston', 'Ready')

    # click on the result
    else:
        gui.doubleClick(searchResult)