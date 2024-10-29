import src.mouse as mouse
import src.screen as screen


mousePos = mouse.getMousePos()

screen.screenShot((mousePos[0],mousePos[1],mousePos[0]+100,mousePos[1]+100))



