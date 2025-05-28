import numpy as np
import librosa

def dft(n, scale=None):
    """
    Modify from scipy.linalg.dft implementation of SciPy.
    """
    omegas = np.exp(-2j * np.pi * np.arange(n) / n).reshape(-1, 1)
    m = omegas ** np.arange(n)
    if scale == 'sqrtn':
        m /= math.sqrt(n)
    elif scale == 'n':
        m /= n
    return m

def adfa_arb(n, n_arb):
    return aa_arb(n, n_arb))

def aa_arb(n, n_arb):
    """
    n_arb is the lenght of the signal you want to analyze.
    """
    omegas = np.exp(-1j * np.pi * np.arange(n) / (n - 1)).reshape(-1, 1)
    m = omegas ** np.arange(n_arb)
    return m

def mdfa_arb(n, fs, n_arb):
    return ma_arb(n, fs, n_arb)

def ma_arb(n, fs, n_arb):
    """
    n_arb is the lenght of the signal you want to analyze.
    """
    mel_frequencies=librosa.mel_frequencies(n_mels=n, fmin=0.0, fmax=fs/2, htk=False)
    omegas = np.exp(-1j * np.pi * mel_frequencies / (fs/2)).reshape(-1, 1)
    m = omegas ** np.arange(n_arb)
    return m

def cqfa_arb(n, base, bins, n_arb):
    return cqa_arb(n, base, bins, n_arb)

def cqa_arb(n, base, bins, n_arb):
    """
    n_arb is the lenght of the signal you want to analyze.
    When base=2, bins means the number of frequency components per octave.
    """
    omegas = np.exp(-1j * np.pi * pow(base, -np.arange(n)/bins)[::-1]).reshape(-1, 1)
    m = omegas ** np.arange(n_arb)
    return m
