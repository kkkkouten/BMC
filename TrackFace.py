#!/usr/bin/python
# coding: utf-8
# created by Tei


import os
import dlib
import cv2


def mkdir(save_path):
    "save path is the folder where you wanna put"
    "save_path = directory + new_folder_name"
    "eg: save_path = './user/download' + '/' + 'new_folder_name' "
    "therefore, save_path = './user/download/new_folder_name"

    folder = os.path.exists(save_path)

    if not folder:
        os.makedirs(save_path)
        print('new folder finished ')

    else:
        print('folder exited')
        print('please input other new folder name')


def read_files(file_path, print_=True):
    "file_path is the videos without tracking face"
    "file_path incude all of videos"

    files = os.listdir(file_path)

    if print_:
        return files

    else:
        return print('read files finished')


def track_face(image, fill=2):
    "only change fill, do not change anythind else"
    'fill means rectangle width'
    'fill = -1 -->  entirely fill'
    'fill = 1,2,3,... --> rectangle width'

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # gray video
    faces = detector(gray, 1)  # track model

    for face in faces:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()

        #  a rectangle of left top and right bottom
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), fill)
        # cv2.imshow('image', image)


def track_func(file_path, files, save_path, fill):

    for file in files:
        video_path = file_path + '/' + str(file)
        cap = cv2.VideoCapture(video_path)  # read videos
        fps = cap.get(cv2.CAP_PROP_FPS)  # get fps
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # get graphics
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # video type
        videoWriter = cv2.VideoWriter(save_path + '/' + str(file), fourcc, fps, size, isColor=True)

        while True:
            tolerance, frame = cap.read()
            if tolerance is False:
                break
            track_face(frame,fill)
            videoWriter.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # cap.release()
        # videoWriter.release()
        # cv2.destroyAllWindows()
    return 'end coding'

if __name__ == '__main__':

    # All videos based on .avi type, other video type need to update params

    # example
    file_path = 'path_0/original_videos'
    save_path = 'path_1/tack_face_videos'

    mkdir(save_path)  # creat folder that you wanna save

    files = read_files(file_path,print_=True)  # import all videos name for reading data and output data name

    detector = dlib.get_frontal_face_detector()  # import face recognization model
    track_func(file_path, files, save_path, fill=-1)
