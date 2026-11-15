from pathlib import Path
import numpy as np
import pandas as pd

def make_batch(n=1800, seed=42, shifted=False):
    rng=np.random.default_rng(seed)
    income=rng.lognormal(10.6 + (0.10 if shifted else 0), .55, n)
    age=rng.integers(30, 2500, n)
    count=rng.poisson(12 + (3 if shifted else 0), n)
    avg=rng.lognormal(4.0 + (.12 if shifted else 0), .55, n)
    util=np.clip(rng.beta(2.2 + (.5 if shifted else 0), 4.5, n),0,1)
    tickets=rng.poisson(1.0 + (.3 if shifted else 0), n)
    z=-2.2 + .9*util + .15*tickets - .00001*income + .018*count
    prob=1/(1+np.exp(-z))
    y=rng.binomial(1,prob)
    return pd.DataFrame({"income":income.round(2),"account_age_days":age,
      "transaction_count":count,"avg_transaction_value":avg.round(2),
      "utilization":util.round(3),"support_tickets":tickets,"target":y})

if __name__=="__main__":
    Path("data/sample").mkdir(parents=True,exist_ok=True)
    make_batch(seed=42,shifted=False).to_csv("data/sample/reference_data.csv",index=False)
    make_batch(seed=99,shifted=True).to_csv("data/sample/current_data.csv",index=False)
    print("Generated reference and current synthetic batches.")
