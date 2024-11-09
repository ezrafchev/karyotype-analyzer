
import cv2
import numpy as np
from skimage import io, filters, measure, segmentation
import matplotlib.pyplot as plt

def load_image(file_path):
    return cv2.imread(file_path)

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

def segment_chromosomes(image):
    thresh = filters.threshold_otsu(image)
    binary = image > thresh
    labeled = measure.label(binary)
    return labeled

def analyze_karyotype(labeled_image):
    regions = measure.regionprops(labeled_image)
    abnormalities = []
    for region in regions:
        # This is a placeholder for more complex analysis
        if region.area > 1000:  # Example threshold
            abnormalities.append(f"Large chromosome at {region.centroid}")
    return abnormalities

def main(image_path):
    image = load_image(image_path)
    preprocessed = preprocess_image(image)
    segmented = segment_chromosomes(preprocessed)
    abnormalities = analyze_karyotype(segmented)
    
    print("Detected abnormalities:")
    for abnormality in abnormalities:
        print(abnormality)

    plt.imshow(segmented, cmap='nipy_spectral')
    plt.title("Segmented Chromosomes")
    plt.show()

if __name__ == "__main__":
    # Replace with actual image path when testing
    main("path_to_karyotype_image.jpg")
