from audioFeature import AudioFeature
from pydub import AudioSegment
import matplotlib.pyplot as plt

# 242577


def main():
    aF = AudioFeature("../bjehp.wav")
    energy = aF.energy
    spectralEntropy = aF.spectralEntropy
    zcr = aF.zcr
    spectralCentroid = aF.spectralCentroid
    spectralFlux = aF.spectralFlux
    frameNum = len(energy)
    secondsNum = len(aF.x) / 44100

    xlabels = []
    for index in range(len(energy)):
        xlabels.append(index*secondsNum/(frameNum+0.0))

    plt.subplot(2, 1, 1)
    plt.plot(xlabels, spectralFlux)
    plt.xlabel('Frame no')
    plt.ylabel('Spectral Flux')

    plt.subplot(2, 1, 2)
    plt.plot(xlabels, energy, 'r-o')
    plt.xlabel('Frame no')
    plt.ylabel('Energy')
    plt.show()

main()
