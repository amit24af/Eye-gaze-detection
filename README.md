# Eye gaze detection
In this project, gaze-based signals were used to distinguish between typically developing (TD) children and those with ASD. The goal was to build robust classification models capable of supporting early diagnosis.

---

# 📊 Dataset
We used the “Eye Tracking Autism” dataset from Kaggle, consisting of:
25 CSV files containing eye-tracking time-series data from 59 participants
Metadata file with participant age, gender, group label (TD/ASD), and CARS scores
Features include pupil diameter, gaze coordinates, tracking ratio, AOIs, and more
✅ Balanced: ~50% ASD / 50% TD
✅ Age range: 2.7 – 12.9 years
✅ Data preprocessed: cleaned, normalized, aggregated, standardized

---

### 📈 Methodology Flowchart

![Pipeline Diagram](flowchart.png)

---
## 🧠 Model Architectures

| Model | Description |
|-------|-------------|
| **LSTM + Attention** | Bidirectional LSTM with memory and focus on relevant gaze segments |
| **1D CNN** | Applies convolution over time-series segments |
| **Random Forest** | Works on aggregated statistical features; interpretable |
| **MLP** | Fully connected layers using aggregated gaze stats |

---

## ✅ Evaluation Summary

| Model | Accuracy | Precision (ASD) | Recall (ASD) | AUC |
|-------|----------|-----------------|--------------|-----|
| **LSTM + Attention** | 81.3% | 73% | 77% | 0.894 |
| **1D CNN** | 82.6% | 73.9% | 74.8% | — |
| **Random Forest (Tuned)** | 70.0% | 72% | 55% | — |
| **MLP** | 71.6% | 74% | 57% | — |

---

## 🧰 Technologies Used

- `Python` (Pandas, NumPy, Scikit-learn)
- `TensorFlow/Keras` for LSTM and CNN
- `Streamlit` for web deployment
- `Matplotlib` / `Seaborn` for visualization
- `Lucidchart` for methodology diagram

---

## ✔️ Strengths and Limitations

**Strengths:**
- Sequence models that capture eye movement dynamics
- Balanced dataset with metadata
- Models tested and compared across different paradigms

**Limitations:**
- Small sample size (n = 59)
- Some missing gaze data and tracking noise
- Dataset only covers children in a narrow age range

---

## 🚀 Future Work

- Expand dataset (more participants, diverse age/gender groups)
- Incorporate multimodal features (audio, facial expressions)
- Combine CNN and LSTM in hybrid models
- Improve interpretability with SHAP or LIME
- Real-time optimized deployment for clinical screening

---
