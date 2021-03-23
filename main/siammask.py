from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import argparse
import sys
import cv2
import torch
import numpy as np
from glob import glob

from pysot.core.config import cfg
from pysot.models.model_builder import ModelBuilder
from pysot.tracker.tracker_builder import build_tracker

from os.path import realpath, dirname, join, exists
# set device, depending on whether cuda is available
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')



class SiamMask(object):


    def __init__(self,classid=0,anchorid=0,init_frame=None,init_bbox=None):
        # load config
        cfg_path = '../object_detection/pysot/experiments/siamrpn_r50_l234_dwxcorr/config.yaml'
        snapshot = '../object_detection/pysot/experiments/siamrpn_r50_l234_dwxcorr/model.pth'
        cfg.merge_from_file(cfg_path)
        cfg.CUDA = torch.cuda.is_available() and cfg.CUDA
        # cfg.CUDA = False
        device = torch.device('cuda' if cfg.CUDA else 'cpu')
        # device='cpu'

        # create model
        model = ModelBuilder()

        # load model
        model.load_state_dict(torch.load(snapshot,
            map_location=lambda storage, loc: storage.cpu()))
        model.eval().to(device)

        # build tracker
        tracker = build_tracker(model)
        
        self.tracker = tracker
        self.classId = classid
        self.anchorId = anchorid
        self.init_bbox = init_bbox
        self.init_frame = init_frame
            

    def init(self, init_frame, initial_bbox):
        """
        Initialize SiamRPN tracker with inital frame and bounding box.
        """
        with torch.no_grad():
            self.tracker.init(init_frame,initial_bbox)



    def update(self, next_image):
        """
        Update bounding box position and size on next_image. Returns True
        beacuse tracking is terminated based on number of frames predicted
        in OpenLabeling, not based on feedback from tracking algorithm (unlike
        the opencv tracking algorithms).
        """
        with torch.no_grad():
            outputs = self.tracker.track(next_image)

            bbox = list(map(int, outputs['bbox']))

            score = outputs['best_score']
            if score > 0.7:
                return True, bbox
            else:
                return False, bbox

            # return True, bbox
