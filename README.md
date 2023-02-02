# Simple Face Recognition Program
This program uses OpenCV, dlib, and face_recognition to determine whether or not a given input image matches with a face recognized within a dataset of images of different people.

## Requirements
* Python 3
* OpenCV
* dlib
* face_recognition

## Usage
1. Make sure you have a dataset of images of different people stored in a single folder named "dataset". Each subfolder within the "dataset" folder should contain images of the same person.
2. Make sure you have an input image named "input.jpg" in the same directory as the python script.
3. Run the python script using the command python main.py
4. The program will check if the face within the input image (if any are detected) matches with that of a person within the dataset and will print the name of the person if match is found, otherwise it will print "No match found"
