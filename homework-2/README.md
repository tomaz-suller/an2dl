# Homework 2

[Kaggle competition]()

## Dataset
This dataset consists of segmented images from Mars terrain. Each image is paired with a mask representing the class of each pixel. Here is an example:

<div style="display: flex; justify-content: space-between;">
    <img src="github/image.png" alt="First Image" style="width: 48%;">
    <img src="github/mask.png" alt="Second Image" style="width: 48%;">
</div>

### Dataset Details
* Image Size: 64x128
* Color Space: Grayscale (1 channel)
* Input Shape: (64, 128)
* File Format: npz (Numpy archive)
* Number of Classes: 5

### Class Labels
* 0: Background
* 1: Soil
* 2: Bedrock
* 3: Sand
* 4: Big Rock
