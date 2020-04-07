# PyShoe

Code for "Robust Data-Driven Zero-Velocity Detection for Foot-Mounted Inertial Navigation": an open source foot-mounted, zero-velocity-aided inertial navigation system (INS) that includes implementations of four classical zero-velocity detectors, in addition to two learning-based detectors.

This is based on https://github.com/utiasSTARS/pyshoe.git 

<img src="https://github.com/utiasSTARS/pyshoe/blob/master/main_figure.png" width="400px"/>

## Dependencies:
* numpy
* scipy 
* [scikit-learn](https://scikit-learn.org/stable/) to run the adaptive zero-velocity detector
* [pytorch](https://pytorch.org/) to run the LSTM-based zero-velocity classifier

Scikit-Learn and PyTorch do not need to be installed if you do not intend to use our zero-velocity detectors.  You must remove the import of LSTM and SVM from ins_tools/EKF.py to do so.

## Added Functionality (ROS Bag reading via CSV Export)
ROS Bag files can be used to generate odometry data, using the provided script `imu_ros.py`.

Use `rostopic echo -b "${fileName}.bag" -p $topicName > "${fileName}.csv"` to generate the CSV file. Then specify the exported CSV file location in `imu_ros.py` file in lines 11 and 13. You can also specify the result directory in line 12.

The code has been tested with Python 3.5. It will save a time-stamped csv file containing odometry data, and a tragectory plot, in the specified results folder.
