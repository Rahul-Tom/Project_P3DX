## HOST machine Set up

Install Ubnatu 22.04 (or 24.04) && Verify the ubantu version
```sh
lsb_release -a
```

Install ROS2 Humble (or latest version) from source (https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html). 
verify ROS2 version
```sh
echo $ROS_DISTRO
```

Download the necssary packages
```sh
cd
sudo apt update
sudo apt install ros-$ROS_DISTRO-navigation2 -y
sudo apt install ros-$ROS_DISTRO-nav2-bringup -y
sudo apt install ros-$ROS_DISTRO-robot-localizatio -y
sudo apt install ros-$ROS_DISTRO-slam-toolbox -y
sudo apt install python3 python3-pip -y
sudo apt install python3-pyqt5 -y
sudo apt install pyqt5-dev-tools -y
sudo apt install ros-jazzy-twist-mux -y
```
Download Docker Engine
```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo apt  install docker-compose -y

```

Clone the repo
```sh
mkdir Project_P3dDX && cd Project_P3DX
git clone https://github.com/Rahul-Tom/Project_P3DX.git
cd ~/Project_P3DX/p3dx_ws/src/
git clone https://github.com/AlexKaravaev/csm.git
git clone https://github.com/AlexKaravaev/ros2_laser_scan_matcher.git
```

Build the workspace
```sh
cd ~/Project_P3DX/p3dx_ws
colcon build --symlink install
```
If you are getting error during colcon build try agin with last command. If the problem still persist replace #include <tf2_geometry_msgs/tf2_geometry_msgs.h> with #include <tf2_geometry_msgs/tf2_geometry_msgs.hpp> in line 47 of header file in include directory of ros2_laser_scan_matcher package.


building the docker containers
#### Before building comment or uncomment every docker files' since RPi architecture (arm64 ) is different from nomal PC/Laptop's architecutre.
#### Docker files are located with name "Dockerfile" in every folder(humble, noetic, bridge, )
If you have ROS2 installation on your system consider commenting ros2 serivce called humble from docker-compose file

```sh
cd ~Project_P3DX/p3dx_docker
docker-compose -f arm64_compose.yaml up --build
```
Note that for the first time building it will take some time. Go and get your coeffee

If you don't build the ros2 service consider adding the sourcing to the envionment variable
```sh
echo "source/opt/jazzy/setup.bash">>~/.bashrc
echo "source~/Project_P3DX/p3dx_ws/install/setup.bash">>~/.bashrc
```

### Install OpenSSH
Install OpenSSH for  remotely controlling RPi using the command in the terminal (Ctrl + Alt + T)
```sh
sudo apt update
sudo apt install openssh-server -y
sudo systemctl start ssh
hostname -I
```
Now you will see your ip address let it be $ip_address
Get inter your RPi using shh
```sh
##command
ssh -X p3dx@$ip_address
##password
p3dX
```