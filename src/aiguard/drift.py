import numpy as np
import pandas as pd

def _psi(expected, actual, bins=10):
    expected = pd.Series(expected).dropna().astype(float)
    actual = pd.Series(actual).dropna().astype(float)
    if expected.empty or actual.empty:
        return None
    edges = np.unique(np.quantile(expected, np.linspace(0, 1, bins + 1)))
    if len(edges) < 3:
        lo, hi = float(expected.min()), float(expected.max())
        if lo == hi:
            lo -= 0.5; hi += 0.5
        edges = np.linspace(lo, hi, bins + 1)
    edges[0] = -np.inf
    edges[-1] = np.inf
    e = np.histogram(expected, bins=edges)[0] / len(expected)
    a = np.histogram(actual, bins=edges)[0] / len(actual)
    eps = 1e-6
    e = np.clip(e, eps, None); a = np.clip(a, eps, None)
    return float(np.sum((a - e) * np.log(a / e)))

def psi_report(reference, current, columns):
    return {col: _psi(reference[col], current[col]) for col in columns}

def psi_band(value):
    if value is None: return "Unavailable"
    if value >= 0.25: return "High"
    if value >= 0.10: return "Moderate"
    return "Low"
