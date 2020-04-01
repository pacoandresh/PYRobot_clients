
from PYRobot_cli.client import Client
from PYRobot_cli.client_camera import ClientCamera
import time

robot=Client()
robot.Available_Robots()

robot.Connect_Robot("maxybot01")
robot.show_info()

robot.TOPICS(dist="vl6180x/distance",suelo="tracker/digital")
robot.TOPICS(md="dfrobot/md",mi="dfrobot/mi")
robot.SERVICES(base="dfrobot/basemotion")
robot.SERVICES(cam="camara_frontal/camera")

#cam=ClientCamera(robot.cam)
time.sleep(3)
print("mover")
robot.base.set(0,0)

for  x in range(1000):
    print(robot.suelo,robot.mi,robot.md,robot.dist)
    if robot.dist<100:
        print("me largo",x,robot.dist)
        mi=-100
        md=100
        robot.base.set(mi,md)
        time.sleep(0.5)
    elif robot.dist<150:
        print("cuidado obtaculo",x,robot.dist)
        mi=0
        md=0
        robot.base.set(mi,md)
    else:
        print("libre",x,robot.dist)
        mi=100
        md=100
        robot.base.set(mi,md)
    
    time.sleep(0.05)

robot.base.set(0,0)

time.sleep(1)
robot.close()