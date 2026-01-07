# 🤖 Q-Bot Mini Workspace

ROS 2 development environment for the **Q-Bot Mini Quadruped Robot**.

## Prerequisites

* [VS Code](https://code.visualstudio.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

## Initial Setup (Run Once)

### Docker Permissions
Required to run containers without `sudo`.
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### GPU Acceleration (Optional / x86 Only)
<details>
<summary> Click to expand NVIDIA setup instructions (install NVIDIA Container Toolkit)</summary>

```bash
# Add package repositories
curl -fsSL [https://nvidia.github.io/libnvidia-container/gpgkey](https://nvidia.github.io/libnvidia-container/gpgkey) | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && \
curl -s -L [https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list](https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list) | \
sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# Install and configure
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```
</details>

---

## Getting Started

1\. Open this folder in VS Code.

2\. Press `F1` and select: **Dev Containers: Reopen in Container**.

3\. Once inside the terminal, build the workspace:

```bash
colcon build --symlink-install
source install/setup.bash
```

4\. Run the nodes you need:

```bash
# ros2 run [your_package] [your_node]
ros2 run test_cpp talker
ros2 run test_py listener

# ros2 run [your_package] [your_launch_file]
ros2 launch test_cpp test.launch.py
ros2 launch test_py test.launch.py
```

## Additional Useful Commands
```
docker system prune -a

xacro src/robot_description/urdf/robot.xacro > src/robot_description/urdf/robot.urdf

xhost +local:root
```