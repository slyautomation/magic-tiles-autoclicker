# magic-tiles-autoclicker

https://www.slyautomation.com/blog/step-by-step-coding-tutorial-creating-an-auto-clicker-to-dominate-magic-tiles/

## Introduction: 

Creating an autoclicker for the game Magic Tiles to automate the clicking process and achieve high scores effortlessly.

Purpose of the Tutorial: Guide users through developing a Python script for Magic Tiles autoclicker, providing transferrable skills for Robotic Automation Processing (RPA).

## Step 1: Set Up the Environment

Install Python and a code editor (e.g., Visual Studio Code).
Create a new project and Python script, saving it with a meaningful name.
Install necessary libraries, including pyautogui, keyboard, and pillow.

## Step 2: Capture Game Screen

Create a function to take a screenshot using ImageGrab.grab().
## Step 3: Identify Clickable Tiles

Implement a function to click on specified coordinates.
## Step 4: Implement the Auto Clicker

Create a function (run_autoclicker) to continuously check and click on identified tiles based on pixel color.
## Step 5: Implement a Fail-Safe

Add a fail-safe mechanism to stop the autoclicker if needed, triggered by the 'Num Lock' key.
Additional Function: Start Game

Create a function (start_game) to initiate the game by checking the color of the starting tile.
Enhanced Auto Clicker (run_autoclicker_v2)

Improve efficiency by checking a vertical line from the bottom of the screen upwards.
Utilize find_max_value_and_index function to prioritize the tile closest to the bottom.
Conclusion: Recap the tutorial and emphasize adjusting parameters cautiously, complying with game terms of service when using auto-clickers.
