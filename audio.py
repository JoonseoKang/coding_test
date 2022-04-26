audio = './sample.wav'
y, sr = librosa.load(audio)

import librosa
def pitch(data, sampling_rate, pitch_factor):
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

import numpy as np

def whitenoise(data, noise_factor):
    noise = np.random.randn(len(data))
    augmented_data = data + noise_factor * noise
    # Cast back to same data type
    augmented_data = augmented_data.astype(type(data[0]))
    return augmented_data

a = pitch(y, sr, 1.1)
a

b = whitenoise(y, 0.05)
noise
librosa.output.write_wav('pitch.wav', a, sr)

librosa.output.write_wav('./aa.wav', a, sr)

import soundfile as sf
sf.write('./pitch.wav', a, sr)
sf.write('./whitenoise.wav', b, sr)