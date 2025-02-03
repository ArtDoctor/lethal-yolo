# Lethal YOLO

![Lethal YOLO Demo](example.gif)

## Project Description
Lethal YOLO is an object detection system that uses the YOLO11n model to detect entities from Lethal Company. Right now only hoarding bugs are supported.

## Installation
To install the necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Training
The main training process happens in yolo-finetune.ipynb. Note that you need a Roboflow dataset to train the model.

## Usage
To run the object detection, you can use testing.py script. Just change the paths there and you can run it using:
```bash
python testing.py
```

## Comment
I fine-tuned the model using only 42 images. To be honest, I was surprised that the model worked so well with such small amount of data.  
Next steps would most likely be increasing the dataset size and adding more detection classes (snareflee, coilhead, etc.).

## License
This project is licensed under the MIT License.
