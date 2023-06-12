# BUYMEACOFFEE-CALCULATOR
![Icon](icon.png)

# Description
buymeacoffee-calculator is a python script that calculates how much did someone receive through [BuyMeACoffee](https://buymeacoffee.com).

# Previous steps

## Install the dependencies
Before you run the program you have to install the dependencies running `pip install -r requirements.txt` inside of the project directory.

**These steps would be for Linux**

## Download Gecko Driver
Additionally you have to download the [geckodriver](https://github.com/mozilla/geckodriver/releases) for you OS. This program provides the HTTP API described by the WebDriver protocol to communicate with Gecko browsers, such as Firefox. It translates calls into the Marionette remote protocol by acting as a proxy between the local and remote ends.

## Unzip tar file

`sudo tar -xvf FILENAME` Where FILENAME is the name of the downloaded tar file.

## Make Executable Permission to 'geckodriver'

`sudo chmod +x geckodriver`

## Move Gecko Driver to Binary Location

`sudo mv geckodriver /usr/local/bin/`

# Run the program

To run the program open a terminal go to the project directory and run `python3 main.py USERNAME` where `USERNAME` is the username of the person that you want to calculate the revenue.

# How it works

The program uses Selenium to click on the "See more" button until it loads the whole page so it can take the number of coffees donated and do simple maths to calculate the revenue
