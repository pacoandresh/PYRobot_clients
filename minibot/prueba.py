

from PYRobot.libs.client import Client
from PYRobot.libs.client_camera import ClientCamera
import time

robot=Client("mybot")
robot.show_info()

#robot.TOPICS_list("MYgps/X","MYgps/Y","BaseM/mi","BaseM/md","temperatura1/temp")
robot.TOPICS(X="MYgps/X",Y="MYgps/Y")
robot.TOPICS(mi="BaseM/mi",md="BaseM/md")
robot.TOPICS(temp="temperatura1/temp")
robot.EVENTS(BM="BaseM/basemotion")
robot.EVENTS(GPS="MYgps/gps")
robot.SERVICES(base="BaseM/basemotion_interface")
robot.SERVICES(cam="camara_frontal/camera")
cam=ClientCamera(robot.cam)


#Do Here your code for this robot


robot.base.set_base(100,100)
for x in range(2000):
    time.sleep(0.1)
    print(robot.mi,robot.md)
    print(robot.BM)
    if "Max" in robot.BM:
        robot.base.set_base(robot.mi-20,robot.md-20)
    if "Right" in robot.BM:
        robot.base.set_base(robot.mi,robot.md+10)
    if "Left" in robot.BM:
        robot.base.set_base(robot.mi+10,robot.md)
    if "Forward" in robot.BM:
        robot.base.set_base(robot.mi+10,robot.md+11)
