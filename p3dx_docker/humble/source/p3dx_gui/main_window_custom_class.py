#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main_window import Ui_MainWindow
#pyuic5 -x main_window.ui -o main_window.py

import os
import sys
import time
import threading

class ButtonDefinition(Ui_MainWindow):
    def _init_(self):
        super().__init__()
        self.exportNum=0
        self.extractNum=0


    def init(self):
        self.init__control_panel()
        self.color_control()
        self.button_hide()
        self.label_text()
        

    def init__control_panel(self):
        self.pushButton_ConnectToRobot.clicked.connect(self.pushButton_ConnectToRobot_action)
        self.pushButton_RQt.clicked.connect(self.pushButton_RQt_action)
        self.pushButton_Rviz2.clicked.connect(self.pushButton_Rviz2_action)
        self.pushButton_Record.clicked.connect(self.pushButton_Record_action)
        self.pushButton_Autonomous.clicked.connect(self.pushButton_Autonomous_action)
        self.pushButton_JoyControl.clicked.connect(self.pushButton_JoyControl_action)
        self.pushButton_NewMap.clicked.connect(self.pushButton_NewMap_action)
        self.pushButton_withMap.clicked.connect(self.pushButton_withMap_action)
        self.pushButton_StartStopRecord.clicked.connect(self.pushButton_StartStopRecord_action)
        self.pushButton_STOP_Nav.clicked.connect(self.pushButton_STOP_Nav_action)
        self.pushButton_StartStopRecord_2.clicked.connect(self.pushButton_StartStopRecord2_action)
        self.pushButton_SaveMap.clicked.connect(self.pushButton_SaveMap_action)
        self.pushButton_ManualControl.clicked.connect(self.pushButton_ManualControl_action)
        self.pushButton_KeyboardControl.clicked.connect(self.pushButton_KeyboardControl_action)
        self.pushButton_Emergency.clicked.connect(self.pushButton_Emergency_action)
        self.pushButton_Refresh.clicked.connect(self.pushButton_Refresh_action)
        
        
    
    def color_control(self):
        self.pushButton_ConnectToRobot.setStyleSheet("background-color: green; color: white; font-weight: bold;")    
        self.pushButton_STOP_Nav.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.pushButton_Emergency.setStyleSheet("background-color: red; color: white; font-weight: bold;")

    def label_text(self):
        self.label.setText('Please press "Connect to Robot" button and wait for 30 seconds..')
        self.label.setStyleSheet("color: blue;")
    

    def button_hide(self):
        # Initially hide the horizontal layout widget
        self.horizontalLayoutWidget.hide()
        self.horizontalLayoutWidget_2.hide()
        self.horizontalLayoutWidget_4.hide()
        self.lineEdit.hide()
        self.pushButton_STOP_Nav.hide()
        self.pushButton_StartStopRecord.hide()
        self.pushButton_StartStopRecord_2.hide()
        self.pushButton_SaveMap.hide()
        self.pushButton_Refresh.hide()

    ##executation method
    def execCommand(self, cmd: str):
        cmd_base_head = "gnome-terminal -- bash -c '"
        cmd_base_tail = "'&"
        cmd_full =   cmd_base_head + cmd + cmd_base_tail  

        print(f"#COMMAND: {cmd_full}")
        os.system(cmd_full)    

    ##Function to Connection to robot and lidar
    def pushButton_ConnectToRobot_action(self):
        cmd = f'cd $(find / -type d -name "p3dx_docker" 2>/dev/null | head -n 1) && docker-compose up --build'
        cmd1='ros2 lauch p3dx_navigation twist_mux_launch.py'
        self.execCommand(cmd)
        self.execCommand(cmd1)
        self.startDelayThread()
        self.pushButton_STOP_Nav.show()
        self.pushButton_Refresh.show()
    

     # Function to run the delay using threading
    def startDelayThread(self):
        thread = threading.Thread(target=self.delayAndShow)
        thread.start()
    def delayAndShow(self):
        time.sleep(2)  # 30-second delay
        self.horizontalLayoutWidget.show()
        self.label.setText(f"P3-DX is ready for the adventure")   
    
    #Function for RQt
    def pushButton_RQt_action(self):
        cmd="source /opt/ros/$ROS_DISTRO/setup.bash && ros2 run rqt_gui rqt_gui"
        self.execCommand(cmd)
        self.label.setText(f"RQt is running, introspect ROS2 node")    
     #Function for Rviz2
    def pushButton_Rviz2_action(self):
        cmd = "ros2 run rviz2 rviz2"
        self.execCommand(cmd)
        self.label.setText(f"Rviz is running:")
     #Function for bag recording..
    def pushButton_Record_action(self):
        self.lineEdit.show()
        self.pushButton_StartStopRecord.show()
        self.label.setText(f"Type the bag name here without any extension ->")
        self.label.setStyleSheet("color: green;")
        
     #Function for bag recoding start
    def pushButton_StartStopRecord_action(self):
        bag_file_name = self.lineEdit.text().strip()
        if bag_file_name:
            self.label.setText(f'Recording bag files. Press "Stop recording" to stop.')
            self.pushButton_StartStopRecord.hide()
            self.pushButton_StartStopRecord_2.show()
            cmd = f'cd $(find / -type d -name "p3dx_bag_files" 2>/dev/null | head -n 1) && ros2 bag record -o {bag_file_name} -a'
            self.execCommand(cmd)
            self.lineEdit.clear()
            self.lineEdit.hide()
        else:
            self.label.setText("Please enter a valid name for the bag file.")
            self.label.setStyleSheet("color: red;")

     #Function for bag recoring stop
    def pushButton_StartStopRecord2_action(self):
        self.lineEdit.hide()
        self.label.setText(f"Bag file saved..")
        cmd = 'pkill -f "ros2 bag record"'
        self.execCommand(cmd)
        self.pushButton_StartStopRecord_2.hide()
        self.pushButton_StartStopRecord.hide()    

     #Function for autonomous nav, launch robot description and laser scan matching.
    def pushButton_Autonomous_action(self):
        self.horizontalLayoutWidget_2.show()
        cmd0 = "ros2 launch p3dx_navigation p3dx_description_ros2.launch.py ; exec bash"
        cmd1 = "sleep 1 && ros2 launch ros2_laser_scan_matcher start.matcher.launch.py"
        self.execCommand(cmd0)
        self.execCommand(cmd1)

     #Function for manual operation
    def pushButton_ManualControl_action(self):
        self.horizontalLayoutWidget_4.show()
        self.label.setText(" Choose the teleoperation you want ")
     
    #Function for keyboard control, consider write it into launch file
    def pushButton_KeyboardControl_action(self):
       cmd = f'ros2 run turtlesim turtle_teleop_key --ros-args -r turtle1/cmd_vel:=RosAria/cmd_vel; exec bash'
       self.label.setText("Choose the Arrow buttons for driving.")
       self.execCommand(cmd) 

     #Function for Joystick control
    def pushButton_JoyControl_action(self):
        cmd = "source /opt/ros/$ROS_DISTRO/setup.bash && ros2 launch p3dx_navigation joystick_launch.py"
        self.execCommand(cmd) 
        self.label.setText(f"Press and hold L2/R2 and left control button to navigate")

     #Function for new map using SLAM, 
    def pushButton_NewMap_action(self):
        cmd0 = "source /opt/ros/$ROS_DISTRO/setup.bash && ros2 launch p3dx_navigation online_async_launch.py; exec bash" #; exec bash
        cmd1 = "source /opt/ros/$ROS_DISTRO/setup.bash && ros2 launch p3dx_navigation joystick_launch.py"
        cmd2="ros2 launch p3dx_navigation navigation_launch.py"
            
        self.lineEdit.show()
        # self.line_edit.setStyleSheet("QLineEdit { border: 2px solid red; }")
        self.label.setText(f"Mapping started. Save the map when you done with mapping. Name your map here(without any extension)")
        self.pushButton_SaveMap.show()
        self.execCommand(cmd0)
        self.execCommand(cmd1)
        self.execCommand(cmd2)
        
     #Function for saving the new map, consider make additions such that it asking for the directory where to save.
    def pushButton_SaveMap_action(self):
        map_name=self.lineEdit.text().strip()
        maps_dir = os.popen('find / -type d -name "p3dx_maps" 2>/dev/null | head -n 1').read().strip()
        if map_name:
            self.label.setText(f"Map is saved")
            self.label.setStyleSheet("color: green;")
            cmd = f"ros2 run nav2_map_server map_saver_cli -f {maps_dir}/{map_name}" #; exec bash"
            self.execCommand(cmd)
            self.pushButton_SaveMap.hide()
            self.lineEdit.clear()
            self.lineEdit.hide()
        else:
              self.label.setText(f"Name your bag file and save ..")
              self.label.setStyleSheet("color: red;")  

    # #Function for selecting the map for localization and nav
    def pushButton_withMap_action(self):
        self.label.setText(f"choose the map")
        self.openFileDialog()

    def openFileDialog(self):
        default_dir = "/home/tom/Project_P3DX/p3dx_maps"
        file_name, _ = QFileDialog.getOpenFileName(None, 'Select Map', default_dir, "Map Files (*.yaml)")
        if file_name:
            print(f"Selected map file: {file_name}")
            cmd0 =f"ros2 launch p3dx_navigation localization_launch.py map:={file_name}"
            self.label.setText(f"Selected map file: {file_name}")
            self.execCommand(cmd0)
            time.sleep(2)
            cmd1="ros2 launch p3dx_navigation navigation_launch.py"
            self.execCommand(cmd1)
            self.label.setText("Use 2d pose estimation in Rviz for initail position and set your goals")
        else:
            self.label.setText("Choose a valid map in YAML format or map your environment using 'New Map' button")

    
     #Function for stopinng nav2 and any other ros2 commands.
    def pushButton_STOP_Nav_action(self):
        cmd0="pkill -f ros2"
        
        self.execCommand(cmd0)
        self.pushButton_STOP_Nav.hide()
        
        self.label.setText("Stopping ........")
        time.sleep(5)
        self.label.setText("Stoped, start again")
        self.label.setStyleSheet("color: red;")

     #Function for Emergency, same button is for disconnecting the robot also    
     # consider to write a function to stop the rqt aslo if it is enabled
    def pushButton_Emergency_action(self):
        self.pushButton_STOP_Nav_action()
        cmd0 = f'cd $(find / -type d -name "p3dx_docker" 2>/dev/null | head -n 1) && docker-compose down'
        self.execCommand(cmd0)
        self.button_hide()
        self.label.setText("EMEGENCY enabled ........ROS2 stopeed, robot disconnected")

     #Function for restart ros2 daemon
    def pushButton_Refresh_action(self):
        cmd="ros2 daemon stop && sleep 1 && ros2 daemon start"
        self.execCommand(cmd)
        self.label.setText("ROS2 Daemon restarted ........")    
    
    
    



    

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ButtonDefinition()
    ui.setupUi(MainWindow)
    ui.init()
    MainWindow.show()
    sys.exit(app.exec_())
