# AVASpeech - SMAD

This repository contains code, labels and metadata for AVASpeech - SMAD dataset presented in late-breaking demo, ISMIR 2021. 

## Citation

**AVASpeech-SMAD: A Strongly Labelled Speech and Music Activity Detection Dataset with Label Co-Occurrence** [[arXiv]](https://arxiv.org/pdf/2111.01320.pdf)

*- Yun-Ning Hung, Karn N. Watcharasupat, Chih-Wei Wu, Iroro Orife, Kelian Li, Pavan Seshadri, Junyoung Lee*

    @article{avaspeechSMAD,
      title     = {AVASpeech-SMAD: A Strongly Labelled Speech and Music Activity Detection Dataset with Label Co-Occurrence},
      author    = {Hung, Yun-Ning and Watcharasupat, Karn and Wu, Chih-Wei and Orife, Iroro and Li, Kelian and Seshadri, Pavan and Lee, Junyoung},
      year      = {2021},
      journal={arXiv preprint arXiv:2111.01320}
    }
    
## Dataset

1. Download audio:
    - Install [youtube-dl](https://github.com/ytdl-org/youtube-dl)
    - Run the download script ```python3 process.py```

2. Labels (in **labels/**):
    - Speech labels: from original [AVASpeech dataset](https://research.google.com/ava/download.html#ava_speech_download) [1]
    - Music labels: manually created by the authors
    
## Metadata

1. Benchmark result from the existings models (in **evaluation/**):
    - inaSpeechSegmenter [2]: results derived from this [repo](https://github.com/ina-foss/inaSpeechSegmenter)
    - synth-audio-seg [3]: results derived from this [repo](https://github.com/satvik-venkatesh/train-synth-audio-seg)

2. Statistic
    - **statistic.cvs**: music, speech and overlap labels percentage of each song.
    - **distribution/**: music, speech and overlap labels percentage distribution for the entire dataset 
    
## Code

1. **process.py**: code to download the audio and calculate the statistics

## Reference

[1] S. Chaudhuri, J. Roth, D. P. Ellis, A. Gallagher, L. Kaver, R. Marvin, C. Pantofaru, N. Reale, L. G. Reid, K. Wilson et al., “AVA-speech: A densely la- beled dataset of speech activity in movies,” in Proceed- ings of the 19th Annual Conference of the International Speech Communication Association, 2018.

[2] S. Venkatesh, D. Moffat, and E. R. Miranda, “Inves- tigating the effects of training set synthesis for audio segmentation of radio broadcast,” Electronics, vol. 10, no. 7, p. 827, 2021.

[3] D. Doukhan, E. Lechapt, M. Evrard, and J. Carrive, “INA’s MIREX 2018 music and speech detection sys- tem,” in 14th Music Information Retrieval Evaluation eXchange, 2018.

## Contact

Yun-Ning (Amy) Hung

[yhung33@gatech.edu](mailto:yhung33@gatech.edu)

