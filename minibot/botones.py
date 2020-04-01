from PYRobot_cli.client import Client
from PYRobot_cli.client_camera import ClientCamera
import time

robot=Client()
robot.Available_Robots()

robot.Connect_Robot("minibot02")
robot.show_info()
robot.TOPICS(dist="vl6180x/distance")
robot.TOPICS(suelo="explorerhat/analog",md="explorerhat/md",mi="explorerhat/mi")
robot.SERVICES(light="explorerhat/light_interface")