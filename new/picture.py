from audioFeature import AudioFeature
from pydub import AudioSegment
import matplotlib.pyplot as plt

# 242577


def main():
    aF = AudioFeature("../bjehp.wav")
    energy = aF.energy
    spectralEntropy = aF.spectralEntropy
    zcr = aF.zcr
    frameNum = len(energy)
    secondsNum = len(aF.x) / 44100

    plt.subplot(2, 1, 1)
    plt.plot(zcr)
    plt.xlabel('Frame no')
    plt.ylabel('Spectral Entropy')

    plt.subplot(2, 1, 2)
    plt.plot(aF.energy)
    plt.xlabel('Frame no')
    plt.ylabel('Energy')
    plt.show()

main()
