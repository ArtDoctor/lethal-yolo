from ultralytics import YOLO
import cv2


def process_image(model_path, image_path):
    model = YOLO(model_path)
    image = cv2.imread(image_path)

    results = model(image)
    annotated_image = results[0].plot()

    output_path = image_path.replace('.', '_output.')
    cv2.imwrite(output_path, annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    model_path = '/home/ash/lethal-yolo/runs/detect/train2/weights/best.pt'
    image_path = '/home/ash/lethal-yolo/bugs.webp'
    process_image(model_path, image_path)
