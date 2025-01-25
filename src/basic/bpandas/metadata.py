
import pandas as pd

from python.runfiles import runfiles

r = runfiles.Create()

# print(r.Rlocation("ai_prtc/src/basic/bpandas/annual-enterprise-survey-2023-financial-year-provisional.csv"))

data = pd.read_csv(r.Rlocation("ai_prtc/src/basic/bpandas/annual-enterprise-survey-2023-financial-year-provisional.csv"))

print(data[:10])
