<div id="top"></div>
<h1 align="center">Quack Sack</h1>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dbaca15/ucsd-mae-148-team-3">
    <img src="images\UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>MAE148 Final Project</h3>
<p>
Team 3 Winter 2024
</p>
<img src="images\car photo here.jpg" alt="Logo" width="500" height=400">
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#team-members">Team Members</a>
    </li>
    <li><a href="#final-project">Final Project</a></li>
      <ul>
        <li><a href="#primary-goals">Primary Goals</a></li>
        <li><a href="#final-project-documentation">Final Project Documentation</a></li>
      </ul>
    <li><a href="#robot-design">Robot Design </a></li>
      <ul>
        <li><a href="#cad-parts">CAD Parts</a></li>
          <ul>
            <li><a href="#final-assembly">Final Assembly</a></li>
            <li><a href="#3d printed parts & base plate design">3d Printed Parts & Base Plate Design</a></li>
            <li><a href="#open-source-parts">Open Source Parts</a></li>
          </ul>
        <li><a href="#electronic-hardware">Electronic Hardware</a></li>
        <li><a href="#software">Software</a></li>
          <ul>
            <li><a href="#embedded-systems">Embedded Systems</a></li>
            <li><a href="#ros2">ROS2</a></li>
            <li><a href="#donkeycar-ai">DonkeyCar AI</a></li>
          </ul>
      </ul>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- TEAM MEMBERS -->
## Team Members
<div align="center">
    <img src="images\Team.jpg" alt="Logo" width="500" height=400">
    <p align = "center">person one (Left), person two (Middle), person three (Right)</p>
</div>
<h4>Team Member Major and Class </h4>
<ul>
  <li>Daniel Baca - Mechanical Engineering Spec in Ctrls & Robotics (MC34) - Class of 2025</li>
  <li>Ryan Omori - Mechanical Engineering Spec in Ctrls & Robotics (MC34) - Class of 2025</li>
  <li>Daniel Vega - Aerospace Engineering Spec in Flight Dynamics & Ctrls(MC35) - Class of 2024</li>
</ul>

<!-- Final Project -->
## Final Project

Project Quack Sack seeks to develop an object-following robot. Our car is programmed using custom ROS2 packages to follow anyone with the proper key. The key object is tracked on the OAKD-Lite using a model created on Roboflow. The idea may be simple, but having a follower can be useful for various reasons like carrying supplies. Using a custom Python script, our car can also seek out the key object when lost. 

<!-- Primary Goals -->
### Primary Goals
1. Follow the key object by keeping it in the car's POV. The car will slow to a stop whenever it reaches a certain distance from the key object. In this case, the key object is a 3d printed mama duck.
2. If the car loses sight of the key object for too long, it will go into a seeking mode. This seeking mode is a Python script built to look for the key object around the area. Once the key object is found, the duck will return to the key object and go back to following mode.

### Final Project Documentation

* [Final Project Proposal 2/8](https://docs.google.com/presentation/d/1moO-ZlQi4ESZR3XwmRlqZk-4W117Qocw2nV0kwnNdVw/edit?usp=sharing)
* [First Progress Update 2/29](https://docs.google.com/presentation/d/1NAcGFi7LNld9GlBOmhneJEPiE3GNgi9s3R5NsQQY7bQ/edit?usp=sharing)
* [Second Progress Update 3/7](https://docs.google.com/presentation/d/1FqhtvtD_XulPEkqER6wvuZKyt5m80NjzAZZ-L4SKuVQ/edit?usp=sharing)
* [Final Progress Update 3/14](https://docs.google.com/presentation/d/1lDfH2DU8BgbXBb7jGNfDQjTwF17CYSD6O3kXAU3AJYU/edit?usp=sharing)

<!-- Robot Design -->
## Robot Design

### CAD Parts

#### 3d Printed Parts & Base Plate Design
| Part | CAD Model | Credits |
| Camera Mount |  Jetson Mount | LIDAR Mount |
:-------------------------:|:-------------------------:|:-------------------------:
[<img src="images\Top_camera_mount.PNG">](https://github.com/ECE148-WI-23-Team-1/CV-Sign-and-Person-Detection/blob/main/images/Top_camera_mount.PNG)  |  [<img src="images\Bottom_camera_mount.PNG">](https://github.com/ECE148-WI-23-Team-1/CV-Sign-and-Person-Detection/blob/main/images/Bottom_camera_mount.PNG) | [<img src="images\LIDAR_Mount.PNG">](https://github.com/ECE148-WI-23-Team-1/CV-Sign-and-Person-Detection/blob/main/images/LIDAR_Mount.PNG)



#### Open Source Parts
| Part | CAD Model | Source |
|------|--------|-----------|
| Jetson Nano Case | <img src="https://github.com/kiers-neely/ucsd-mae-148-team-4/assets/161119406/6770d099-0e2e-4f8d-8072-991f1b72971f" width="400" height="300" /> | [Thingiverse](https://www.thingiverse.com/thing:3778338) |
| Oak-D Lite Case | <img src="https://github.com/kiers-neely/ucsd-mae-148-team-4/assets/161119406/bcc64c60-d67c-47af-b0cb-f46ac7b8a4c1" width="400" height="300" /> | [Thingiverse](https://www.thingiverse.com/thing:533649) |


### Electronic Hardware
Below is a circuit diagram of the electronic hardware setup for the car.

<img src="https://github.com/kiers-neely/ucsd-mae-148-team-4/assets/161119406/6f7501ee-382a-4590-9c0a-f8ce738efec3" width="800" height="400" />


### Software
#### Embedded Systems
To program the Jetson Nano, we accessed the Jetson Nano through remote SSH connection to an embedded Linux system onboard and ran a docker container with all the necessary dependencies to run our packages. This allowed us to eliminate any incompatibility issues and to maximize resource efficiency on the Jetson. We used a variation of virtualization softwares including VMWare and WSL2 to build, test and launch our programs. 

#### ROS2
The base image pulled from Docker Hub for our project development contained the UCSD Robocar module ran on a Linux OS (Ubuntu 20.04). The Robocar module, consisting of several submodules using ROS/ROS2, was originally developed by Dominic Nightingale, a UC San Diego graduate student. His framework was built for use with a wide variety of sensors and actuation methods on scale autonomous vehicles, providing the ability to easily control a car-like robot while enabling the robot to simultaneously perform autonomous tasks.

#### DonkeyCar AI
For our early quarter course deliverables we used DonkeyCar to train a car in driving autonomous laps around a track in a simulated environment. We used Deep Learning to record visual data of driving on a simulated track and trained the car with the data to then race on a remote server. This helped us to prepare for training our physical car on an outdoor track with computer vision.

<!-- Authors -->
## Authors
  - [@kiers-neely](https://github.com/kiers-neely)  

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
*Thank you to my teammates, Professor Jack Silberman, and our incredible TA Arjun Naageshwaran for an amazing Winter 2024 class!*

<!-- CONTACT -->
## Contact

* Kiersten | kneely@ucsd.edu
* Jacob | jacoberobison@gmail.com 
* Joe | hjjeong@ucsd.edu
* Damien | dcuara@ucsd.edu
