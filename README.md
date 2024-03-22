<div id="top"></div>
<h1 align="center">Quack and Track: An Autonomous Duckling Following Robot Car</h1>
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
<img src="images\IMG_2320.jpg" alt="Logo" width="500" height=400">
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- TEAM MEMBERS -->
## Team Members
<div align="center">
    <img src="images\IMG_2315.png" width="600" height="450">
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

Project Quack and Track builds an autonomous following robot car using ROS2 for efficient control. Our unique system utilizes a custom-trained Roboflow model deployed on the OAK-D Lite camera to track a designated "key" object. This follower robot can be utilized for tasks like carrying supplies by autonomously following its designated target.  Furthermore, a custom Python script equips the robot with lost-object recovery capabilities, allowing it to locate the key object even when out of sight.

<!-- Primary Goals -->
### Primary Goals

1. <b>Accurate Object Following:</b> Develop an object-following system using ROS2 for efficient control. The robot car will utilize a custom-trained Roboflow model deployed on the OAK-D Lite camera to track a designated "mama duck" object within its field of view.
2. <b>Lost Object Recovery:</b> Implement a "seeking mode" triggered by a custom Python script when the robot loses sight of the mama duck. This mode will actively search the surrounding area for the duck, enabling autonomous recovery.
3. <b>Safe and Precise Stopping:</b> Upon locating the mama duck, the robot will employ controlled braking to come to a stop at a safe and pre-defined distance, ensuring the safety of both the robot and its target.

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
<img src="images\IMG_2310.png" width="400" height="300" /> <img src="images\IMG_2320.jpg" width="400" height="300" /> <img src="images\IMG_2321.jpg" width="400" height="300" /> <img src="images\IMG_2322.jpg" width="400" height="300" /> <img src="images\IMG_2323.jpg" width="400" height="300" /> <img src="images\IMG_2324.jpg" width="400" height="300" />

#### Printed Parts and Base Plate Design
| Camera Mount | Base Plate |
:-------------------------:|:-------------------------:|
<img src="images\Camera_Mount.png" width="300" height="300" /> | <img src="images\base_plate.png" width="300" height="300" />

#### Open Source Parts
We utilized a wild duck model from Thingiverse found here: (https://www.thingiverse.com/thing:4797920)
We also utilized a rubber ducky model from Thingiverse found here: (https://www.thingiverse.com/thing:6429736)
And an OAK-D Lite camera mount model from Thingiverse found here: (https://www.thingiverse.com/thing:5336496)
And a Jetson Nano Case model from Thingiverse found here: (https://www.thingiverse.com/thing:3778338)
Here are our final versions of these open source parts:
| Wild Duck |  DJ Ducky | 
:-------------------------:|:-------------------------:|
<img src="images\wild_duck.jpg" width="320" height="240" />  |  <img src="images\dj_ducky.png" width="300" height="300" > |

| Oak-D Lite Mount | Jetson Nano Case |
:-------------------------:|:-------------------------:|
<img src="images\OAKD.png" width="300" height="300" /> | <img src="images\Jetson.png" width="300" height="300" /> |


### Electronic Hardware
Below is a circuit diagram of the electronic hardware setup for the car.

<img src="images\electronic_hardware.png">

## Acknowledgments
*Thank you to team Quack Sack, Professor Jack Silberman, and our top tier TA Arjun Naageshwaran for an amazing Winter 2024 class!*

<!-- CONTACT -->
## Contact

* Daniel Baca | dbaca@ucsd.edu
* Ryan Omori | romori@gmail.com 
* Daniel Vega Zepada | dvegazepg@ucsd.edu
