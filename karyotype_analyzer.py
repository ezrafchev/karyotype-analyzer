
import cv2
import numpy as np
from skimage import io, filters, measure, segmentation
import matplotlib.pyplot as plt
import os
import json
from datetime import datetime
from PIL import Image

# Define the samples directory
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), 'samples')

def load_image(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Image file not found: {file_path}")
    try:
        image = Image.open(file_path)
        image = np.array(image)
        if len(image.shape) == 2:  # Grayscale image
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        elif len(image.shape) == 3 and image.shape[2] == 4:  # RGBA image
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
        elif len(image.shape) == 3 and image.shape[2] == 3:  # RGB image
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image
    except Exception as e:
        raise ValueError(f"Unable to read image: {file_path}. Error: {str(e)}")

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
    chromosome_data = []
    for idx, region in enumerate(regions):
        chromosome = {
            "id": idx + 1,
            "area": region.area,
            "perimeter": region.perimeter,
            "eccentricity": region.eccentricity,
            "solidity": region.solidity,
            "centroid": region.centroid.tolist()  # Convert to list for JSON serialization
        }
        chromosome_data.append(chromosome)
        
        if region.area > 1000:
            abnormalities.append(f"Large chromosome {idx+1} at {region.centroid}")
        elif region.eccentricity > 0.8:
            abnormalities.append(f"Elongated chromosome {idx+1}")
        elif region.solidity < 0.8:
            abnormalities.append(f"Irregular shape in chromosome {idx+1}")
    
    return abnormalities, chromosome_data

def save_results(abnormalities, chromosome_data, output_path):
    report = {
        "timestamp": datetime.now().isoformat(),
        "abnormalities": abnormalities,
        "chromosome_data": chromosome_data
    }
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)

def main(sample_id, output_path):
    try:
        # Use the samples directory
        image_path = os.path.join(SAMPLES_DIR, f"{sample_id}")
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Sample image not found: {image_path}")
        
        print(f"Loading image: {image_path}")
        image = load_image(image_path)
        print(f"Image shape: {image.shape}")
        
        print("Preprocessing image...")
        preprocessed = preprocess_image(image)
        
        print("Segmenting chromosomes...")
        segmented = segment_chromosomes(preprocessed)
        
        print("Analyzing karyotype...")
        abnormalities, chromosome_data = analyze_karyotype(segmented)
        
        print("Detected abnormalities:")
        for abnormality in abnormalities:
            print(abnormality)

        print(f"Saving results to {output_path}")
        save_results(abnormalities, chromosome_data, output_path)

        plt.imshow(segmented, cmap='nipy_spectral')
        plt.title("Segmented Chromosomes")
        segmented_image_path = output_path.replace('.json', '_segmented.png')
        plt.savefig(segmented_image_path)
        plt.close()

        print(f"Results saved to {output_path}")
        print(f"Segmented image saved to {segmented_image_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    sample_id = "sample001.jpg"
    main(sample_id, f"karyotype_analysis_results_{sample_id}.json")
