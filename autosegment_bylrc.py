# -*- coding:utf-8 -*-  

from pydub import AudioSegment
import librosa
import random
import lrc_helper

CHUNK_SIZE = 10 # 10ms per chunk

song = AudioSegment.from_wav("pndgmcsy.wav")
# song = AudioSegment.from_wav("bjehp.wav")
# song = AudioSegment.from_wav("frx.wav")

repeatMaxTime = 6

# print ("max volume of this song is: " + str(maxVolume)) # 23640
# print ("number of frames in this song: " + str(number_of_frames_in_sound)) # 12996330


segments = []
period = 800

path = "./pndgmcsy.lrc"
songLrc = lrc_helper.extract_sentence(path)
begin = 0
end = 0

print(song)

for each in songLrc:
    # print(each)
    # print("$$$$$$$$$$$$$")
    words = each['words']
    sentence_start_time = each['start_time']
    for word in words:
        if (word['time_duration'] > 1000):
            print(word)
            begin = sentence_start_time + word['start_time']
            end = begin + word['time_duration']
            segments.append((int(begin), int(end), int(3*(end-begin)/period)))


tail = 0
newsong = song[0]
for each in segments:
    print (str(each[0]) + " " + str(each[1]) + " " + str(each[2]))
    repeattime = repeatMaxTime if repeatMaxTime < each[2] else each[2]
    newsong = newsong + song[tail:each[0]]
    newsong = newsong + song[each[0]:each[1]].speedup(playback_speed=repeattime) * repeattime
    tail = each[1]
newsong = newsong + song[tail+1:]

newsong.export("newpndgmcsy.wav", format="wav")
# newsong.export("newfrx.wav", format="wav")