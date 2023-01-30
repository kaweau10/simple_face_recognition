import os
import cv2
import face_recognition

# Create a list to store known faces
known_faces = []

# Create a list to store the names of the known faces
known_face_names = []

# Loop through the folders in the dataset directory
for folder in os.listdir("dataset"):
    #Check if folder var is the .DS_Store file and ignore it
    if folder == ".DS_Store": continue

    # Get the path to the current folder
    folder_path = os.path.join("dataset", folder)

    # Get the name of the current folder (which is the name of the person)
    name = folder
    
    # Loop through the images in the current folder
    for file in os.listdir(folder_path):
        # Get the path to the current image
        image_path = os.path.join(folder_path, file)
        
        # Load the current image
        image = cv2.imread(image_path)

        # Get the face encodings for the current image
        face_encodings = face_recognition.face_encodings(image)

        # If a face is detected in the current image
        if len(face_encodings) > 0:
            # Add the face encoding to the list of known faces
            known_faces.append(face_encodings[0])

            # Add the name of the person to the list of known face names
            known_face_names.append(name)

# Load the input image
input_image = cv2.imread("input.jpg")

# Get the face encodings for the input image
face_encodings = face_recognition.face_encodings(input_image)

# If a face is detected in the input image
if len(face_encodings) > 0:
    # Compare the input face encoding with the known faces
    #matches = face_recognition.compare_faces(known_faces, face_encodings[0])
    matches = face_recognition.face_distance(known_faces, face_encodings[0]) > 0.6

    # If a match is found
    if True in matches:
        first_match_index = matches.index(True)
        print("Match found:", known_face_names[first_match_index])
    else:
        print("No match found")
else:
    print("No face detected in the input image")