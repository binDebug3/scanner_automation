from utils.analytics import *
from utils.opener import *
from utils.output import *
from steps import search, inputDetails, start, mergePDF, scan, replaceFile, store


def run():
    """
    This is the main function that runs the program. It will run through the steps of the program and then exit.
    :return: None
    """
    # start of day and start of scanning process
    initialize()

    # scan documents
    keepScanning = True
    while keepScanning:
        # initialize variables and close pycharm window
        minimize()

        # replace the file and start a new scanning process
        if 1 not in config.progress:
            replaceFile.replaceFile()

            start.start()

        # search for document in the system
        if config.subType != 'Quit':
            if 2 not in config.progress:
                search.search()

            # scan a new paper document
            scan.scan()

            # input document details
            if 5 not in config.progress:
                inputDetails.inputDetails()

            # merge PDFs
            if 6 not in config.progress:
                mergePDF.mergePDF()

            # save and store the document
            if 7 not in config.progress:
                store.storeDocuments()

        else:
            keepScanning = False

        viewCount()




try:
    run()
finally:
    gui.alert('Ah! Something in me broke!', 'Winston', 'RIP')
