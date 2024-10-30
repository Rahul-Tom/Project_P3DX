## HOST machine Set up
Highly recomended to use ubuntu machine(22.04 LTS). 

Install Ubuntu 22.04 (or 24.04) && Verify the ubuntu version
```sh
lsb_release -a
```

Note that this repo have different branches. For any branch needs docker installation. 

**1. main** -Assume you have ROS2 installed Ubuntu machine

**2. Full_Container_arm64** - Assume you have ARM64 architecutre without ROS2 installation. If you are using Rasperyy Pi (5), use this branch.

**3. Full_Container_amd64** Assume you have ubuntu machine without ROS2 installation.

Since GUI is developed for main bracnch some buttons may not work in other two branches. But it not at all effect overall operations

### Install docker engine and docker compose
Download Docker Engine
```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo apt  install docker-compose -y

```
### ROS2 Installation (only for main branch)
Install ROS2 Humble (or latest LTS version) from source (https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html).

verify ROS2 version
```sh
echo $ROS_DISTRO
```



### Download the necssary packages (only for main branch)
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
#sudo apt install ros-humble-twist-mux -y
```

### Clone the repo
If you are using different branch than main, go there and find the readme inside it for cloning restrcition. This is for main branch. 
```sh
cd ~/
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


### Building the docker containers
Note that this may vary according the branch you are using.
```sh
cd ~Project_P3DX/p3dx_docker

docker-compose up --build

```
Note that for the first time building it will take some time. Go and get your coeffee

If you don't build the ros2 service consider adding the sourcing to the envionment variable
```sh
echo "source/opt/humble/setup.bash">>~/.bashrc
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

## Some useful commands
### 1. Docker

To remove unneceaary images
```sh
docker system prune
```
To down all the containers(running or stopped)
```sh
docker-compose down
#or
docker-compose -f arm64_compose.yaml down
```
To get a terminal
```sh
docker exec -it ros2_humble_container bash
```

### 2. ROS2

Launch
```sh
ros2 launch pkg_name filename.py
```
Run
```sh
ros2 run pkg_name executable
```
To retsart ros2 daemon
```sh
ros2 dameon stop && ros2 dameon start
```

## Application on Windows 11

Eventhough it is not recommended, it is possible. But I did not tried the hardware compatability.
**1 Install Docker Desktop**

**2 Install WSL**
```sh
wsl --install -d Ubuntu-22.04
```
for bash terminal from thr command prompt execute same above command.
Follow the instructions for Full_Container_amd64/main branch including ROS2 installtion, but avoid docker installation.


