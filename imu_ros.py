import numpy as np
from ins_tools.util import *
import ins_tools.visualize as visualize
from ins_tools.INS import INS
import scipy.io as sio

from utilities.csv_parser import readCSV, readROSBagCSV, writeCSV 
from utilities.data_visualizer import show3Dposition, show2Dposition
from utilities.geometry_utils import rotateOutput

data_dir = "./ros_data/"
result_dir = "./ros_data/results/"
fileName = "2020-03-23-17-15-36"

fieldNames= ["time", "field.linear_acceleration.x", "field.linear_acceleration.y", "field.linear_acceleration.z",
                 "field.angular_velocity.x", "field.angular_velocity.y", "field.angular_velocity.z"]
dataTypes = [int, float, float, float, float, float, float]

status, userData = readROSBagCSV(data_dir+fileName+'.csv', fields=fieldNames, dtype=dataTypes)
ros_data = userData.view((float, len(userData.dtype.names)))

print("ROS Bag Demo: " + fileName)

imu = ros_data[:,1:]
timeStep = 1.0/40

print ("Input shape: ", imu.shape)
ins = INS(imu, sigma_a = 0.00098, sigma_w = 8.7266463e-5, T=timeStep) 

detector = "shoe"

if (detector == "shoe"):
    # load the pre-computed optimal thresholds
    G_opt_shoe = 2.5e8
    #Estimate trajectory
    x_out = ins.baseline(W=5, G=G_opt_shoe, detector='shoe')

elif (detector == "ared"):
    # load the pre-computed optimal thresholds
    G_opt_ared = 1.5000000000000004 
    #Estimate trajectory
    x_out = ins.baseline(W=5, G=G_opt_ared, detector='ared')

elif (detector == "lstm"):
    zv_lstm = ins.Localizer.LSTM()
    x_out = ins.baseline(zv=zv_lstm)

else:
    print ("Invalid detector")
    exit

output = np.zeros((x_out.shape[0], 11))
output[:,0] = userData['time']
# Rotate and generate output
output[:,1:11] = rotateOutput(x_out, roll=math.pi, pitch=0, yaw=0)


writeCSV(output, result_dir+fileName+'.csv', fields=['time', 
                                                    'x_position', 'y_position', 'z_position', 
                                                    'roll', 'pitch', 'yaw',
                                                    'quaternion_w', 'quaternion_x', 'quaternion_y', 'quaternion_z'])
show2Dposition(output[:,1:], result_dir+fileName)



