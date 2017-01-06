## Documentation

- General info about using gstreamer
<https://developer.ridgerun.com/wiki/index.php?title=Gstreamer_pipelines_for_Tegra_X1#v4l2src>

- Nvidia accelerated gstreamer user guide
<http://developer.download.nvidia.com/embedded/L4T/r24_Release_v2.1/Docs/Accelerated_GStreamer_User_Guide_Release_24.2.1.pdf?autho=1483070556_cb12f3e991709ffaa188b6275a955d81&file=Accelerated_GStreamer_User_Guide_Release_24.2.1.pdf>

## Aliases

alias webcam1="gst-launch-1.0 nvcamerasrc fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! nvtee ! nvvidconv flip-method=2 ! nvoverlaysink -e"

alias webcam2="gst-launch-1.0 nvcamerasrc fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! nvvidconv flip-method=2 ! nvegltra
nsform ! nveglglessink -e"

alias webcam3="gst-launch-1.0 v4l2src device=/dev/video1 ! 'video/x-raw, width=1920, height=1080, format=(string)I420, framerate=(fraction)30/1' ! xvimagesink -e"

alias webcam_leopard="gst-launch-1.0 nvcamerasrc sensor-id=0 fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! nvvidconv flip-method=0 ! nvegltransform ! nveglglessink -e"

alias webcam_leopard_record="gst-launch-1.0 nvcamerasrc sensor-id=0 fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! omxh264enc bitrate=8000000 ! 'video/x-h264, stream-format=(string)byte-stream' ! filesink location=sample_leopard.mp4 -e"

alias webcam_logitech="gst-launch-1.0 nvcamerasrc sensor-id=3 fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! nvvidconv flip-method=0 ! nvegltransform ! nveglglessink -e"

alias webcam_logitech_record="gst-launch-1.0 nvcamerasrc sensor-id=3 fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! omxh264enc bitrate=8000000 ! 'video/x-h264, stream-format=(string)byte-stream' ! filesink location=sample_logitech.mp4 -e"
