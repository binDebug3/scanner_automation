import pickle

import config


def incDocCount():
    """
    Increment the document count for the current document type
    :return: None
    """
    # Load the scan record
    with open('../pickles/scanRecord.pk', 'rb') as fi:
        scanRecord = pickle.load(fi)
        
    # Increment the document count
    if config.todaysDate in scanRecord.keys():
        if config.documentType in scanRecord[config.todaysDate].keys():
            scanRecord[config.todaysDate][config.documentType] += 1
        else:
            scanRecord[config.todaysDate][config.documentType] = 1
    
    # If the date is not in the scan record, add it   
    else:
        scanRecord[config.todaysDate] = {'SLP': 0, 'FNMA': 0, 'GNMA': 0, 'settlement': 0, 'Note': 0}
        scanRecord[config.todaysDate][config.documentType] = 1
        
    # Save the scan record
    with open('../pickles/scanRecord.pk', 'wb') as fi:
        pickle.dump(scanRecord, fi)


def viewCount():
    """
    View the document count for the current day
    :return: None
    """    
    # Load the scan record
    with open('../pickles/scanRecord.pk', 'rb') as fi:
        scanRecord = pickle.load(fi)
        
    # Print the document count
    statsToday = scanRecord[config.todaysDate]
    print('You have scanned:')
    
    if statsToday['SLP'] != 0:
        print('\tSLP:\t' + str(statsToday['SLP']) + ' documents')
    if statsToday['FNMA'] != 0:
        print('\tFNMA:\t' + str(statsToday['FNMA']) + ' documents')
    if statsToday['GNMA'] != 0:
        print('\tGNMA:\t' + str(statsToday['GNMA']) + ' documents')
    if statsToday['settlement'] != 0:
        print('\tFinal Settlement: ' + str(statsToday['settlement']) + ' documents')
    if statsToday['Note'] != 0:
        print('\tNote:\t' + str(statsToday['Note']) + ' documents')


def modStats(delay):
    """
    Modify the average scan time for the current document type
    :param delay: 
    :return: 
    """
    # Load the scan time
    if config.documentType == 'SLP' and delay > 600:
        return None
    
    if delay > 300:
        return None
    
    # Save the scan time
    with open('../pickles/scanLastSpeed.pk', 'wb') as fi:
        pickle.dump(delay, fi)
    with open('../pickles/scanTime.pk', 'rb') as fi:
        scanTime = pickle.load(fi)
    with open('../pickles/scanRecord.pk', 'rb') as fi:
        scanRecord = pickle.load(fi)
        
    # Modify the scan time
    if config.todaysDate in scanTime.keys():
        count = scanRecord[config.todaysDate][config.documentType]
        scanTime[config.todaysDate][config.documentType] = \
            (scanTime[config.todaysDate][config.documentType] * count + delay) / (count + 1)
        
    # If the date is not in the scan time, add it
    else:
        scanTime[config.todaysDate] = {'SLP': 0, 'FNMA': 0, 'GNMA': 0, 'settlement': 0, 'Note': 0}
        scanTime[config.todaysDate][config.documentType] = delay
        
    # Save the scan time
    with open('../pickles/scanTime.pk', 'wb') as fi:
        pickle.dump(scanTime, fi)


def viewSpeed():
    """
    View the average scan time for the current document type
    :return: None
    """
    # Load the scan time
    with open('../pickles/scanTime.pk', 'rb') as fi:
        scanTime = pickle.load(fi)
        
    # Print the scan time
    print('Average scan times for', config.todaysDate + ':')
    if scanTime[config.todaysDate]['SLP'] != 0:
        print('\tSLP:\t' + str(round(scanTime[config.todaysDate]['SLP'], 2)) + ' seconds')
    if scanTime[config.todaysDate]['FNMA'] != 0:
        print('\tFNMA:\t' + str(round(scanTime[config.todaysDate]['FNMA'], 2)) + ' seconds')
    if scanTime[config.todaysDate]['GNMA'] != 0:
        print('\tGNMA:\t' + str(round(scanTime[config.todaysDate]['GNMA'], 2)) + ' seconds')
    if scanTime[config.todaysDate]['settlement'] != 0:
        print('\tFinal Settlement: ' + str(round(scanTime[config.todaysDate]['settlement'], 2)) + ' seconds')
    if scanTime[config.todaysDate]['Note'] != 0:
        print('\tNote:\t' + str(round(scanTime[config.todaysDate]['Note'], 2)) + ' seconds')
