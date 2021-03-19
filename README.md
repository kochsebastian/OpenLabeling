# AutoLabeling: open-source image and video labeler

This is a more advanced version of OpenLabeling. Improvements include a build in object detector to quickly label known objects, an advanced and more stable tracker for tracking labeled objects over a long time, and build-in automated track-id generation to keep track of individual objects.


<img src="https://media.giphy.com/media/l49JDgDSygJN369vW/giphy.gif" width="40%"><img src="https://media.giphy.com/media/3ohc1csRs9PoDgCeuk/giphy.gif" width="40%">
<img src="https://media.giphy.com/media/3o752fXKwTJJkhXP32/giphy.gif" width="40%"><img src="https://media.giphy.com/media/3ohc11t9auzSo6fwLS/giphy.gif" width="40%">



<!-- ## Latest Features

- Jun 2019: Deep Learning Object Detection Model
- May 2019: [ECCV2018] Distractor-aware Siamese Networks for Visual Object Tracking
- Jan 2019: easy and quick bounding-boxe's resizing!
- Jan 2019: video object tracking with OpenCV trackers!
- TODO: Label photos via Google drive to allow "team online labeling".
[New Features Discussion](https://github.com/Cartucho/OpenLabeling/issues/3) -->

## Table of contents

- [Quick start](#quick-start)
- [Prerequisites](#prerequisites)
- [Run project](#run-project)
- [GUI usage](#gui-usage)
- [Authors](#authors)

## Quick start

```
git clone --recurse-submodules git@github.com:kochsebastian/AutoLabeling.git
conda install --yes --file requirements.txt
```

### Prerequisites

#### Detector:   
The detector models are already provided in the EfficientDet submodule

#### Tracker:

Download siamrpn_r50_l234_dwxcorr model from 
[Google Drive](https://drive.google.com/drive/folders/1rkj6UHyNSUUtwi7FwTSqCAVxgESS6S3_?usp=sharing) and put it into 
```
object_detection/pysot/experiments/
```

    
### Run manual mode

  1. Navigate to `main/` 
  2. (Swap Detector and Tracker)
  3. (Edit **class_list.txt**)
  4. Run the code:

         python main.py [-h] [-i] [-o] [-t] [--tracker TRACKER_TYPE] [-n N_FRAMES] [--detector DETECTOR_TYPE]

         optional arguments:
          -h, --help                Show this help message and exit
          -i, --input               Path to images and videos input folder | Default: input/
          -o, --output              Path to output folder | Default: output/
          -t, --thickness           Bounding box and cross line thickness (int) | Default: -t 2
          --tracker tracker_type    tracker_type being used: ['SiamMask']
          --detector detector_type    detector_type being used: ['EfficentDet']
          -n N_FRAMES               number of frames to track 

### Run auto mode

  1. Navigate to `main/` 
  2. (Swap Detector and Tracker)
  3. (Edit **class_list.txt**)
  4. Run the code:

         python main.py [-h] [-i] [-o] [-t] [--tracker TRACKER_TYPE] [--detector DETECTOR_TYPE]

         optional arguments:
          -h, --help                Show this help message and exit
          -i, --input               Path to images and videos input folder | Default: input/
          -o, --output              Path to output folder | Default: output/
          -t, --thickness           Bounding box and cross line thickness (int) | Default: -t 2
          --tracker tracker_type    tracker_type being used: ['SiamMask']
          --detector detector_type    detector_type being used: ['EfficentDet']



### GUI usage

Keyboard, press: 

<img src="https://github.com/Cartucho/OpenLabeling/blob/master/keyboard_usage.jpg">

| Key | Description |
| --- | --- |
| a/d | previous/next image |
| s/w | previous/next class |
| e | edges |
| o | make prediction with detector |
| h | help |
| \space\ | save |
| q | save and quit |

Video:

| Key | Description |
| --- | --- |
| p | predict labels of the next frame |
| x | stop tracking |

Mouse:
<img src="https://github.com/kochsebastian/AutoLabeling/blob/master/object_interaction.jpg">
  - To create a bounding box do a left click for the top left corner and do a left click for the bottom right corner 
  - Use right click on object to quick delete
  - Use mouse wheel to zoom in and out
  - Use double click to select a bounding box
  - Use seperators to correct the bounding box
  - Use *X* to remove this and all the bounding boxes in the following frames with the same id
  - Click the green box to make the object non-trackable 



## Original Repo

  **João Cartucho**
```bibtex
@INPROCEEDINGS{8594067,
  author={J. {Cartucho} and R. {Ventura} and M. {Veloso}},
  booktitle={2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)}, 
  title={Robust Object Recognition Through Symbiotic Deep Learning In Mobile Robots}, 
  year={2018},
  pages={2336-2341},
}
```