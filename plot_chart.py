import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from vesting_csv import emissionHistory, start_monthTotal
plt.style.use("seaborn")

private_sale,marketing,team,public_sale,community,ecosystem,chain = [],[],[],[],[],[],[]
for i in emissionHistory:
    private_sale.append(i[0])
    marketing.append(i[1])
    team.append(i[2])
    public_sale.append(i[3])
    community.append(i[4])
    ecosystem.append(i[5])
    chain.append(i[6])

month = [i for i in range(start_monthTotal)]

colors = sns.color_palette("RdBu", 7)
labels=["private_sale", "marketing", "team", "public_sale", "community", "ecosystem", "chain"]
plt.stackplot(month, private_sale, marketing, team, public_sale, community, ecosystem, chain, labels=labels, colors=colors)

plt.grid(visible=None)
plt.legend(loc = "upper center", bbox_to_anchor=(1.1, 0.8), shadow=True, ncol=1)
plt.title('Vesting Schedule')
plt.ylabel('Emission Percentage (%)')
plt.xticks(np.arange(0,start_monthTotal,step=10), rotation=40)

plt.tight_layout()
plt.show()