import pandas as pd
from src.aiguard.drift import _psi, psi_band
from src.aiguard.governance import create_alerts

def test_identical_distribution_has_low_psi():
    x=pd.Series([1,2,3,4,5,6,7,8,9,10])
    assert _psi(x,x) < 0.01

def test_psi_bands():
    assert psi_band(0.05) == "Low"
    assert psi_band(0.15) == "Moderate"
    assert psi_band(0.30) == "High"

def test_quality_failure_creates_alert():
    alerts=create_alerts({},None,{"passed":False})
    assert any(a["type"]=="Data quality" for a in alerts)
