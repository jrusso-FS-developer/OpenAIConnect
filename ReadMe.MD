# ReadMe Documentation for OpenAIConnect 1.0
This is the first iteration of the application OpenAIConnect. Developed as a POC/Demo application, in the Python programming language, this app explores the new possibilities/capabilities of the OpenAI library and AI engines.  Future iterations will integrate this code into a Web API controller, and/or a front end website such as React/Angular, etc...

## Software Requirements
You need to have Python >= 3.11.0 installed on your system.  Although this code will most likely work on an earlier version, it has not been tested on anything older than Python 3.11.2. 

To install Python visit the following link and complete the installation instructions. https://www.python.org/downloads/

## Clone Repo 
1. Open the terminal in VSCode, or your favorite GUI, and navigate to the folder you wish to clone the repo to.
2. Enter the following to clone the repo, ```git clone https://github.com/jrusso-FS-developer/OpenAIConnect.git```
![image](https://user-images.githubusercontent.com/13722805/229315511-b7e7aa20-80d6-46a3-a244-e05d1a0de2ed.png)
3. Once the repo is cloned, follow the steps below under 'De-bugging'.

## De-bugging
1. Open the root folder containing the repo for this project, in VSCode, or a GUI of your choice Ie. PyCharm, Sublime, etc...
2. In VSCode, open a terminal, and enter the following command to create a virtual environment in the root folder. 
        ```python -m venv /path/to/new/virtual/environment```
3. In the same terminal, now enter ```/path/to/new/virtual/environment/Scripts/activate``` to activate your new virtual environment.
4. Now install the dependencies for this project by running the following command, ```pip3 install -r requirements.txt```
5. With the virtual environment activated, now enter the following command to run the application.  ```python app.py```
6. In the terminal you will now be prompted to ask OpenAI something.  Have Fun!!!

## Details/Notes
1. Developer: Justin P. Russo
2. Inception: 4/1/2023
3. Language/Version: Python 3.11.2
