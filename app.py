import sys,os
from cellSegmentation.pipeline.training_pipeline import TrainPipeline
from cellSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from cellSegmentation.constant.application import APP_HOST, APP_PORT




app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"



@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/predict", methods=['POST','GET'])
@cross_origin()

def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")

        opencodedbase64 = encodeImageIntoBase64("runs/segment/predict7/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}

        # Find the latest output image file in the runs/segment directory
        output_image_path = findLatestOutputImage("runs/segment/")

        # Return the path of the latest output image
        result["output_image_path"] = output_image_path

        os.system("rm -rf runs")

        return jsonify(result)

    except KeyError:
        return Response("Key value error: Incorrect key passed", status=400)

    except ValueError as val:
        print(val)
        return Response("Value not found inside JSON data", status=400)

    except FileNotFoundError as e:
        print(e)
        return Response("No directories found in runs/segment", status=404)

    except Exception as e:
        print(e)
        return Response("Internal Server Error", status=500)


def findLatestOutputImage(directory):
    try:
        # Get a list of all directories (predict folders) in the specified directory
        predict_folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

        if not predict_folders:
            raise FileNotFoundError("No directories found in {}".format(directory))

        # Sort the directories by name (which should be predict1, predict2, ...)
        predict_folders.sort()

        # Find the latest predict folder and extract the number
        latest_predict_folder = predict_folders[-1]
        latest_predict_number = int(latest_predict_folder.split("predict")[-1])

        # Increment the predict number
        next_predict_number = latest_predict_number + 1

        # Construct the file path with the incremented predict number
        output_image_path = os.path.join(directory, f"predict{next_predict_number}", "inputImage.jpg")

        return output_image_path

    except Exception as e:
        print(e)
        raise  # Re-raise any other exceptions to handle them in the calling function

    



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
    # app.run(host='0.0.0.0', port=80) #for AZURE






