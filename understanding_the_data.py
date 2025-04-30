import os
from scipy.io import loadmat

def inspect_mat_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mat'):
            full_path = os.path.join(folder_path, filename)
            try:
                data = loadmat(full_path)
                print(f"\nFile: {filename}")
                print("Keys in this .mat file:", data.keys())
                # If you know a specific key (e.g., 'EEG'), you can print more details:
                # if 'EEG' in data:
                #     print("Shape of EEG data:", data['EEG'].shape)
            except Exception as e:
                print(f"Could not load {filename}. Error: {e}")

# Example usage:
inspect_mat_files("Control_part2")  # Replace with the actual path to your folder
