# Bone Segmenter
A modification of the Prostate Segmenter library using our bone segmentation routines with CT images

# Docker Image

## CPU

##### Downloading the docker image from the hub
```
docker pull 4Quant/bone-segmenter-cpu
```

##### Building the docker
```
docker build -t bone-segmenter-cpu -f Dockerfile.cpu .
```

##### Running the docker
```
docker run -t -v [Absolute PATH to the Project Folder]/Prostate-Segmenter/prostatesegmenter/data/test/:/home/deepinfer/data deepinfer/prostate-segmenter-cpu --InputVolume /home/deepinfer/data/input.nrrd --OutputLabel /home/deepinfer/data/label_predicted_test.nrrd
```


# Results

## Predictions
The predictions so two random images from the validation set including the predictions (middle column) by the network and the ground truth (right column). While the network does not always find smaller bones like ribs, it manages to accurately find vertebrae and hips.

![Predictions](figures/boneseg_predictions.png)

## Training Score

Here we show the training progress and corresponding DICE score.

![Training Results](figures/boneseg_training.png)