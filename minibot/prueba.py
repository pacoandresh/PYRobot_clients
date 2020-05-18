
from PYRobot_cli.botlogging.coloramadefs import C_Err,P_Log
from PYRobot_cli.client import Client
from PYRobot_cli.client_camera import ClientCamera
import time
import inspect 



robot=Client(delay=0.5)
robot.Available_Robots()
robot.Connect_Robot("prueba")
robot.show_info()

#robot.TOPICS(X="joystick/ABS_X",Y="joystick/ABS_Y",Z="joystick/ABS_Z",BUTT="joystick/BUTTONS")
robot.TOPICS_list("explorerhat/mi","explorerhat/md","explorerhat/analog","explorerhat/analog_raw")
#robot.INTERFACES(cam="camara_frontal/camera",base="Base/basemotion")
#robot.EVENTS(eventjs="joystick/joystick")
#cam=ClientCamera(robot.cam)

#Do Here your code for this robot

for x in range(4000):
    time.sleep(0.01)
    #print(robot.X,robot.Y,robot.Z,robot.BUTT,robot.mi,robot.md)
    print(robot.mi,robot.md,robot.analog,robot.analog_raw)
    

 