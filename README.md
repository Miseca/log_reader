# log_reader
## About The Project
This program was built for the Mantel Group technical task which required the program to parse a log and report on
the number of unique ips, top 3 most active ips and the 3 most visited urls.

## Built With
This program was built using Python3

## Getting Started
To get started clone the repository

## Prerequisites
There are no external libraries or dependancies needed to run this program

## Usage
To get started with the program is simple, all you need to do is run the program followed by the path to a log file. 
    E.g python logReader.py "path_to_log"

To run the program with dummy code provided is as follows: 
    python logReader.py "./programming-task-example-data_1.log"

The program will then output the number of unique ip addresses, the top 3 most active ips, the top 3 most visited urls and the amount of lines flagged for errors
and an errorlog text file which includes the lines flagged as invalid. 
You may notice through the use of this program that the top 3 for active ips and urls will sometimes include more than 3 elements, that was purposeful and made to account for any variables that tie for the 3rd place position and so they are included aswell as a result. 

## Contact
Milos-Sean Selemidis - mselemidis@hotmail.com

Project Link: https://github.com/Miseca/log_reader