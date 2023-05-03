import pyautogui as gui

gui.alert('Ready?')
gui.PAUSE = 0.05
gui.click(336, 153)
while True:
    gui.press('\'')
    gui.press('down')
    gui.press('delete')