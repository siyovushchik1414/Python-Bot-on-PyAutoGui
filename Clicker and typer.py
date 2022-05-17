import pyautogui
import time

pyautogui.moveTo(170,767,duration=1)
pyautogui.moveTo(170,750,duration=0.4)
pyautogui.leftClick(duration = 0.8)
pyautogui.leftClick(265,150,duration = 0.8)
pyautogui.leftClick(530,645,duration = 0.8)
# pyautogui.hotkey("alt", "shift")
pyautogui.write('Hello there? my name is John, adn im trying to act naturally', interval=0.1)
pyautogui.press('enter') 

