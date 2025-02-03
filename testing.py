from ultralytics import YOLO
import cv2


def process_video(model_path, video_path):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = video_path.replace('.mp4', '_output.mp4')
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model(frame)
            annotated_frame = results[0].plot()
            out.write(annotated_frame)
            # cv2.imshow('yolov11n', annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    model_path = '/home/ash/lethal-yolo/runs/detect/train2/weights/best.pt'
    video_path = '/home/ash/lethal-yolo/test.mp4'
    process_video(model_path, video_path)
