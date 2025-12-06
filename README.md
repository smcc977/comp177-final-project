<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">COMP 177 Final Project</h3>

  <h4 align="center">
    Dynamic Source Routing (DSR) with Fault Recovery in a Simulated Network
  </h4>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

In this project we created a DSR Simulator to simulate what happens on a network using DSR.

We created 2 networks of differing sizes and created a sequence of actions that will test the algorithms behavior in various conditions. These actions involved finding a route from and to a given node, but also includes removing links due to the ever-changing topology within an ad hoc network.

Our program while testing these sequences will measure how long a given action takes and output the network graphs at periodic intervals. These features help in understand the algorithms behavior while also being able to analyze its performance in different conditions.

<!-- GETTING STARTED -->
## Getting Started

To get the program up and running please follow the steps below.

### Prerequisites

Here are the libraries we use and how to install them.
* NetworkX
  ```sh
  pip install networkx
  ```
* Matplotlib
  ```sh
  pip install matplotlib
  ```

### Installation

After ensuring you have all the dependencies installed:

1. Clone the repo
   ```sh
   git clone https://github.com/smcc977/comp177-final-project.git
   ```

2. Run the program
   ```sh
   python Main.py
   ```
   Note: When program runs it will create folders to store graphs created during run time.