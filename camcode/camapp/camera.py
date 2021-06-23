import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import datetime
from django.shortcuts import render


class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture('http://127.0.0.1:8000/static/akash.jpg')

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()


class IPWebCam(object):
	def __init__(self):
		self.video = cv2.VideoCapture('static/Funny CCTV VIDEOS _ funny videos _ Comedy videos _ Comedy funny videos.mp4')

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		frame_flip = cv2.flip(image,1)

		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

		
class LiveWebCam(object):
	def __init__(self):
		self.url = cv2.VideoCapture("rtsp://admin:Mumbai@123@203.192.228.175:554/")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()
import cv2

names = ['/home/saiful/Videos/Apocalypto 2006 Bluray HD Full Movie Download BY Ripon.MP4',
         '/home/saiful/Videos/Baaghi 3 2020 New Latest Hindi Full Movie 2020.mp4',
         '/home/saiful/Videos/Bahubali 2 (2017) 1CD DVDSCR x264 700MB MKV [DoriDro.Com].mkv',
         '/home/saiful/Videos/Extraction (2020) Dual Audio Hindi 720p WEB-DL x264 AAC 1.2GB(BDmusicKing.Net).mkv']