 #First we need to import the pyautogui module. After that, we need to import the time module. Why do we need it? If we didn't have this module, our bot would work too fast, so we need a time delay before the programs are loaded.

        #All of our code is written with mouse coordinates, but how do we see these coordinates? We need a program called ScreenLoupe. When we turn it on, it shows the position of our mouse

        #Let's start writing our code. In order to understand the controls, let's try just to move our mouse in a given direction. To do this we use the pyautogui.moveTo() function, the name says it all. We need coordinates (we get them from ScreenLoupe). We write into this function the horizontal coordinates first. The cursor will position itself at the coordinates we have specified but it will position itself there in an instant. That is why we need to prescribe something else, namely the third coordinate duration=(the bigger it is, the slower the standard = 1) 1.
It looks like this: pyautogui.moveTo(680,0,duration=1). This is how the Mouse moves#
	
	#Now let's try rightClick & leftClick & middleClick. Pyautogui.leftClick(500,500,duration=1). When rightClick(ex,ex,duration=ex) is used, you might get a situation where the action is executed without any delay. This can be corrected by adding muwTu in addition toClick. 
	
	#The function pyautogui.PAUSE= n or time.sleep(n)
	#pyautogui.write(' ', interval=0.25) or pyautogui,typewrite("Ghbdtn vbh") is used to write something to the specified mouse point.
	#pyautogui.press('enter') the name says it all, the keys can be found in the documentation. Everything works intuitively.
	#pyautogui.hotkey("alt", "shift")
	#also function pyautogui.hold('shift'), variations are also in documentation
	
#Some words about pyautogui#
! The documentation for pyautogui is well-structured. 
#Pyautogui. Module documentation Welcome to PyAutoGUI's documentation! - PyAutoGUI documentation. 
This is a library which allows you to emulate keyboard actions (keystrokes, text input, hotkeys) as well as mouse actions (right/left button, click, drag, move). It works wherever Python works, which means that code written in one place will work in another.
