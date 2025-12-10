🔬 End-To-End Cell Segmentation Using YOLOv8 With Deployment

An end-to-end deep learning project for cell detection and segmentation using YOLOv8 instance segmentation, built and deployed as a complete pipeline.

This system detects multiple cells from microscopic images, draws bounding boxes and segmentation masks, and displays the confidence score for each detected cell.

📌 Project Overview

This project uses the YOLOv8 segmentation model to:

• Detect individual cells in microscopic images
• Draw bounding boxes around detected cells
• Generate segmentation masks
• Show confidence scores in real time
• Deploy the trained model via a web interface

With more training data and longer training time, the accuracy and detection quality significantly improve.

🚀 Features

• End-to-end training and deployment pipeline
• YOLOv8 instance segmentation
• Custom dataset training
• Real-time image inference
• Web application for prediction
• Docker support for deployment
• Modular project structure

🛠️ Tech Stack

Python
YOLOv8 (Ultralytics)
OpenCV
PyTorch
Streamlit / Flask (for UI)
Docker
HTML / CSS

📁 Project Structure

This is how your repository is structured:

.github/workflows
cellSegmentation/
components/
├── data_ingestion.py
├── data_validation.py
├── model_trainer.py

constant/
training_pipeline/
entity/
logger/
pipeline/
utils/
data/
research/
templates/

Dockerfile
app.py
requirements.txt
setup.py
template.py
README.md

📷 Sample Output

The model detects cells and displays:

• Red bounding boxes
• Label as cell
• Confidence scores
• Segmentation masks

Note: The more training data you use, the better the model performance.

⚙️ Installation

Clone the repository and move into the project folder.

Create and activate a virtual environment.

Install required dependencies using requirements.txt:

pip install -r requirements.txt

▶️ How to Run the App

Start the application locally:

python app.py

Or if using Streamlit:

streamlit run app.py

Open the browser at:

http://localhost:8501

🧪 Training the Model

To train the YOLOv8 model:

Add your custom dataset in the data/ directory

Configure parameters inside the training pipeline

Run the training script

Trained weights will be saved inside the runs/segment/ folder

Training on more data will increase model accuracy.

🐳 Docker Deployment

Build the Docker image:

docker build -t cell-segmentation-app .

Run the container:

docker run -p 5000:5000 cell-segmentation-app

📌 Future Enhancements

• Improve model accuracy with larger datasets
• Support live camera feed for detection
• Add batch image prediction
• Cloud deployment support

👨‍💻 Author

Sarthak Kelkar
GitHub: https://github.com/EasySarthak1440

📜 License

This project is licensed under the MIT License.
