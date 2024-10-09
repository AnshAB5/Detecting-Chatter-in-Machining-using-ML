# Chatter Detection in Machining Using Machine Learning

## Overview

This project focuses on detecting machining chatter using a combination of machine learning and signal processing techniques. Effective chatter detection helps improve surface quality and prolong tool life in manufacturing processes.

## Features

- **Machine Learning Detection**: Implemented a ResNet50 Convolutional Neural Network to identify chatter from images of machined surfaces, supplementing the mathematical model.
  
- **Signal Processing Analysis**: Applied time and frequency domain analyses, including Fast Fourier Transform (FFT), on acceleration data to detect instability.
  
- **Mathematical Modeling**: Developed models using statistical features such as Peak-to-Peak Value, Root Mean Square (RMS), Variance, and Skewness for accurate chatter identification.
  
- **Image Preprocessing**: Utilized OpenCV for image clipping and enhancement to create a high-quality dataset for training and evaluation.

- **Custom Image Labeling Script**: Developed an automated labeling script that detects the RPM and DOC (Depth of Cut) from the image file names. It prompts users to label the images as "positive" (chatter present) or "non-positive" (no chatter). Once the labeling is complete, it outputs a CSV file summarizing the labels. The image folder for output is named `output`.

## Technologies Used

- Python 3
- TensorFlow/Keras
- OpenCV
- NumPy
- SciPy

## Contact

For any questions or collaboration interests, please contact b.ansh@iitg.ac.in
