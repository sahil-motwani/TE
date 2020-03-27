import cv2
import requests
import json
face_url = 'http://a3a11e5a.ngrok.io/'

#x = input('Click Image ')
#if x == 'y':
  #  camera = cv2.VideoCapture('http://192.168.0.103:8080/shot.jpg')
  #  return_value, image = camera.read()
  #  cv2.imwrite('op.jpg', image)
  #  del(camera)

values = {'id':28}
url = face_url+'verify'
files = {'image': open('op.jpg', 'rb')}
r = requests.post(url, files=files,data=values)
if r.json()['output']=="True":
    print('Verified')
    url = face_url+'detect'
    r = requests.post(url, files=files)
y = eval(r.json())
print(y)
response = {values['id']:y}
response = str(response)
newurl ='http://127.0.0.1:8000/blog/detection/'
r = requests.post(newurl,data={'res':response})
