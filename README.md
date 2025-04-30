```markdown
# ADHD Detection from EEG Data

This repository contains all code, data, and artifacts for our project on automated ADHD detection using 19-channel EEG recordings and classical machine learning techniques.

## 📂 Repository Structure

```
.
├── Channel_Labels.docx          # Mapping of EEG channel indices → standard 10-20 labels
├── Project-Slides.pptx          # Final presentation slides (PowerPoint)
├── README.md                    # This file
│
├── analyze_files.py             # Script to explore raw .mat EEG files & extract basic stats
├── understanding_the_data.py    # Quick Python script to compute summary statistics (mean, SD, etc.)
│
├── data_preprocess.ipynb        # Notebook: filtering, z-score normalization, artifact removal
├── feature_extraction.ipynb     # Notebook: compute time-, frequency-, and non-linear features
├── test-1.ipynb                 # Notebook: toy experiments & early model prototyping
│
├── time_features.csv            # Aggregated time-domain features for all subjects
├── freq_features.csv            # Aggregated frequency-domain features for all subjects
├── nonlinear_features_all.csv   # Aggregated non-linear / complexity features
├── merged_features.csv          # Combined feature matrix (458 features) before dimensionality reduction
└── features_selected.csv        # (Generated) Selected features via SelectKBest / LDA
```

## 🔍 Overview

1. **Data Understanding & Exploration**  
   - Raw EEG recordings (MATLAB `.mat` files) from 61 ADHD and 60 control children, 19 channels, 128 Hz sampling.  
   - Initial scripts (`analyze_files.py`, `understanding_the_data.py`) compute channel-wise ranges, means, and artifact rates.

2. **Preprocessing**  
   - Butterworth band-pass filter (0.5–45 Hz)  
   - Z-score normalization per channel  
   - Amplitude-based artifact removal (threshold ±100 µV)

3. **Feature Extraction**  
   - **Time-domain:** mean, std, skewness, kurtosis, RMS, zero crossings, peak-to-peak  
   - **Frequency-domain:** Welch PSD, delta/theta/alpha/beta/gamma band powers, spectral entropy, SEF, PSD slope  
   - **Non-linear/complexity:** approximate entropy, Higuchi fractal dimension, Hjorth mobility/complexity, Hurst exponent

4. **Dimensionality Reduction**  
   - Evaluated PCA (95% variance) and SelectKBest (ANOVA F)  
   - Final approach: supervised LDA on training split → single discriminant axis

5. **Modeling & Evaluation**  
   - Classical classifiers on LDA output: SVM, Decision Tree, Random Forest, K-Nearest Neighbors, Logistic Regression  
   - Hyperparameter tuning via grid search + 5-fold CV  
   - Held-out test set (20% stratified split) for final performance  
   - Voting ensemble of all five classifiers  

6. **Results**  
   - **Ensemble Test Performance:**  
     - Accuracy: 72.0%  
     - Precision: 68.8%  
     - Recall: 84.6%  
     - F1-Score: 75.9%  
     - ROC AUC: 78.8%  

## ⚙️ How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YourUsername/ADHD-EEG-Classification.git
   cd ADHD-EEG-Classification
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   # e.g. numpy, scipy, pandas, scikit-learn, mne, matplotlib, seaborn
   ```

3. **Explore raw data**  
   ```bash
   python analyze_files.py
   ```

4. **Preprocess & feature extraction**  
   - Open `data_preprocess.ipynb` for filtering & normalization.  
   - Open `feature_extraction.ipynb` to compute all feature CSVs.

5. **Model training & evaluation**  
   - Load `merged_features.csv`, split train/test, apply LDA on training only.  
   - Train classifiers and ensemble as shown in `model_training.ipynb` (not included).

## 🎯 Key Findings

- **LDA** on 458 features → 1 discriminant axis yields highly informative representation.  
- **SVM** + **voting ensemble** achieve balanced performance, with emphasis on high recall to minimize missed ADHD diagnoses.  
- **SelectKBest** and **PCA** were evaluated but underperformed compared to supervised LDA.
