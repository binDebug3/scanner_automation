import pickle

import config


def getLoanNumber():
    """
    Get the loan number from the pickle file
    :return: (int) loan number
    """
    # Load the loan number
    with open('../pickles/loanNumber.pk', 'rb') as fi:
        return pickle.load(fi)
    
    
def getDeed():
    """
    Get the deed from the pickle file
    :return: (int) deed
    """
    # Load the deed
    with open('../pickles/deed.pk', 'rb') as fi:
        return pickle.load(fi)
    
    
def saveProgress(step, saveRange=False):
    """
    Save the progress to the pickle file
    :param step: (int) the current step
    :param saveRange: (boolean) save the range of steps or not
    :return: None
    """
    # update step
    if 0 < step < 8:
        if saveRange:
            config.progress = []
            
            for i in range(step):
                config.progress.append(i)
            print('Step ' + str(config.progress[len(config.progress) - 1]) + ' complete')
            
        else:
            config.progress.append(step)
            print('Step ' + str(step) + ' complete')
            
    else:
        config.progress = []

    # Save the progress
    with open(config.fileName, 'wb') as fi:
        pickle.dump(config.progress, fi)
        
        
def getProgress(prent=True):
    """
    Get the config.progress from the pickle file
    :param prent: (boolean) print the current step or not
    :return: (int) the current step
    """
    # Load the progress
    with open(config.fileName, 'rb') as fi:
        config.progress = pickle.load(fi)

    # Print the current step
    if prent:
        if len(config.progress) > 0:
            print('Step ' + str(config.progress[len(config.progress)-1]) + ' complete')
        else:
            print('Initiating')

    # Return the current step
    if len(config.progress) > 0:
        return config.progress[len(config.progress)-1]
    else:
        return 0