# **Classification of Metals and Plastics using CNN**  

## 📌 Project Overview  
This project presents a **Convolutional Neural Network (CNN)** designed for the classification of **metals and plastics** from image data. The model is developed using **TensorFlow and Keras**, leveraging advanced deep learning techniques to achieve high classification accuracy.  

---

### This work has been **successfully published** as a **research paper**:  

📄 **A Novel Approach for Classification of Metals and Plastics under the Methodology of Deep Learning using Convolutional Neural Networks** 🔗 [IEEE Xplore – Read the Paper](https://ieeexplore.ieee.org/abstract/document/10307663)  

## **Abstract:**  
This research introduces a fully **automated solution** for waste segregation in the recycling process. The primary challenge in recycling is the **classification and separation** of materials, specifically plastics and metals. Our proposed CNN-based model efficiently categorizes waste materials, ensuring seamless classification with high accuracy.  

The system enables real-time classification, storing results in a structured format for further analysis. By leveraging **Deep Learning Neural Networks**, the model enhances the **efficiency and accuracy** of material segregation, reducing human effort, optimizing resource allocation, and contributing to **environmental sustainability**. The study demonstrates the effectiveness of **CNN-based classification** for waste management, offering a scalable and deployable solution for recycling industries.  

---

## 🔍 **Process**  

### **1. Data Preparation**  
- Images are preprocessed and normalized for CNN training.  
- Labels are extracted and mapped to images for supervised learning.  

### **2. Model Development**  
- Developed using **Keras Sequential API**, comprising multiple **convolutional layers**, activation functions, pooling layers, and dense layers.  

### **3. Training and Evaluation**  
- The model is trained with **batch processing** and optimized hyperparameters.  
- Performance is measured using **validation metrics** and **accuracy scores**.  

### **4. Model Persistence**  
- The trained model is stored in **H5 format** for efficient deployment and scalability.  

---

## ✨ **Features**  

- **Convolutional Layers** – Extracts features using **ReLU activation** and **max pooling**.  
- **Dense Layers** – Uses **sigmoid activation** for binary classification.  
- **TensorBoard Integration** – Monitors and visualizes model training.  
- **Data Normalization** – Scales image data for improved learning efficiency.  
- **Model Storage** – Saves the trained model in **H5 format** for reuse.  

---

## 🛠 **Tech Stack**  

- **Programming Language:** Python  
- **Deep Learning Frameworks:** TensorFlow, Keras  
- **Data Handling:** NumPy, Pickle  
- **Model Storage:** H5 format  

---

## 📂 **Project Structure**  
```
classification-using-cnn/
├── Cam.py                # Real-time classification script  
├── Loading.py            # Dataset loading and preprocessing  
├── MPmodel.h5            # Trained CNN model  
├── README.md             # Project documentation  
├── Testing.py            # Model evaluation script  
├── Training.py           # Model training script  
├── Training_JL.ipynb     # Jupyter Notebook for model training  
├── X.pickle              # Preprocessed feature data  
├── y.pickle              # Preprocessed labels  
└── logs/                 # TensorBoard logs for training visualization  
```  

---

## 🚀 **Getting Started**  

### **Prerequisites**  
Ensure the following dependencies are installed:  
- Python 3.x  
- TensorFlow  
- Keras  
- NumPy  
- Pickle
