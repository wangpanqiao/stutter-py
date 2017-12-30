# -*- coding:utf-8 -*-  

from pydub import AudioSegment
import librosa
import random
import lrc_helper

CHUNK_SIZE = 10 # 10ms per chunk
f = open('wav.txt', 'w')
seg = open('seg.txt', 'w')

song = AudioSegment.from_wav("pndgmcsy.wav")
# song = AudioSegment.from_wav("frx.wav")
path = "./pndgmcsy.lrc"
songLrc = lrc_helper.extract_sentence(path)

maxVolume = song.max
number_of_frames_in_sound = song.frame_count()


# testsong = song[number_of_frames_in_sound/300:number_of_frames_in_sound/300*2]
# testsong.export("testsong.wav", format="wav")

# print ("max volume of this song is: " + str(maxVolume)) # 23640
# print ("number of frames in this song: " + str(number_of_frames_in_sound)) # 12996330

i = 0
num = 0
total = 0
average = 0
begin = 0
end = 0
last = 0

noise = 0
noiseCnt = 0
threshhold0 = 0
threshhold1 = 0
threshhold2 = 0

repeatMaxTime = 4

segments = []

for each in song:
    total = total + each.rms
    if (num >= 19):
        average = total / 20
        noise = noise + average
        noiseCnt = noiseCnt + 1
        num = 0
        total = 0
    num = num + 1

threshhold0 = noise / noiseCnt
threshhold1 = threshhold0 * 0.2
threshhold2 = threshhold0 * 1
threshhold3 = threshhold0 * 0.5

period = 800
maxPeriod = 2 * period

def getSegment(song, segments, period, maxPeriod):
    total = 0
    num = 0
    noise = 0
    noiseCnt = 0
    average = 0
    silence = True
    i = 0
    begin = 0
    end = 0

    for each in song:
        total = total + each.rms
        if (num >= 19):
            average = total / 20
            f.write(str(average) + " " + str(i) + "\n")
            if (average > threshhold2 and silence):
                silence = False
                begin = i
            if (not silence):
                if (average < threshhold1):
                    silence = True
                    end = i
                    seg.write(str(begin) + " ")
                    seg.write(str(end) + " ")
                    seg.write(str(end - begin) + "\n")
                    if (end - begin > period):
                        print(str(begin) + " " + str(end))
                        if (end - begin > maxPeriod):
                            begin = end - maxPeriod
                        segments.append((begin, end, int(3*(end-begin)/period)))
            last = average
            total = 0
            average = 0
            num = 0
        num = num + 1
        i = i + 1

getSegment(song, segments, period, maxPeriod)

# lrc segment
segments_lrc = []
for each in songLrc:
    # print(each)
    # print("$$$$$$$$$$$$$")
    words = each['words']
    sentence_start_time = each['start_time']
    sentence_end_time = each['duration'] + sentence_start_time
    if (words[len(words)-1]['time_duration'] > period):
        for seg in segments:
            if (abs(seg[1]-sentence_end_time)<2000):
                begin = sentence_end_time - words[len(words)-1]['time_duration']
                end = sentence_end_time
                segments_lrc.append((int(begin), int(end), int(2*(end-begin)/period)))
                print(segments_lrc)

             
    # for word in words:
    #     if (word['time_duration'] > 1000):
    #         print(word)
    #         begin = sentence_start_time + word['start_time']
    #         end = begin + word['time_duration']
    #         segments_lrc.append((int(begin), int(end), int(3*(end-begin)/period)))

# print(segments)

tail = 0
newsong = song[0]
for each in segments_lrc:
    print (str(each[0]) + " " + str(each[1]) + " " + str(each[2]))
    repeattime = repeatMaxTime if repeatMaxTime < each[2] else each[2]
    newsong = newsong + song[tail:each[0]]
    newsong = newsong + song[each[0]:each[1]].speedup(playback_speed=repeattime) * repeattime
    tail = each[1]
newsong = newsong + song[tail+1:]

newsong.export("newpndgmcsy2.wav", format="wav")
# newsong.export("newfrx.wav", format="wav")