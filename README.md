# ADHD Detection from EEG Data

This repository contains all code, data, and artifacts for our project on automated ADHD detection using 19-channel EEG recordings and classical machine learning techniques.

## 🔍 Overview

1. **Data Exploration**
   - MATLAB `.mat` EEG files (61 ADHD, 60 control), 19 channels, 128 Hz sampling
   - Scripts compute channel-wise stats: mean, variance, skewness, kurtosis, ptp

2. **Preprocessing**
   - Butterworth band-pass filter (0.5–45 Hz) removes drift & noise
   - Z-score normalization per channel (mean = 0, std = 1)
   - Amplitude-based artifact removal (±100 µV threshold)

3. **Feature Extraction**
   - **Time-domain:** mean, std, skewness, kurtosis, RMS, zero crossings, peak-to-peak
   - **Frequency-domain:** Welch PSD, delta/theta/alpha/beta/gamma band powers, spectral entropy, SEF, PSD slope
   - **Non-linear:** approximate entropy, Higuchi fractal dimension, Hjorth mobility/complexity, Hurst exponent

4. **Dimensionality Reduction**
   - PCA (95 % variance) tested → suboptimal
   - **Final:** supervised LDA applied only on training split → single discriminant axis

5. **Modeling & Evaluation**
   - Classifiers on LDA output: SVM, Decision Tree, Random Forest, KNN, Logistic Regression
   - Hyperparameter tuning: grid search + 5-fold CV
   - Held-out 20 % test split for final metrics
   - Voting ensemble of all five models

6. **Results**
   - **Ensemble Test Performance:**
     - Accuracy: 72.0 %
     - Precision: 68.8 %
     - Recall: 84.6 %
     - F1-Score: 75.9 %
     - ROC AUC: 78.8 %

## ⚙️ Installation & Usage

```bash
git clone [https://github.com/YourUsername/ADHD-EEG-Classification.git](https://github.com/YourUsername/ADHD-EEG-Classification.git)
cd ADHD-EEG-Classification
jupyter notebook
```

Explore raw data: run `analyze_files.py`
Preprocess & extract features: open and execute `data_preprocess.ipynb` and `feature_extraction.ipynb`
Train & evaluate models: implement LDA on train split, train classifiers, build ensemble

## 🤝 Collaboration & Version Control

Progress and deliverables were tracked through regular team syncs and shared document updates.
