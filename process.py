import numpy as np
import os
import csv


def _extract_activation_roll(name, duration=90*16000, hop_size=160, sr=16000, split='\t'):
    activation_roll = np.zeros((int(duration/hop_size), 1)) # music, speech
    file = open(name, 'r')
    lines = file.readlines()
    for line in lines:
        start, end, label = line.strip().split(split)
        start = int(float(start)*sr/hop_size)
        end = int(float(end)*sr/hop_size)
        activation_roll[start:end] = 1
    return activation_roll

def statistic_calculation():
    speech_percents, music_percents, overlap_percents = [], [], []

    for key in os.listdir('music labels'):
        music_labels = _extract_activation_roll(f'music labels/{key}', split=',')
        speech_labels = _extract_activation_roll(f'speech labels/{key}')
        labels = np.concatenate((music_labels, speech_labels), 1)
        
        # calculate speech and music percentage
        percentages = (labels.sum(0)/len(labels))
        music_percents.append(percentages[0])
        speech_percents.append(percentages[1])

        # calculate overlap percent
        overlap = len(np.where(labels.sum(1)==2)[0])/len(labels)
        overlap_percents.append(overlap)
        print(f'{key} / Music: {str(percentages[0])}% / Speech: {str(percentages[1])}% / Overlap: {str(overlap)}')

    print(f'Avg Music: {str(sum(music_percents)/len(music_percents))}% / Speech: {str(sum(speech_percents)/len(speech_percents))}% / Overlap: {str(sum(overlap_percents)/len(overlap_percents))}')

statistic_calculation()