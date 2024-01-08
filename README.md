## Malaria Application Detector 

This is a flask app which predicts whether the given image belongs to parasite category or unparasite. I have used the concept of transfer learning in this project. I used the pre-trained [VGG-16 model architecture](https://neurohive.io/en/popular-networks/vgg16/) which was trained with ImageNet dataset. I trained this model (by freezing the in-between convolutional layers having previously trained weights) on [parasite-vs-unparasite dataset]. I am able to achieve around 92% accuracy on the validation dataset.

---
### A Glimpse of the app 
Homepage
![home](https://github.com/eng979710/malaria-Application-Detector-Flask-web-app/blob/master/screenshots/home.jpg?raw=true)
<br>

Upload page
![upload](https://github.com/eng979710/malaria-Application-Detector-Flask-web-app/blob/master/screenshots/upload.jpg?raw=true)
<br>

Prediction Page
![prediction](https://github.com/eng979710/malaria-Application-Detectoe-Flask-web-app/blob/master/screenshots/prediction.jpg?raw=true)

---
### Steps to clone this repo on local machine 
This repository contains an LFS file (VGG_model.h5) as this weights file is of 156 mb and github only allows to upload files which are less than 100 mb. So follow the steps below to clone it - 
1. Download and install [Git LFS](https://git-lfs.github.com/) on your machine.
2. Then after configuring Git LFS, open Bash console and type the usual git clone command. 
    ``` bash
    git clone https://github.com/eng979710/malaria-Application-Detector-Flask-web-app.git
    ```
---

### Steps to run the malaria Application Detector classifier app on your machine
1. Fire up the terminal in the cloned repository directory.

2. First create a virtual environment.
    ```shell
    virtualenv .env
    ```
3. Activate the virtual environment.
    ```shell
    . ./.env/Scripts/activate
    ```
4. Install the packages from requirements.txt file
    ```shell
    pip install -r requirements.txt
    ```
5. Then finally start the flask app by typing
    ```shell
    python main.py
    ```
<br>
