import cv2
from PIL import Image
def open_video(path, log=False, convert=False):
    output_frames = []
    cap = cv2.VideoCapture(path)
    current_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        current_frame += 1
        if log:
            print(f"Extracting frame {current_frame}")
        if convert:
            frame = Image.fromarray(frame, 'RGB')
        output_frames.append(frame)
    cap.release()
    cv2.destroyAllWindows()
    return output_frames
def look_for_velocity(path, frames):
    a, b = frames[0], frames[-1]
    path_no_format = path[:len(path)-path[::-1].find('.')]
    cv2.imwrite(path_no_format+'-First.png', a)
    cv2.imwrite(path_no_format+'-Last.png', b)
    vel = eval(input('Velocity in format (x, y): '))
    return vel
def unblur(frames, vel):
    num_frames = len(frames)
    dx, dy = vel[0]/num_frames, vel[1]/num_frames
    x, y = 0, 0
    for frame in frames:

path = r'C:\Users\Amin Yadi\Videos\2024-03-06 21-20-11.mkv'
frames = open_video(path)
vel = look_for_velocity(path, frames)



