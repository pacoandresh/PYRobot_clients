

from PYRobot_cli.client import Client
from PYRobot_cli.client_camera import ClientCamera
import time

robot=Client()

robot.Available_Robots()
robot.Connect_Robot("pcubuntu")
robot.show_info()

robot.TOPICS_list("MYgps/X","MYgps/Y","BaseM/mi","BaseM/md","temperatura1/temp")
robot.SERVICES(cam="camara_frontal/camera")
robot.TOPICS(X="MYgps/X",Y="MYgps/Y")
robot.TOPICS(mi="BaseM/mi",md="BaseM/md")
robot.TOPICS(temp="temperatura1/temp")
robot.EVENTS(BM="BaseM/basemotion")
robot.EVENTS(GPS="MYgps/gps")
robot.SERVICES(base="BaseM/basemotion")

cam=ClientCamera(robot.cam)

#Do Here your code for this robot


robot.base.set(100,100)
for x in range(2000):
    time.sleep(0.1)
    print(robot.mi,robot.md,robot.X,robot.Y)
    print(robot.BM)
    if "Max" in robot.BM:
        robot.base.set(robot.mi-20,robot.md-20)
    if "Right" in robot.BM:
        robot.base.set(robot.mi,robot.md+10)
    if "Left" in robot.BM:
        robot.base.set(robot.mi+10,robot.md)
    if "Forward" in robot.BM:
        robot.base.set(robot.mi+10,robot.md+11)
