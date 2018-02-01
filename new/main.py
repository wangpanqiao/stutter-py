from audioFeature import AudioFeature
from pydub import AudioSegment
import matplotlib.pyplot as plt

# 242577
threshhold1 = 0.002
threshhold2 = 0.01

sentences = []

def getSentence(energy):
    isSilence = True
    for index, each in enumerate(energy):
        if (each > threshhold2 and isSilence):
            begin = index
            last = begin
            isSilence = False
        if (not isSilence):            
            if (each > threshhold1):
                last = index
            else:
                if (index - last > 15):
                    isSilence = True
                    end = last
                    sentences.append((begin, end))
                    print((begin, end))



def main():
    aF = AudioFeature("../pndgmcsy.wav")
    energy = aF.energy
    spectralEntropy = aF.spectralEntropy
    frameNum = len(energy)
    secondsNum = len(aF.x) / 44100

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

    getSentence(energy)

    # for index, each in enumerate(energy):
    #     if (each > threshhold2 and isSilence):
    #         isSilence = False
    #         begin = index
    #     if (not isSilence):
    #         if (last * 1.5 < each):
    #             begin = index
    #         if (each < threshhold1):
    #             end = index
    #             isSilence = True
    #             segments.append(
    #                 (begin * secondsNum / (frameNum + 0.0), end * secondsNum / (frameNum + 0.0)))
    #     last = each

    # for index, each in enumerate(spectralEntropy):
    #     if (last * 1.5 < each):
    #         pitch = 

    #     last = each

    # for each in segments:
    #     seg.write(str(each[0]) + " " + str(each[1]))
    #     seg.write("\n")

    # lastSeg = (0, 0)
    # for each in segments:
    #     if (each[0] > lastSeg[1] + 1 and lastSeg[1] - lastSeg[0] > 0.7):
    #         print (str(lastSeg[0]) + " " + str(lastSeg[1]))
    #         begin = int(lastSeg[0] * 1000)
    #         end = int(lastSeg[1] * 1000)
    #         newsong = newsong + song[tail:begin]
    #         newsong = newsong + song[begin:end].speedup(playback_speed=3) * 3
    #         tail = end
    #     lastSeg = (each[0], each[1])
    # newsong = newsong + song[tail + 1:]
    # newsong.export("newpndgmcsy.wav", format="wav")

    # plt.subplot(2,1,2); plt.plot(aF.energy); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()


main()
