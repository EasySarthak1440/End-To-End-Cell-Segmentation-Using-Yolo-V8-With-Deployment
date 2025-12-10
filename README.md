END-TO-END CELL SEGMENTATION USING YOLOv8

------------------------------------------------------------

PROJECT OVERVIEW

This project performs cell instance segmentation from microscopy images using the YOLOv8 model.
It provides a complete pipeline including data ingestion, validation, training, and deployment-ready inference.

The project is structured in a modular way and is suitable for real-world production use.


FEATURES

- Cell instance segmentation using YOLOv8
- Modular pipeline architecture
- Data ingestion and validation modules
- Automated model training
- Inference on new images
- Streamlit web interface
- Docker-ready deployment


TECH STACK

- Python 3.10+
- PyTorch
- Ultralytics YOLOv8
- OpenCV
- NumPy
- Streamlit
- Docker


PROJECT STRUCTURE

End-To-End-Cell-Segmentation-Using-Yolo-V8-With-Deployment/
|
|-- app.py
|-- Dockerfile
|-- README.md
|-- requirements.txt
|-- setup.py
|-- template.py
|
|-- artifacts/
|   |-- model_trainer/
|       |-- best.pt
|
|-- cellSegmentation/
|   |-- components/
|   |   |-- data_ingestion.py
|   |   |-- data_validation.py
|   |   |-- model_trainer.py
|   |
|   |-- constant/
|   |   |-- training_pipeline/
|   |       |-- __init__.py
|   |
|   |-- entity/
|   |   |-- artifacts_entity.py
|   |   |-- config_entity.py
|   |
|   |-- exception/
|   |   |-- __init__.py
|   |
|   |-- logger/
|   |   |-- __init__.py
|   |
|   |-- pipeline/
|   |   |-- training_pipeline.py
|   |   |-- __init__.py
|   |
|   |-- utils/
|       |-- main_utils.py
|       |-- __init__.py
|
|-- data/
|   |-- cell_data.zip
|   |-- inputImage.jpg
|
|-- research/
|   |-- trials.ipynb
|   |-- trials.py
|   |-- yolov8_instance_segmentation_on_custom_dataset.ipynb
|
|-- runs/
|   |-- segment/
|       |-- predict*/
|           |-- inputImage.jpg
|
|-- templates/
|   |-- index.html


INSTALLATION

1. Clone the repository

git clone https://github.com/your-username/End-To-End-Cell-Segmentation-Using-Yolo-V8-With-Deployment.git
cd End-To-End-Cell-Segmentation-Using-Yolo-V8-With-Deployment


2. Create and activate virtual environment

python -m venv venv

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


HOW TO RUN

Start the Streamlit app:

streamlit run app.py


MODEL TRAINING

Run the training pipeline:

python cellSegmentation/pipeline/training_pipeline.py


MODEL WEIGHTS LOCATION

artifacts/model_trainer/best.pt


PREDICTION OUTPUTS LOCATION

runs/segment/predict*/


DOCKER USAGE

Build image:

docker build -t cell-segmentation-yolov8 .

Run container:

docker run -p 8501:8501 cell-segmentation-yolov8


AUTHOR

Sarthak Kelkar


LICENSE

MIT License
