import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import librosa

NOTE_NAMES = ["C", "C#", "D", "D#", "E" "F" "F#" "G" "G#" "A" "A#" "B"]

MAJOR_SCALE = {0, 2, 4, 5, 7 ,9, 11}
MINOR_SCALE = {0, 2, 3 ,5, 7, 8, 10}

def hz_to_pitch_class(f_hz: float) -> int:
    if f_hz <=0:
        return None
    
    midi = 69 + 12 * np.log2(f_hz / 440.0)
    midi_rounded = int(np.round(midi))

    return midi_rounded % 12