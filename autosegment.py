# -*- coding:utf-8 -*-  

from pydub import AudioSegment
import librosa
import random

CHUNK_SIZE = 10 # 10ms per chunk
f = open('wav.txt', 'w')
seg = open('seg.txt', 'w')

song = AudioSegment.from_wav("bjehp.wav")

maxVolume = song.max
number_of_frames_in_sound = song.frame_count()

# print ("max volume of this song is: " + str(maxVolume)) # 23640
# print ("number of frames in this song: " + str(number_of_frames_in_sound)) # 12996330

# num = 0
# for each in song:
#     num = num + 1

# print (num)

i = 0
num = 0
total = 0
average = 0
begin = 0
end = 0
last = 0
silence = True

segments = []

for each in song:
    total = total + each.rms
    if (num >= 19):
        average = total / 20
        f.write(str(average) + " " + str(i) + "\n")
        if (average > 150 and silence):
            silence = False
            begin = i
        if ((average - last) > 200 and not silence):
            begin = i
        if (average < 20 and not silence):
            silence = True
            end = i
            seg.write(str(begin) + " ")
            seg.write(str(end) + " ")
            seg.write(str(end - begin) + "\n")
            if (end - begin > 800):
                print(str(begin) + " " + str(end))
                segments.append((begin, end))
        last = average
        total = 0
        average = 0
    num = num + 1
    i = i + 1

tail = 0
newsong = song[0]
for each in segments:
    print(each)
    newsong = newsong + song[tail:each[0]]
    newsong = newsong + song[each[0]:each[1]].speedup(playback_speed=3) * 3
    tail = each[1]
newsong = newsong + song[tail+1:]
newsong.export("newbjehp.wav", format="wav")