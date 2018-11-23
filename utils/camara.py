import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    camera.meter_mode = 'matrix'
    camera.start_recording('my_video.h264', profile='constrained')
    camera.wait_recording(10)
    camera.stop_recording()
