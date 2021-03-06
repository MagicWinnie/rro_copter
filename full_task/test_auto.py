import rospy
from clever import srv
from std_srvs.srv import Trigger
from mavros_msgs.srv import CommandBool
import math
import time
import Utils

points = {"takeoff":(2.3, 2, 1.3), "land": (0.27, 2.05, 1.3)}

magnit = Utils.Magnet()
magnit.off()

rospy.init_node("flight")

copter = Utils.Copter(markers_flipped=True)
copter.start_coord = points["takeoff"]
copter.zero_z = 2.5
# copter.callib_zero_z()

print("takeoff")
copter.takeoff(1.5)
print("takeoff compl")
rospy.sleep(0.5)

print("go to tk point")
copter.go_to_point(points["takeoff"])
print("hold tk point")
rospy.sleep(3)

print("go to tk land")
copter.go_to_point(points["land"])
print("hold tk land")
rospy.sleep(3)
# magnit.off()
print("land")
copter.land()
# copter.go_to_point((0, 0, 1.8))
# rospy.spin()
