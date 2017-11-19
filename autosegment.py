# -*- coding:utf-8 -*-  

from pydub import AudioSegment
import librosa
import random

song = AudioSegment.from_wav("bjehp.wav")

print (song.max)
print (song.frame_count(ms=200))
number_of_frames_in_sound = song.frame_count()

print (number_of_frames_in_sound)
# for each in song:
#     print(each.rms)

# num = 0
# total = 0
# average = 0
# for each in song:
#     total = total + each.rms
#     if (num >= 63):
#         average = total / 64
#         print (average)
#         total = 0
#         average = 0
#     num = num + 1
     
    

