# For development in Laptop with amd64 architecture
ARG BASE_IMAGE=osrf/ros
ARG ROS_DISTRO=humble
FROM ${BASE_IMAGE}:${ROS_DISTRO}-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ARG USER_NAME=tom
ARG UID=1000
ARG GID=1000
ARG DOCKER_GID=999  # Replace with the actual Docker GID from your host if necessary
ENV HOME=/home/${USER_NAME}

# Install necessary packages
RUN apt-get update && apt-get install -y \
    at-spi2-core \
    bash-completion \
    build-essential \
    dbus-x11 \
    docker.io \
    git \
    gnome-terminal \
    jstest-gtk \
    ros-${ROS_DISTRO}-nav2-bringup \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-robot-localization \
    sudo \
    wget \
    xterm \
    && rm -rf /var/lib/apt/lists/*


# Create the Docker group and add the user to it
RUN groupadd -g ${DOCKER_GID} docker || true && \
    addgroup --gid ${GID} ${USER_NAME} && \
    adduser --gecos "ROS User" --disabled-password --uid ${UID} --gid ${GID} ${USER_NAME} && \
    usermod -aG dialout,docker ${USER_NAME}  # Add user to both dialout and docker groups

# Add sudo permissions for the user
ADD config/99_aptget /etc/sudoers.d/99_aptget
RUN chmod 0440 /etc/sudoers.d/99_aptget && chown root:root /etc/sudoers.d/99_aptget

# Create the workspace
RUN mkdir -p ${HOME}/humble_ws/
WORKDIR ${HOME}/humble_ws

# Set up environment
COPY config/update_bashrc /sbin/update_bashrc
RUN chmod +x /sbin/update_bashrc && chown ${USER_NAME} /sbin/update_bashrc && sync && /bin/bash -c /sbin/update_bashrc && rm /sbin/update_bashrc

# Change entrypoint to source ~/.bashrc and start in ~
COPY config/entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh && chown ${USER_NAME} /ros_entrypoint.sh

# Clean image
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
