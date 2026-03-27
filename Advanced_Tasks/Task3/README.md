# 🏠 Multimodal Machine Learning: Housing Price Prediction

## 📌 Overview

This project implements a **Multimodal Machine Learning model** to predict house prices using both:

* 🧾 **Structured (tabular) data**
* 🖼️ **Visual (image) data**

The model combines features extracted from house images using **Convolutional Neural Networks (CNNs)** with numerical features such as number of bedrooms, bathrooms, and area.

---

## 🎯 Objective

The goal of this project is to:

* Predict housing prices using **multiple data modalities**
* Combine **image features + tabular features**
* Evaluate performance using regression metrics

---

## 📂 Dataset

This project uses the **Houses Dataset** introduced in the paper:
**"House Price Estimation from Visual and Textual Features"**

* 📄 Paper: https://arxiv.org/pdf/1609.08399.pdf
* 👥 Authors: Ahmed, Eman & Moustafa, Mohamed

### 📊 Dataset Details

* **Total Houses:** 535
* **Total Images:** 2140 (4 per house)
* **Images per house:**

  * Bedroom
  * Bathroom
  * Kitchen
  * Front view

### 🧾 Tabular Features

Each house includes the following attributes:

* Number of Bedrooms
* Number of Bathrooms
* Area
* Zipcode
* Price (Target Variable)

### 📁 Files

* `HousesInfo.txt` → Tabular data
* Image files → Named like:

  * `1_front.jpg`
  * `1_bedroom.jpg`
  * `1_bathroom.jpg`
  * `1_kitchen.jpg`

---

## ⚙️ Technologies Used

* Python 🐍
* PyTorch 🔥
* Torchvision
* Pandas & NumPy
* Scikit-learn

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing

* Loaded `HousesInfo.txt` using pandas
* Converted tabular data to numeric format
* Handled missing values
* Standardized features using **StandardScaler**

### 2️⃣ Image Processing

* Resized images to **224×224**
* Normalized using ImageNet statistics
* Used **ResNet18** as a feature extractor

### 3️⃣ Feature Extraction

* Extracted image features using CNN
* Flattened CNN output (512 features)

### 4️⃣ Feature Fusion

* Combined:

  * Tabular features
  * Image features
* Used concatenation to form a unified feature vector

### 5️⃣ Model Architecture

* CNN: ResNet18 (pretrained)
* Fully Connected Layers:

  * 512 + tabular features → 256 → 64 → 1
* Output: Predicted house price

### 6️⃣ Training

* Loss Function: **Mean Squared Error (MSE)**
* Optimizer: **Adam**
* Epochs: 20

---

## 📈 Evaluation Metrics

The model is evaluated using:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**

Example Results:

```
MAE  ≈ 540,000  
RMSE ≈ 645,000  
```

---

## 💾 Model Saving

The trained model is saved using:

```python
torch.save(model.state_dict(), 'multimodal_model.pth')
```

Scaler is saved using:

```python
joblib.dump(scaler, 'tabular_scaler.pkl')
```

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install torch torchvision pandas numpy scikit-learn pillow joblib
```

### 2️⃣ Run Training

```bash
python multimodal_model.py
```

---

## 📌 Project Structure

```
project/
├── HousesInfo.txt
├── images/
│   ├── 1_front.jpg
│   ├── 1_bedroom.jpg
│   └── ...
├── multimodal_model.py
├── multimodal_model.pth
├── tabular_scaler.pkl
└── README.md
```

---

## 📚 Skills Gained

* Multimodal Machine Learning
* CNN Feature Extraction
* Feature Fusion (Image + Tabular)
* Regression Modeling
* Model Evaluation

---

## 📖 Citation

If you use this dataset, please cite:

```bibtex
@article{ahmed2016house,
  title={House price estimation from visual and textual features},
  author={Ahmed, Eman and Moustafa, Mohamed},
  journal={arXiv preprint arXiv:1609.08399},
  year={2016}
}
```

And:

```bibtex
H. Ahmed E. and Moustafa M. (2016).
House Price Estimation from Visual and Textual Features.
Proceedings of IJCCI 2016.
```

---

## 🔮 Future Improvements

* Use **all 4 images per house** instead of only frontal image
* Apply **data augmentation**
* Use advanced models like **EfficientNet / Vision Transformers**
* Add **zipcode embedding**
* Deploy model using **Streamlit**

---

## ✅ Conclusion

This project demonstrates how combining **visual and structured data** can improve predictive performance in real-world problems like housing price estimation. It highlights the power of **multimodal deep learning** in regression tasks.

---
