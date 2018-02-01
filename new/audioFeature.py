from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from pyAudioAnalysis import audioSegmentation as aS
# import matplotlib.pyplot as plt

class AudioFeature:
    def __init__(self, song):
        [Fs, x] = audioBasicIO.readAudioFile(song)
        F = audioFeatureExtraction.stFeatureExtraction(
            x, Fs, 0.10 * Fs, 0.025 * Fs)

        self.energy = F[1, :]
        self.spectralEntropy = F[5, :]
        self.spectralCentroid = F[3, :]
        self.spectralFlux = F[6, :]
        self.zcr = F[0, :]
        self.Fs = Fs
        self.x = x
        self.song = song

# print(Fs)

# for tmp in x:
#   print(tmp)
# print(len(x)/44100)

# F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
# plt.subplot(2,1,1); plt.plot(F[4,:]); plt.xlabel('Frame no'); plt.ylabel('Spectral Entropy');
# plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()

# [flagsInd, classesAll, acc, CM] = aS.mtFileClassification("data/scottish.wav", "data/svmSM", "svm", True, 'data/scottish.segments')
