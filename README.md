## water_quality_detection
Monitor water quality by using photos taken every minute and deep learning. 

###download_photos_webcamera
Download photos from webcamera via API. <br>

###training_model.py
Train VGG16 models by using photos. <br>
Image generator is used to increase training dataset. <br>
<br>
To get photos, photos are saved from each frames in video.

###prediction.py
Predict result to new data by using trained model.

###retraining.py
Retrain existing model by using new data.

###water_prediction.py
Summary deployed. It predicts new data by using trained model.
