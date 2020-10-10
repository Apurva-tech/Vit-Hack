# CertiPy-thon

### Team PROCODERS: 
- [x] Apurva Sharma 
- [x] Shruti Gupta
- [x] Rishikesh Rane
- [x] Gaurav Gupta

# PROBLEM STATEMENT 👩‍💻
The problem statement assigned to us was to develop an Automated Certificate Generator which maps the contents on the given certificate template, receives the data of the recipients from a normal file and prints the corresponding data on the certificate in appropriate location. 

# OUR PROPOSED MODELS 💡
1. Finding the blank spaces using cursor, implemented using OpenCV, This model can work with any template.
2. Using NLP and an Image Processing model, we detect blank spaces and process the text to print appropriate data from CSV File. This model has some limitations as an automated model might lag in accuracy. 

# APPROACH 1: 🎯

Any ML/DL/Image Processing Model trains on data to comprehend a unknown data, likewise a human being learns and develops cognitive skills through the data they have been fed. That is why our first approach focuses more on accuracy than automation. In the first approach we will be using the mouse pointer to mark the blank spaces/area of input on the template of the certificate. This can be done using the OpenCV library. The pointer marks the position where the required text needs to be entered using image processing. Then the model puts the data from the data file on the template. Hence, we are giving user the liberty, at the same time creating a automated process to generate as many certificate as the user wants.

<p  align="center"><img height= "400" width = "800" src = "https://github.com/Apurva-tech/Vit-Hack/blob/main/Assets/approach1.gif"></p>

# Let's Discuss the first model in detail :

### Instructions to run the model: 

- [x] Main Requirement is OpenCV library. OpenCV is a Computer Vision Python Library. We have used this library to process our image template
  - ✔ 1. Open your cmd
  - ```pip install opencv-python```
  - ```pip install numpy```
  - ```pip install pandas```
  - ```pip install pillow```
  - ✔ 2. Clone this Repository
  - ```git clone https://github.com/Apurva-tech/Vit-Hack.git```
  - ✔ 3. Navigate to the Certificate-Generator Folder
  - ✔ 4. Open the ```sample_mouse_pointer.py``` File
  - ✔ 5. Choose any template from the ```templates``` folder 
  - ✔ 6. Define the correct path for the template image in ```sample_mouse_pointer.py```
  - ✔ 7. Now compile the file
  - ✔ 8. Select the blank space where the data has to be placed
  - ✔ 9. Give the color of text you want
  - ✔ 10. Aaannnddd VOILA, check the ```img``` folder to see your generated certificate !!

### Please notice that our first approach focuses More on Accuracy than on Automation.
  
# APPROACH 2: 🎯
This model focuses more on Automation than Accuracy. We have tried to implement the solution using an Image Processing model. The model maps the contents of the certificate template and then uses NLP to judge which attribute from the data file should be placed in a particular location of the certificate template. The model had errors as the model requires a good amount of data to train on, hence, <strong> This is a proposed model we will like to work on the model in our future aspects of the project. </strong>

<p  align="center"><img height= "400" width = "800" src = "https://github.com/Apurva-tech/Vit-Hack/blob/main/Assets/approach2.gif"></p>

### Approach-2 : Step 1 :- Find the text on image template 
- [x] We are using tesseract to detect the text on image
  - ✔ 1. Open your cmd and create a virtual env in IP-NLP Folder
  - ```pipenv env```
  - ```env\Scripts\activate```
  - ```pip install tesseract```
  - ```pip install opencv-python```
  - ✔ 2. Refer the ```requirements.txt``` file for required installation
  - ✔ 3. In the IP-NLP Folder
  - ✔ 4. Open the ```Recognize-text.py``` File
  - ✔ 5. Choose any template from the ```templates``` folder 
  - ✔ 6. Define the correct path for the template image in ```Recognize-text.py```
  - ✔ 7. Now open the ```recognized.txt``` file 
  - ✔ 8. It contains the text on the template image 

### Approach-2 : Step 2 :- Detect the Blank space lines using a Houghlines Concept in OpenCV
- [x] Detect the blank spaces where the data has to be placed
  - ✔ 1. Open the ```Direct-lines1.py``` File
  - ✔ 2. Choose any template from the many ```templates```  
  - ✔ 3. Define the correct path for the template image in ```Direct-lines1.py```
  - ✔ 4. Now open the ```houghlines5``` image 
  - ✔ 5. The image has lines detected. 

### The detected lines would look something like this
<p  align="center"><img height= "400" width = "800" src = "https://github.com/Apurva-tech/Vit-Hack/blob/main/Assets/houghlines5.jpg"></p>

### Approach-2 : Step 3 :- Find the text on image template 
- [x] Use the text extracted to paas onto a NLP model to predict the data to be entered
  - ✔ 1. Open the ```sample.py``` File
  - ✔ 2. Choose any template from the many ```templates``` 
  - ✔ 3. Define the correct path for the template image in ```sample.py```
  - ✔ 4. Now open the ```img``` folder, it contains the certificate generated 

# Block Diagram 

<p  align="center"><img height= "1000" width = "800" src = "https://github.com/Apurva-tech/Vit-Hack/blob/main/Assets/blockdiagram.png"></p>

# Tech Stack 

<p  align="center"><img height= "500"  src = "https://github.com/Apurva-tech/Vit-Hack/blob/main/Assets/techstack.jpeg"></p>

# PYTHON LIBRARIES USED:👾
In our Image Processing model, we used the following libraries: 
- [x] OpenCV
- [x] Numpy
- [x] Pandas
- [x] Pillow
- [x] NLTK


# FUTURE SCOPE:🤖

In future we would like to make both of our models stronger, more accurate and capable of working on most of the certificate templates. However, our prime target for the time being is to work on approach 2 and build a better model so that it can work on various templates of different dimensions and having different fields to be entered. We may even plan to implement the model on an android app or web app.
