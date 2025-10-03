# Neural Network Handwritten Digit Recognizer

<p align="center">
  <img src="https://github.com/user-attachments/assets/122daa65-4608-4822-85c7-09bacf6a5b35" alt="Image 1" width="300" style="border:2px solid #555; border-radius:8px; margin-right:10px;">
  <img src="https://github.com/user-attachments/assets/27de2c5a-68f4-4bbc-9286-b3f2332e617e" alt="Image 2" width="300" style="border:2px solid #555; border-radius:8px;">
</p>


A **GUI application** for recognizing handwritten digits using a simple neural network.

---

## Adding Your Own Images

If you want to test the application with your own images, here are some recommendations to get the best results:

- **Handwritten style**: Try to write digits or characters clearly, similar to MNIST dataset style.  
- **Minimal background noise**: Use images with plain or uniform backgrounds to avoid confusing the model.  
- **Good contrast**: Make sure the text is dark enough and stands out from the background.  

- **Single character per image**: For better accuracy, each image should contain only one digit

Following these guidelines will help the model recognize your handwritten input more accurately.

---


## Future Updates

Currently, the application only predicts handwritten digits. Upcoming features:

### Next Update
- Improved digit prediction accuracy
- Support for recognizing English words

### Following Update
- Recognizing full English sentences

---

## Features

- Developed with **Tkinter + ttk + tkinterdnd2**  
- Draw digits on the **canvas** or **upload/drag-and-drop images** from your computer  
- Image preprocessing: resize to **28x28**, grayscale conversion, and normalization  
- Digit prediction using a **three-layer neural network**  
- Save your canvas drawings as **PNG, JPG, or JPEG**  
- Dark theme for an appealing UI  
- User-friendly **info, warning, and error messages**

---

## Model Accuracy

| Class | Precision | Recall | F1-Score | Support |
|-------|----------|--------|----------|---------|
| 0     | 0.98     | 0.99   | 0.99     | 980     |
| 1     | 0.99     | 0.99   | 0.99     | 1135    |
| 2     | 0.98     | 0.97   | 0.98     | 1032    |
| 3     | 0.96     | 0.98   | 0.97     | 1010    |
| 4     | 0.98     | 0.98   | 0.98     | 982     |
| 5     | 0.98     | 0.97   | 0.97     | 892     |
| 6     | 0.98     | 0.98   | 0.98     | 958     |
| 7     | 0.98     | 0.97   | 0.98     | 1028    |
| 8     | 0.97     | 0.97   | 0.97     | 974     |
| 9     | 0.97     | 0.97   | 0.97     | 1009    |
| **Accuracy** | - | - | 0.98 | 10000 |
| **Macro Avg** | 0.98 | 0.98 | 0.98 | 10000 |
| **Weighted Avg** | 0.98 | 0.98 | 0.98 | 10000 |


---

## 🚀 Replacing the Model

If you have a **better model**, you can place it inside the `models/` folder.  
Make sure that your custom model follows the same **layer architecture**:

- **Input layer**: 784 neurons (for 28x28 pixel MNIST images)  
- **Hidden layer 1**: 256 neurons  
- **Hidden layer 2**: 128 neurons  
- **Output layer**: 10 neurons (digits 0–9)

---

## Requirements

### 1️⃣ Running the Application
- No additional libraries are required. Just run the app executable.

### 2️⃣ Running the Source Code / Development
- Python 3.x is required
- Install the required libraries:


```bash
pip install -r requirements.txt         
```
