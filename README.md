

---

```markdown
# End-To-End Cell Segmentation Using YOLOv8 With Deployment

A complete end-to-end computer vision project for **cell instance segmentation** using **YOLOv8**, including training pipelines, validation, prediction, and deployment-ready structure.

---

## 🔍 Project Overview

This project performs **cell segmentation from microscopy images** using the YOLOv8 instance segmentation model.  
It includes a structured MLOps-style pipeline for data ingestion, validation, model training, and prediction, along with a Streamlit-based user interface and Docker deployment support.

The system is designed to be modular, scalable, and production-ready.

---

## 🚀 Features

- Cell **instance segmentation** using YOLOv8
- Modular MLOps-style pipeline architecture
- Data ingestion and validation modules
- Automated training pipeline
- Inference pipeline for new images
- Streamlit web interface
- Docker-ready deployment
- Structured logging and exception handling

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Frameworks/Libraries:**  
  - PyTorch  
  - Ultralytics YOLOv8  
  - OpenCV  
  - NumPy  
  - Streamlit  
- **Tools:** Docker, Git, VS Code

---

## 📁 Project Structure

```

End-To-End-Cell-Segmentation-Using-Yolo-V8-With-Deployment/
│
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
├── setup.py
├── template.py
│
├── artifacts/
│   └── model_trainer/
│       └── best.pt
│
├── cellSegmentation/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   └── model_trainer.py
│   │
│   ├── constant/
│   │   └── training_pipeline/
│   │       └── **init**.py
│   │
│   ├── entity/
│   │   ├── artifacts_entity.py
│   │   └── config_entity.py
│   │
│   ├── exception/
│   │   └── **init**.py
│   │
│   ├── logger/
│   │   └── **init**.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── **init**.py
│   │
│   └── utils/
│       ├── main_utils.py
│       └── **init**.py
│
├── data/
│   ├── cell_data.zip
│   └── inputImage.jpg
│
├── research/
│   ├── trials.ipynb
│   ├── trials.py
│   └── yolov8_instance_segmentation_on_custom_dataset.ipynb
│
├── runs/
│   └── segment/
│       └── predict*/
│            └── inputImage.jpg
│
└── templates/
└── index.html

````

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/End-To-End-Cell-Segmentation-Using-Yolo-V8-With-Deployment.git
cd End-To-End-Cell-Segmentation-Using-Yolo-V8-With-Deployment
````

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Run Streamlit App

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧠 Training the Model

You can start the full training pipeline using:

```bash
python cellSegmentation/pipeline/training_pipeline.py
```

This will:

* Ingest data
* Validate datasets
* Train YOLOv8 model
* Save weights to:

```
artifacts/model_trainer/best.pt
```

---

## 🔮 Running Predictions

To run predictions on a new image:

```bash
python app.py
```

Or use the Streamlit UI to upload:

```
data/inputImage.jpg
```

Predicted results are stored in:

```
runs/segment/predict*/
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t cell-segmentation-yolov8 .
```

### Run Docker Container

```bash
docker run -p 8501:8501 cell-segmentation-yolov8
```

---

## 📈 Future Improvements

* Add model versioning
* Improve segmentation mask post-processing
* Add batch image upload feature
* Add model evaluation dashboards

---

## 👨‍💻 Author

**Sarthak Kelkar**
AI Engineer



Just tell me: **"make downloadable file"**
```
