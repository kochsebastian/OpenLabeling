
import os
import cv2
import torch
import numpy as np

class EfficientDet(object):


    def __init__(self):
        # load config
        self.detector = None
        if torch.cuda.is_available():
            self.detector = torch.load('../object_detection/efficientdet/trained_models/signatrix_efficientdet_coco.pth')
            self.detector = self.detector.cuda()
        else:
            self.detector = torch.load('../object_detection/efficientdet/trained_models/signatrix_efficientdet_coco.pth',map_location='cpu').module



    def detect(self, img, conf=0.4):
        """
         
        """
        image_size = 1024
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # boxes, confidences, classIds =  detector.detect(im_rgb)
        height, width = im_rgb.shape[:2]
        image = im_rgb.astype(np.float32) / 255
        image[:, :, 0] = (image[:, :, 0] - 0.485) / 0.229
        image[:, :, 1] = (image[:, :, 1] - 0.456) / 0.224
        image[:, :, 2] = (image[:, :, 2] - 0.406) / 0.225
        if height > width:
            scale = image_size / height
            resized_height = image_size
            resized_width = int(width * scale)
        else:
            scale = image_size / width
            resized_height = int(height * scale)
            resized_width = image_size

        image = cv2.resize(image, (resized_width, resized_height))

        new_image = np.zeros((image_size, image_size, 3))
        new_image[0:resized_height, 0:resized_width] = image
        new_image = np.transpose(new_image, (2, 0, 1))
        new_image = new_image[None, :, :, :]
        new_image = torch.Tensor(new_image)
        if torch.cuda.is_available():
            new_image = new_image.cuda()
        with torch.no_grad():
            confidences, classIds, boxes = self.detector(new_image) # boxes are xmin ymin xmax ymax
            boxes /= scale
        boxes[:,2]=boxes[:,2]-boxes[:,0] # we need x y w h
        boxes[:,3]=boxes[:,3]-boxes[:,1]
        boxes=boxes[confidences>conf].cpu() 
        classIds=classIds[confidences>conf].cpu()
        confidences=confidences[confidences>conf].cpu()

        return confidences, classIds, boxes

