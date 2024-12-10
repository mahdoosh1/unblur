import cv2
from PIL import Image, ImageDraw
import numpy as np
def open_video(path, log=False, convert=False):
    output_frames = []
    cap = cv2.VideoCapture(path)
    fps = cap.
    current_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        current_frame += 1
        if log:
            print(f"Extracting frame {current_frame}")
        if convert:
            frame = Image.fromarray(frame, 'BGR')
        output_frames.append(frame)
    cap.release()
    cv2.destroyAllWindows()
    return output_frames, fps
def look_for_velocity(path, frames):
    a, b = frames[0], frames[-1]
    path_no_format = path[:len(path)-path[::-1].find('.')]
    cv2.imwrite(path_no_format+'-First.png', a)
    cv2.imwrite(path_no_format+'-Last.png', b)
    vel = eval(input('Velocity in format (x, y): '))
    return vel
def unblur(frames, vel):
    sx, sy = frames[0].width, frames[0].height
    num_frames = len(frames)
    vx, vy = vel
    
    new_frames = [
        Image.new('BGR',(
            (sx+num_frames)*vx,
            (sy+num_frames)*vy
        ),(0,0,0))
    ]*num_frames
    
    k = 0
    for new, frame in zip(new_frames,frames):
        d = ImageDraw.Draw(new)
        for i in range(sx):
            for j in range(sy):
                pix = frame.getpixel((i, j))
                nx, ny = (i+k)*vx, (j+k)*vy
                nx, ny = int(nx), int(ny)
                d.point((nx, ny), pix)
        k += 1
    return new_frames

def back_to_vid(frames):
    raw_frames = []
    for frame in frames:
        raw_frame = np.array(frame.getdata())
        raw_frames.append(raw_frame)
    # TODO:
    
path = r'C:\Users\Amin Yadi\Videos\2024-03-06 21-20-11.mkv'
frames = open_video(path)
vel = look_for_velocity(path, frames)