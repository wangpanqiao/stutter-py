from audioFeature import AudioFeature
from pydub import AudioSegment
import matplotlib.pyplot as plt

# 242577
threshhold1 = 0.005
threshhold2 = 0.01

sentences = []
lastWords = []

def getSentence(energy, frameNum, secondsNum):
    isSilence = True
    framePerMs = frameNum / (secondsNum+0.0) / 1000
    for index, each in enumerate(energy):
        if (each > threshhold2 and isSilence):
            begin = index
            last = begin
            isSilence = False
        if (not isSilence):            
            if (each > threshhold1):
                last = index
            else:
                # 0.2s 
                if (index - last > 200*framePerMs):
                    isSilence = True
                    end = last
                    sentences.append((begin, end))
                    # print((begin * secondsNum / (frameNum + 0.0), end * secondsNum / (frameNum + 0.0)))

def isTremendousRise(seq, threshhold):
    if (seq[0] < seq[1] - threshhold and seq[1] < seq[2] - threshhold):
        return True
    else:
        return False

def getLastWordSeg(energy, frameNum, secondsNum, begin, end):
    sentence = energy[begin:end]
    framePerMs = frameNum / (secondsNum+0.0) / 1000
    for index, each in enumerate(sentence):
        # at least 0.5s
        reversedIndex = len(sentence) - int(200*framePerMs) - index
        if (reversedIndex < 0):
            return
        seq = sentence[reversedIndex:reversedIndex+3]
        if (isTremendousRise(seq, 0.008)):
            lastWords.append(( (end - index - 30) * secondsNum / (frameNum + 0.0), end * secondsNum / (frameNum + 0.0)))
            break

def main():
    aF = AudioFeature("../pndgmcsy.wav")
    energy = aF.energy

    frameNum = len(energy)
    secondsNum = len(aF.x) / 44100

    # pydub
    song = AudioSegment.from_wav("../pndgmcsy.wav")
    number_of_frames_in_sound = song.frame_count()

    segments = []
    isSilence = True
    begin = 0
    end = 0
    last = 0
    seg = open('seg.txt', 'w')

    tail = 0
    newsong = song[0]

    getSentence(energy, frameNum, secondsNum)

    for each in sentences:
        getLastWordSeg(energy, frameNum, secondsNum, each[0], each[1])

    lastSeg = (0, 0)
    for each in lastWords:
        begin = int(each[0] * 1000)
        end = int(each[1] * 1000)
        newsong = newsong + song[tail:begin]
        newsong = newsong + song[begin:end].speedup(playback_speed=3) * 3
        tail = end
    newsong = newsong + song[tail + 1:]
    newsong.export("newpndgmcsy.wav", format="wav")

    # plt.subplot(2,1,2); plt.plot(aF.energy); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()


main()
