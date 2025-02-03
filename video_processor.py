import cv2
import os


def split_video_to_images(video_path, output_folder, images_per_second=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps / images_per_second)

    frame_count = 0
    image_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % interval == 0:
            image_path = os.path.join(output_folder, f"frame_{image_count:05d}.jpg")
            cv2.imwrite(image_path, frame)
            image_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {image_count} images to {output_folder}")


if __name__ == "__main__":
    video_path = "test2.mp4"
    output_folder = "output_images"
    split_video_to_images(video_path, output_folder)
