
from PYRobot_cli.client import Client
from PYRobot_cli.client_camera import ClientCamera
import time

robot=Client()
robot.Available_Robots()

robot.Connect_Robot("minibot04")
robot.show_info()
robot.TOPICS(dist="vl6180x/distance")
robot.TOPICS(suelo="explorerhat/analog",md="explorerhat/md",mi="explorerhat/mi")
robot.SERVICES(light="explorerhat/light_interface")
robot.SERVICES(base="explorerhat/basemotion")
robot.SERVICES(cam="camara_frontal/camera")
#cam=ClientCamera(robot.cam)

robot.light.set_light("red",True)
robot.light.set_light("yellow",True)
robot.light.set_light("blue",True)
robot.light.set_light("green",True)
cam=ClientCamera(robot.cam)
time.sleep(3)
print("mover")
robot.base.set(0,0)
#robot.base.set_base(0,0)
for  x in range(10):
    print(robot.suelo,robot.mi,robot.md,robot.dist)
    if robot.dist<50:
        print("atras",x,robot.dist)
        mi=-10
        md=-10
    elif robot.dist<120:
        print("cuidado obtaculo",x,robot.dist)
        mi=0
        md=0
    else:
        print("libre",x,robot.dist)
        mi=10
        md=10
    robot.base.set(mi,md)
    time.sleep(0.05)
for x in range(3):
    robot.base.set(100,90)
    time.sleep(3)
    robot.base.set(-100,-90)
    time.sleep(3)
    
robot.base.set(0,0)
time.sleep(1)
robot.close()