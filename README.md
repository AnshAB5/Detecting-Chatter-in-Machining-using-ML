# Chatter Detection in Machining Using Machine Learning

## Overview

This project focuses on detecting machining chatter using a combination of machine learning and signal processing techniques. Effective chatter detection helps improve surface quality and prolong tool life in manufacturing processes.

## Features

- **Machine Learning Detection**: Implemented a ResNet50 Convolutional Neural Network to identify chatter from images of machined surfaces, supplementing the mathematical model.
  
- **Signal Processing Analysis**: Applied time and frequency domain analyses, including Fast Fourier Transform (FFT), on acceleration data to detect instability.
  
- **Mathematical Modeling**: Developed models using statistical features such as Peak-to-Peak Value, Root Mean Square (RMS), Variance, and Skewness for accurate chatter identification.
  
- **Image Preprocessing**: Utilized OpenCV for image clipping and enhancement to create a high-quality dataset for training and evaluation.

## Technologies Used

- Python 3
- TensorFlow/Keras
- OpenCV
- NumPy
- SciPy

## Installation and Usage

```bash
# Step 1: Clone the Repository
git clone https://github.com/yourusername/chatter-detection.git
cd chatter-detection

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Data Preparation
# Place raw acceleration data and surface images into the `data/raw` directory.
# Run preprocessing scripts to prepare datasets:
python preprocess_images.py
python preprocess_signals.py

# Step 4: Train Models
# Train the CNN model:
python train_cnn.py

# Train the statistical model:
python train_statistical_model.py

# Step 5: Evaluation
# Evaluate model performance on test data:
python evaluate_models.py
```
## Contact
For any questions or collaboration interests, please contact b.ansh@iitg.ac.in

