# heels_detector

### Requirements
###### Install opencv - go to https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/ and follow the instructions
### Steps of creating the classifier
###### 1. Create a folder and name it **positive**. Place all positive images (*images only containing the object you want to detect*) here. Its best if they are of the same size
###### 2. Create a folder and name it **negative**. Place all negative images (*images of anything but he object we want to detect*) here. Its best if they are of the same size.
###### 3 Create a folder and name it **data** - where the haarcascade xml file will be generated.
###### 4. open terminal and cd into your project folder. type `find positive -iname "*.<your_image_file_extension>" -exec echo \{\} 1 0 0 <width> <height> \; > positive.info`
###### 4. Type `find negative -iname "*.your_image_file_extension" > negative.txt`
###### 6. opencv_createsamples -info positive.info -num 550 -w 48 -h 24 -vec heels.vec
###### 7. opencv_traincascade -data data -vec heels.vec -bg negative.txt -numPos <value_slighty_less_than_count_in_positive_folder> -numNeg <number_of_images_in_negative_folder> -numStages <number_of_train_sages> -w <width_of_images> -h <height_of_images> -featureType LBP
###### The xml files will be generated in the data folder. User the one named `cascade.xml`
### References
###### https://abhishek4273.com/2014/03/16/traincascade-and-car-detection-using-opencv/