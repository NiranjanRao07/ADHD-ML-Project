import os
import numpy as np
from scipy.io import loadmat

def analyze_mat_file(filepath):
    try:
        data = loadmat(filepath)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return

    print(f"\nAnalyzing file: {os.path.basename(filepath)}")
    # Print all keys in the MAT file
    keys = list(data.keys())
    print("Keys:", keys)
    
    # Identify the variable that is not a system key
    user_keys = [k for k in keys if not k.startswith('__')]
    if not user_keys:
        print("No user data found in this file.")
        return

    for key in user_keys:
        variable = data[key]
        print(f"\nVariable: {key}")
        # Print type and shape if it's a NumPy array
        if isinstance(variable, np.ndarray):
            print("Type:", type(variable))
            print("Shape:", variable.shape)
            # If the array is numerical and not too large, show basic stats
            if np.issubdtype(variable.dtype, np.number):
                print("Min:", np.min(variable))
                print("Max:", np.max(variable))
                print("Mean:", np.mean(variable))
                print("Std:", np.std(variable))
            else:
                print("Data type is not numeric.")
        else:
            print("Variable is not a NumPy array. Type:", type(variable))

def analyze_folder(folder_path):
    print(f"\n--- Analyzing folder: {folder_path} ---")
    for filename in os.listdir(folder_path):
        if filename.endswith('.mat'):
            filepath = os.path.join(folder_path, filename)
            analyze_mat_file(filepath)

# Update these paths to match your project directory structure
base_dir = "/home/niranjanrao07/ML-project"  # Change to your actual path
folders = ["ADHD_part1", "ADHD_part2", "Control_part1", "Control_part2"]

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    analyze_folder(folder_path)
