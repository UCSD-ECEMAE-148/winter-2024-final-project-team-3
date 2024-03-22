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
    <li><a href="#pre-final-project">Pre Final Project</a></li>
      <ul>
        <li><a href="#cad-parts">CAD Parts</a></li>
          <ul>
            <li><a href="#final-assembly">Final Assembly</a></li>
            <li><a href="#printed-parts-and-base-plate-design">Printed Parts and Base Plate Design</a></li>
            <li><a href="#open-source-parts">Open Source Parts</a></li>
          </ul>
        <li><a href="#electronic-hardware">Electronic Hardware</a></li>
        <li><a href="autonomous-laps">Autonomous Laps</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- TEAM MEMBERS -->
## Team Members
<div align="center">
    <<img src="images\IMG_2315.png" width="600" height="450">
    <p align = "center">Daniel Baca (Left), Ryan Omori (Middle), Daniel Vega Zepeda (Right)</p>
</div>
<h4>Team Member Major and Class </h4>
<ul>
  <li>Daniel Baca - Mechanical Engineering Spec in Ctrls & Robotics (MC34) - Class of 2025</li>
  <li>Ryan Omori - Mechanical Engineering Spec in Ctrls & Robotics (MC34) - Class of 2025</li>
  <li>Daniel Vega Zepeda - Aerospace Engineering Spec in Flight Dynamics & Ctrls(MC35) - Class of 2024</li>
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

<!-- Pre Final Project -->
## Pre Final Project

### CAD Parts
*Filler here*

#### Final Assembly
*Images here*
[<img src="images\IMG_2310.png" width="400" height="300" />]

#### Printed Parts and Base Plate Design
| Camera Mount | Base Plate |
:-------------------------:|:-------------------------:|
[<img src="images\Camera_Mount.png" width="300" height="300" />] | [<img src="images\base_plate.png" width="300" height="300" />]

#### Open Source Parts
We utilized a wild duck model from Thingiverse found here: (https://www.thingiverse.com/thing:4797920)
We also utilized a rubber ducky model from Thingiverse found here: (https://www.thingiverse.com/thing:6429736)
And an OAK-D Lite camera mount model from Thingiverse found here: (https://www.thingiverse.com/thing:5336496)
And a Jetson Nano Case model from Thingiverse found here: (https://www.thingiverse.com/thing:3778338)
Here are our final versions of these open source parts:
| Wild Duck |  DJ Ducky | 
:-------------------------:|:-------------------------:|
[<img src="images\wild_duck.jpg" width="320" height="240" />]  |  [<img src="images\dj_ducky.png" width="300" height="300" >] |

| Oak-D Lite Mount | Jetson Nano Case |
:-------------------------:|:-------------------------:|
[<img src="images\OAKD.png" width="300" height="300" />] | [<img src="images\Jetson.png" width="300" height="300" />] |


### Electronic Hardware
Below is a circuit diagram of the electronic hardware setup for the car.

<img src="images\electronic_hardware.png">


### Autonomous Laps
Below is a youtube playlist of the car completing 3 autonomous laps using the DonkeyCar framework under different conditions. 

[<img src="images\playlist.png">](vid link)

## Acknowledgments
*Thank you to team Quack Sack, Professor Jack Silberman, and our top tier TA Arjun Naageshwaran for an amazing Winter 2024 class!*

<!-- CONTACT -->
## Contact

* Daniel Baca | dbaca@ucsd.edu
* Ryan Omori | romori@gmail.com 
* Daniel Vega Zepada | dvegazepg@ucsd.edu
