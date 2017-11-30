# -*- coding:utf-8 -*-  

from pydub import AudioSegment
import librosa
import random

# song = AudioSegment.from_wav("再别康桥slow_high.wav")

# ten_seconds = 10 * 1000
# zero = song[17000:17500]

# tmp = song[3001:4000]
# tmp = tmp + zero * 1
# do_it_over = tmp * 3

# out = song[0:3000] + do_it_over + song[3001:]

# tmp = song[13600:15000]
# tmp = tmp + zero * random.randint(3, 5)
# do_it_over = tmp * 5

# out = out[:19000] + do_it_over + out[19001:24000]


# out.export("stutter.wav", format="wav")


# # 1. Get the file path to the included audio example
# filepath = './'
# filename =filepath+'daoxiang.wav'
# # 2. Load the audio as a waveform `y`
# #    Store the sampling rate as `sr`
# y, sr = librosa.load(filename,sr=None)
# y_slow = librosa.effects.time_stretch(y, 5)
# y_slow_high = librosa.effects.pitch_shift(y_slow, sr, n_steps=1)

# librosa.output.write_wav('stutter_new.wav', y_slow, sr)

song = AudioSegment.from_wav("dog_1.wav")
newsong = song.speedup(playback_speed=0.5)
newsong.export("dog_slow.wav", format="wav")