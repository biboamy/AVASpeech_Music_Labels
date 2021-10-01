import numpy as np
import os
import csv
import matplotlib.pyplot as plt


def _extract_activation_roll(name, duration=900*16000, hop_size=160, sr=16000, split='\t'):
    activation_roll = np.zeros((int(duration/hop_size), 1)) # music, speech
    file = open(name, 'r')
    lines = file.readlines()

    for line in lines:
        start, end, label = line.strip().split(split)
        start = int(round(float(start)*sr/hop_size))
        end = int(round(float(end)*sr/hop_size))
        activation_roll[start:end] = 1

    return activation_roll

def statistic_calculation():
    speech_percents, music_percents, overlap_percents = [], [], []

    new_csvfile = open(os.path.join('statistic.csv'), 'w') 
    csvwriter = csv.writer(new_csvfile)
    csvwriter.writerow(['id', 'Music %', 'Speech %', 'Overlap %'])

    for key in os.listdir('music labels'):
        music_labels = _extract_activation_roll(f'music labels/{key}', split=',')
        speech_labels = _extract_activation_roll(f'speech labels/{key}')
        labels = np.concatenate((music_labels, speech_labels), 1)
        
        # calculate speech and music percentage
        percentages = (labels.sum(0)/len(labels)) * 100
        music_percents.append(percentages[0])
        speech_percents.append(percentages[1])

        # calculate overlap percent
        overlap = len(np.where(labels.sum(1)==2)[0])/len(labels) * 100
        overlap_percents.append(overlap)
        print(f'{key} / Music: {str(percentages[0])}% / Speech: {str(percentages[1])}% / Overlap: {str(overlap)}')

        csvwriter.writerow([key.split('.')[0], percentages[0], percentages[1], overlap])


    print(f'Avg Music: {str(sum(music_percents)/len(music_percents))}% / Speech: {str(sum(speech_percents)/len(speech_percents))}% / Overlap: {str(sum(overlap_percents)/len(overlap_percents))}')
    print(f'Min Music: {str(min(music_percents))}% / Max Music: {str(max(music_percents))}% ')
    print(f'Min Speech: {str(min(speech_percents))}% / Max Speech: {str(max(speech_percents))}% ')
    print(f'Min Overlap: {str(min(overlap_percents))}% / Max Overlap: {str(max(overlap_percents))}% ')

    plt.figure()
    plt.hist(music_percents, bins=10)  
    plt.ylabel('Number of Files')
    plt.xlabel('Percentage (%)')
    plt.title("Music Labels Percentage Distribution");
    plt.show()

    plt.figure()
    plt.hist(speech_percents, bins=10)  
    plt.ylabel('Number of Files')
    plt.xlabel('Percentage (%)')
    plt.title("Speech Labels Percentage Distribution");
    plt.show()

    plt.figure()
    plt.hist(overlap_percents, bins=10)  
    plt.ylabel('Number of Files')
    plt.xlabel('Percentage (%)')
    plt.title("Overlap Labels Percentage Distribution");
    plt.show()

statistic_calculation()