# 🚀 AI Image Enhancer (Real-ESRGAN)

An AI-powered web application that enhances image quality using **Real-ESRGAN** and **PyTorch**, built with a **Flask** backend.

---

## 📌 Features

* 🖼️ Image Super Resolution (Upscaling)
* ✨ Noise Reduction & Sharpening
* ⚡ Fast Processing with Optimized Memory Usage
* 📊 Progress Tracking (Real-time)
* 🌐 Simple Web Interface (Flask)

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **AI Model:** Real-ESRGAN
* **Libraries:** PyTorch, OpenCV, Basicsr
* **Frontend:** HTML, CSS

---

## 📁 Project Structure

AI_IMAGE_ENHANCER/
│
├── app.py
├── requirements.txt
│
├── models/
│   └── realesr-general-x4v3.pth  (Download manually)
│
├── utils/
│   └── image_enhancer.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── uploads/
│   └── outputs/

---



## 📥 Download Model (IMPORTANT)

Download the model file from:

👉 https://github.com/xinntao/Real-ESRGAN/releases

Download:

```
realesr-general-x4v3.pth
```

Place it inside:

```
models/
```

---

## ▶️ Run the Application

```bash
python app.py

```
Then open in browser:
```

## 🧠 How It Works

1. User uploads an image
2. Image is processed using Real-ESRGAN AI model
3. Image is enhanced (resolution + quality)
4. Enhanced image is displayed and saved

---

## ⚠️ Notes

* Supports only **JPG, JPEG, PNG**
* Model file is not included due to size

