<a name="readme-top"></a>

<div align="center">
    <h1 align="center">Winston</h1>
    <p align="center">
        A custom process automation software for scanning documents and data entry
    </p>
</div>

<hr>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#instructions">Instructions</a></li>
    <li><a href="#checkpoints">Checkpoints</a></li>
    <li><a href="#arrangements">Arranging Your Windows</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
    <li><a href="#code overview">Code Overview</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#notes">Notes and Commentary</a></li>
  </ol>
</details>


## Introduction

Hello! This is Winston, a simple function-based program to automate most of the scanning process at CMG Financial.
He uses a module called pyautogui (Python Automated Graphical User Interface) to control the
mouse and keyboard automatically. Any changes to Byte, the Scanner, or the scanning process
will need to be updated in the code and the images if made after the code was last updated on May 17, 2022.


<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>


## Installation
Despite the simple nature of Winston, he requires a bit of work to get him set up properly

1) Download Python
        You need admin authentication, so contact your Senior IT Specialist for help and permission.
        Python is a coding language, and this software enables the code to run

2) Download PyCharm
        You need admin authentication, so contact your Senior IT Specialist for help and permission.
        PyCharm is an Integrated Development Environment (IDE). Really any IDE that can run Python will work,
        but I am most familiar with PyCharm.

3) Install Pyautogui
        Open the Windows Command prompts and type in: 'pip install pyautogui'

4) Install Sub-Modules
        PyCharm will give you errors, telling you that you are missing certain modules. Click on
        'Python Packages' near the bottom-left, type in the module that you are looking for, and install the first
        result that resembles the error you received.

5) Load this File
        Make a copy of the ScannerAutomation230 folder and upload it to the folder called PyCharmProjects on
        your own computer

6) Create New Images
        I'll explain more about these later, but just know that before this program will work on a different
        computer, you'll need to update the images that the folder comes with


<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>


## Instructions
To scan a document, you will:

1) <strong>Open up Byte and the Scanner App</strong></br>
        Make sure the Scan button is visible even when Byte is open, and that the
        Scan, Save, and Clear buttons are all visible when the Scanner app is open. Make sure Byte is big enough
        so that you can see any relevant information at one time, but not full screen. Use the gray field, and
        make the yellow field as small as possible, as Winston will not use that section of Byte.</br></br>

2) <strong>Arrange your Files</strong></br>
        Make sure that each folder is visible on your desktop, including the one where you would
        like to save the PDFs you are currently scanning. Make sure there is a space visible at all times where
        the PDF can appear on the Desktop when saved. Please open arrangementScreenshot.png for an example. I
        haven't tested this but I think if you move the folders, it will mess Winston up and he won't be able
        to find them.</br></br>

3) <strong>Open the PyCharm App</strong></br>
        Once open, click File --> Open... --> Users --> <YOUR_NAME> --> PyCharmProjects --> ScannerAutomation230
        then click the OK button. If you are working on the original computer, simply double click the
        PyCharm shortcut on the Desktop, and it should open to this program. The the file load for a minute or two, 
        then you will see an area at the top that says something like, 'You can change these variables'. Below
        are the default settings and what each variable does. Any time you want to change these variables, you must
        stop and rerun Winston in order to apply them.</br></br>

    a) <strong>goFast</strong> = True. This variable will determine how fast Winston runs. It should only be set to false for
        training or demonstration purposes.</br>

    b) <strong>complimentOn</strong> = True. This variable determines if you will get compliments and fun facts each time you scan.
        It defaults to True because it's cool and fun, but Winston is a polite guy so you can ask him to stop and
        he won't complain.</br>

    c) <strong>permissionRequired</strong> = False. While this variable is true, Winston will pause and ask for permission before
        it clicks the 'Store Documents' button. It defaults to False because Winston runs faster and easier this
        way, and you should only set it to True if you are not sure Winston will consistently function 
        correctly.</br>

    d) <strong>resumePosition</strong> = 9. This variable tells Winston where to start when you rerun his program. If it is less than
        zero or greater than seven, then Winston will assume you want to restart where you left off. If that is not
        the case, simply set this variable to the last step Winston should have completed already. You can find more
        information about what this means in the Checkpoints sections below. Just don't forget to reset it so that
        Winston knows where to resume automatically!</br>

    e) <strong>documentType</strong>. This tells Winston what kind of document you are scanning. These strings must match the
        following options exactly:

        i.  Pre Funding Package
        ii. FNMA
        iii.GNMA
        iv. Note
        v.  Final Settlement

    f) <strong>enterDate</strong> = '100721'. This variable tells Winston what to input for the dates of FNMA and GNMA documents.
        If you are not scanning one of these documents, this value does not matter. As a reminder, you must restart
        Winston each time you change this value. It must be in the form: 'MMDDYY'</br>

    g) <strong>userInitials</strong> = 'DS'. This variables tells Winston your initials. For example, if Dallin Stewart is
        scanning, the initials should be DS. Winston only uses this variable if you are scanning a Note or a
        Pre Funding Package. As a reminder, you must restart Winston each time you change this value.</br></br>

4) <strong>Enter the Loan Number</strong></br>
    a) Click the green triangle near the top right to run Winston.</br>
    b) PyCharm will close and a window will pop up.</br>
    c) If he asks for the type of document, use the mouse or the arrow keys to select the appropriate type.</br>
    d) If a window pops up asking for the loan number, enter the loan number. Please ensure that it is correct.</br>
        Do not include an asterisk. Capitalization does not matter. Do not include any spaces.</br>
    e) If a window pops up asking for the type of deed, use the mouse or the arrow keys to select the appropriate
        deed type.</br>
    f) If you do not enter a loan number, Winston will ask you for for the first name, last name, and
        property name corresponding to the loan. Enter this information as precisely and fully as possible.</br></br>

5) <strong>Let Winston Run</strong></br>
   There is a slight flaw in Winston's design that I never bothered to fix. The first thing Winston actually does
   is close out of the previous loan file because that was the most efficient design. However, this means that if
   you are scanning something for the first time that day, you won't have any previous loans pulled up, but Winston
   doesn't necessarily know that. The simplest fix is to open a random loan and let Winston close it. It makes him
   happy.</br></br>

   As he is running, please be sure to:</br>
    a) Double check that the loan he finds and selects is correct. If it is not, stop Winston and finish the
        scanning process manually. Most of the time, Winston will detect and error and ask if you would like 
        to redo the scan. Winston is not infallible, however.</br>
    b) Double check that the document was scanned correctly. If it was not, stop Winston and finish the
        scanning process manually. Most of the time, Winston will detect and error, move the mouse to the 
        location where he detected the error, and ask if you would like to redo the scan. Winston is not
        infallible, however.</br>
    c) Double check that he entered the shipping information correctly. If he did not, stop Winston and finish
        the scanning process manually.</br>
    d) Before finishing, Winston may ask for permission to store the document. If he loaded the loan
        correctly, hit 'Enter' to let Winston continue


<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>

## Checkpoints
One of Winston's latest features is his new and improved memory. Winston can
remember three things: the last loan number you entered, where you left off last time you stopped the program, and
how many of each type of document you scan each day.

### Scan Progress:
Winston divides the scanning process into seven distinct steps:

        1. Input loan information
        2. Search for the loan in Byte
        3. Scan the file
        4. Save the PDF
        5. Input shipping details in Byte
        6. Upload the PDF to Byte
        7. Store the document

At the end of each step and right before moving on to the next step, Winston records that you completed that step.
This way, even if you catch a problem and want to stop Winston so that you can fix it, you can start right where
you left off without having to restart the scanning process or finishing the document manually. 

If you use this
feature, please ensure that you know exactly where in the scanning process you are. If you are not sure, you can
open the PyCharms application where Winston prints your progress at each step. If you would like to reset your
progress, simply set the 'resumePosition' variable to zero. Just be sure change it back to 9 the next time you run,
or Winston will reset your progress every time you rerun him, disabling the ability to resume instead of restart.


### Loan Number:
Winston remembers the last loan number so that you don't have to retype it every time you resume. For some reason,
this doesn't always work while naming the PDF, but you can fix that while the program pauses without too much of
an issue.


### Scanning Analytics
This feature is a little more fun and a little less practical. While the scanning machine tracks the number of
pages you scan in a day, Winston records the number of documents you scan each day, which I thought was kind of
interesting. If you would like to remove this feature, insert a '#' in front of 'incDocCount()' 'storeDocuments'
function of the 'store' file in the 'steps' directory. It should be on line 15.


<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>


## Arrangements
Before you begin scanning please make sure that the following conditions are met:</br>

1. All four folders are visible are the left-hand side of the screen and the icons look like folders with PDFs in 
   them. Make sure they are labeled 'SLP', 'Notes', 'settlement', and 'FNMA' respectively
2. The Scan button on the Fujistu scanner app is visible at all times, even when Byte overlaps part of the scanner
   app
3. The note labeled 'Winston' is open on the right side of the screen so that it never overlaps with Byte</br>
4. When a loan is open in Byte, the gray sections predominates the window. In addition, the 'Shipping' shortcut
   should be right above the 'Scanned Documents' shortcut, and visible even when the scanner app is open</br>
5. Don't change the size or resolution of the PC or any of the applications unless absolutely necessary. Most
   changes will not affect Winston, but some will so it's better to just avoid that problem entirely</br>

<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>


## Troubleshooting
The first thing you need to know is that if you want Winston to stop, he has a failsafe. If you move the mouse
to the upper-leftmost corner of the screen and hold it there for a few seconds, Winston will stop. If that does
not work, you can open PyCharm and double-click the red box near the upper-right hand corner. In addition, if there
is a pop-up from Winston open, Winston has paused and is already waiting for you, so you can safely stop the
program by double-clicking on the red box without worrying about Winston trying to move the mouse and type. You
are in control.

If you don't know the first thing about coding, all I can tell you is to restart Winston each time he messes up,
finish scanning the current document manually, and restart Winston for the next document. In order to start the
program anywhere except from the beginning, you need to know a little about coding. If you do, I'll explain more
about how Winston works in a later section so you know what to comment out if you need.
    All the functions for pyautgui are available here:
    <a href="https://pyautogui.readthedocs.io/en/latest/quickstart.html">
    https://pyautogui.readthedocs.io/en/latest/quickstart.html.

If you don't know what one does or why it is doing what it is doing, check there first. If you do make changes,
the mouseInfo() method is very useful. If there are minor problems or updates and you don't know how to fix them,
I'm happy to help walk you through how to fix it. Just shoot me an email.

The most common error is that Winston will try to save a PDF that has not finished scanning. Fortunately, this
does not cause any problems. You can simply click the Save PDF button once you see that the document is done scanning
and Winston will take things from there.

<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>


## Code Overview
Everything in this section is still true, but since I refactored the code in 2023 with more of an emphasis on the single 
responsibility principle, there are a lot more methods and moving parts than described here.

I've divided the scanning process into six major steps, reflected by six of the files in the steps folder: start, search, scan,
inputDetails, mergePDF, and store. The 'run' function in main calls everything else in the correct order.
The rest of the functions are simply shorter helper functions for the six steps. You can read through the comments in
each of the six steps along with the code itself to understand what is going on. If you are having a problem where
Winston seems to stop for no reason, or does the wrong thing, that is the best place to look.

    - Run
            Calls each of the steps in the correct order with a little bit of logic to handle specific restarts
            and cancellations

    - OpenApps
            A function that is only useful once at the beginning of the day, or if your computer crashes I guess.
            It just opens the Scanner app and Byte so that you don't have to

    - ConvertDoc
            Converts the type of document as seen in the GUI to the simpler keywords that I used when I first wrote
            Winston

    - AddChar
            This method formats the loan number. This method adds the character sent as a parameter in the method call,
            hence the name. I use it to add an asterisk to the search query, and capitalize the pdf name. Two things to
            note here. It will actually make them lowercase if CapsLock is turned on. It also will not capitalize
            letters at the end of the string.

    - EnterByName
            This method could be part of the start step, but I made it separate because if performs a more niche role
            of getting all the personal information from the loan, and it looks better to just call it.

    - WaitToClick
            This is probably the most useful method in the whole program. At the time of writing this file for the first
            time, Winston calls it about fourteen different times. It is a short function that keeps looking for
            the image file sent as a parameter until it finds it. This method allows Winston to handle variable
            wait times quite well.


### Image Files
You might have noticed that this program comes with a lot of image files. These are the images that Winston
looks for to know where to click. From what I can tell, even though they look nearly identical between different
computers with different sizes, they look very different to the computer. For example, my computer can find the
clear button in Byte very well, but as soon as I change the display size from 100% to 125%, Winston can't find the
button to save his life. That is why if you install this program on any new computer, you will have to save a
similar version from your new computer screen for each of the image files. It should not take longer
than a half hour.



<!-- CONTACT -->
## Contact

Dallin Stewart - dallinpstewart@gmail.com

[![LinkedIn][linkedin-icon]][linkedin-url]
[![GitHub][github-icon]][github-url]
[![Email][email-icon]][email-url]

<p align="right">(<a href="#readme-top">top</a>)</p>

<hr>


## Acknowledgements
I worked on a lot of this project while clocked in at CMG Financial. This program is custom-made for their exact process 
and preferences, and hence relies on the Byte software they use for storing loan information. While I did not sign an 
NDA, this GitHub repository does not contain any sensitive or proprietary information.

Thanks to Katie Stewart for her role as a beta tester.

## Notes
Please feel free to include other notes and comments, including helpful hints, oversights in the code, and common
mistakes for your own benefit and the benefit of other future users below.

<p align="right">(<a href="#readme-top">top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES for CONTACT -->

[linkedIn-icon]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedIn-url]: https://www.linkedin.com/in/dallinstewart/

[github-icon]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/binDebug3

[Email-icon]: https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white
[Email-url]: mailto:dallinpstewart@gmail.com