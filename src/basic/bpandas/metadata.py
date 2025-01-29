
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from python.runfiles import runfiles

r = runfiles.Create()

# print(r.Rlocation("ai_prtc/src/basic/bpandas/annual-enterprise-survey-2023-financial-year-provisional.csv"))

data = pd.read_csv(r.Rlocation("ai_prtc/src/basic/bpandas/annual-enterprise-survey-2023-financial-year-provisional.csv"))

# print(data[:10])

data[2:6].style.set_properties(subset=["Variable_category"], **{"width": "400px", "text-aligh": "left"})

# print(data[2:6])

# print(data.column_name[4])

sm = sns.FacetGrid(data[:50], col="Variable_category", col_wrap=5, aspect=2, margin_titles=True)

sm.map(plt.plot, "Year", "Value")

sm.set_titles("{col_name}", size=22).set_ylabels(size=20).set_yticklabels(size=15).set_xlabels(size=20).set_xticklabels(size=12)
