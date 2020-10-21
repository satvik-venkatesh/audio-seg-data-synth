# audio-seg-data-synth
Artificially synthesising data for audio segmentation to improve music-speech detection.

This repository contains code associated with the paper titled "Artificially Synthesising Data for Audio Classification and Segmentation to improve speech and music detection in Radio Broadcast" submitted to IEEE ICASSP 2021.

Machine learning models for audio segmentation and music-speech detection are generally trained on proprietary audio, which cannot be shared. Labelling this data is time-consuming and expensive, which discourages new researchers in this field. In this project, we artificially synthesise data that resembles radio signals by replicating the workflow of a radio DJ. 

The file [data-synthesis.ipynb](https://github.com/satvik-venkatesh/audio-seg-data-synth/blob/main/data-synthesis.ipynb) contains the code for data synthesis. The synthesised data can be stored in your personal Google Drive. The file [train-CRNN.ipynb](https://github.com/satvik-venkatesh/audio-seg-data-synth/blob/main/train-CRNN.ipynb) contains the code to train a Convolutional Recurrent Neural Network for this task. The file [detection-example.ipynb](https://github.com/satvik-venkatesh/audio-seg-data-synth/blob/main/detection-example.ipynb) performs segmentation over any audio file using the pre-trained model.

# Disclaimer
Please note that the pre-trained models are for non-commercial use only. It has been trained on some datasets that do not permit commercial use. The entire list of datasets used for training are [MUSAN](http://www.openslr.org/17/), [GTZAN music-speech](http://marsyas.info/downloads/datasets.html), [GTZAN Genre collection](http://marsyas.info/downloads/datasets.html), [Scheirer & Slaney](https://labrosa.ee.columbia.edu/sounds/musp/scheislan.html), [Instrument Recognition in Musical Audio Signals](https://www.upf.edu/web/mtg/irmas#:~:text=IRMAS%20is%20intended%20to%20be,violin%2C%20and%20human%20singing%20voice.), [Singing Voice dataset](http://isophonics.net/SingingVoiceDataset), and  [LibriSpeech](http://www.openslr.org/12/).

# Quick Start
Want to try it without installing anything? Here is a [Google Colab notebook](https://colab.research.google.com/github/satvik-venkatesh/audio-seg-data-synth/blob/main/detection-example.ipynb).


# License
The pre-trained models are under the [Create Commons Attribution-NonCommercial-ShareAlike-3.0 Unported (CC BY-NC-SA 3.0) license](https://creativecommons.org/licenses/by-nc-sa/3.0/), and the source code for the project is under the [MIT license](https://github.com/satvik-venkatesh/audio-seg-data-synth/blob/main/LICENSE). 
