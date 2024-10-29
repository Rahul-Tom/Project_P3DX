#!/bin/bash
set -e # setup environment
source $HOME/.bashrc # start in home directory 

cd $HOME/humble_ws/ 
# git clone https://github.com/Rahul-Tom/p3dx_description_ros.git
cd $HOME/humble_ws/p3dx_ws 
## colcon build
exec bash -i -c $@
# Adding all the necessary ros sourcing

