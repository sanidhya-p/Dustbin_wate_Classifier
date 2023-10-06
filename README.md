# Dustbin Waste Classifier


## Project Overview

The Dustbin Waste Classifier is a computer vision-based solution designed to assist in waste management and recycling efforts. It can classify various types of waste into five categories and provides recommendations for the appropriate bins for disposal.

### Classification Categories

- List of waste types that can be classified:
  0. Plastic
  1. Glass
  2. Cardboard
  3. Biological
  4. Paper

- List of bins for waste collection:
  1. Recyclable
  2. Hazardous
  3. Residual
  4. Food Waste

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Dataset](#Dataset)
- [Usage](#usage)
  - [Training](#Training) 
  - [Running the Classifier](#running-the-classifier)
  - [Interpreting the Results](#interpreting-the-results)



## Getting Started

### Prerequisites

Before using the Dustbin Waste Classifier, ensure you have the following prerequisites installed:

- Python
- OpenCV
- cvzone
- TensorFlow/Keras

## Dataset

The images used to train the Dustbin Waste Classifier were obtained from [Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification). The original dataset includes 12 classes with nearly 500 images in each class. However, for our specific project, we selected a subset of 5 classes to train the model.
## Usage

## Training
- We used Google Teachable Machine, an online tool, to create and train our custom machine learning model. Teachable Machine allows for easy uploading of images, labeling, and training of models.
- We provided labeled examples of waste images for each waste type to Teachable Machine. The platform automatically generated a model based on these examples, making it accessible and efficient for our project.
- After successful training, we exported the trained model in Keras format (keras_model.h5) for integration into our Dustbin Waste Classifier.


## Running the Classifier
run the file main2.py 
Point your webcam at the waste item you want to classify.

![Image Alt Text](https://github.com/sanidhya-p/Dustbin_wate_Classifier/blob/d4641e06e7a1798a08d98f1f22c18c195a302e96/WasteClassifiwerIMG.jpeg)


## Interpreting the Results
The classifier will provide the following results:

The type of waste (e.g., Plastic, Glass) detected in the image.
A recommendation for the appropriate bin (e.g., Recyclable, Hazardous) for disposal.



