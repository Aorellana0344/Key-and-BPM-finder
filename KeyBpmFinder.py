import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import librosa

NOTE_NAMES = ["C", "C#", "D", "D#", "E" "F" "F#" "G" "G#" "A" "A#" "B"]

MAJOR_SCALE = {0, 2, 4, 5, 7 ,9, 11}
MINOR_SCALE = {0, 2, 3 ,5, 7, 8, 10}

def hz_to_pitch_class(f_hz: float) -> int:
    if f_hz <=0:    #fequencies cannot be negative nor 0
        return None
    
    midi = 69 + 12 * np.log2(f_hz / 440.0)
    midi_rounded = int(np.round(midi))

    return midi_rounded % 12

def estimate_key_by_peaks(path: str, top_k_peaks: int = 3):
    y, sr = librosa.load(path, mono=True)

    S = np.abs(librosa.stft(y, n_fft=4096, hop_length=1024))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=4096)

    #here, we ignore low frequencies that produce rumble, and ultra high frequences as well
    low_hz, high_hz = 50.0, 5000.0
    band_mask = (freqs >= low_hz) & (freqs <= high_hz)
    freqs_band = freqs[band_mask]
    S_band = S[band_mask, :]
    