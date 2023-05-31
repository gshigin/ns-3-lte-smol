# usage: python3 uldl.py

import pandas as pd

# parse UL
ulrlc = pd.read_csv("UlRlcStats.txt", sep = "\t", index_col=False)

ulrlc_1 = ulrlc[ulrlc['IMSI'] == 1]
UL_1 = ulrlc_1['RxBytes'].sum()/1000/(ulrlc_1['end'].max()-ulrlc_1['% start'].min())

ulrlc_2 = ulrlc[ulrlc['IMSI'] == 2]
UL_2 = ulrlc_2['RxBytes'].sum()/1000/(ulrlc_2['end'].max()-ulrlc_2['% start'].min())

# parse DL
dlrlc = pd.read_csv("DlRlcStats.txt", sep = "\t", index_col=False)

dlrlc_1 = dlrlc[dlrlc['IMSI'] == 1]
DL_1 = dlrlc_1['RxBytes'].sum()/1000/(dlrlc_1['end'].max()-dlrlc_1['% start'].min())

dlrlc_2 = dlrlc[dlrlc['IMSI'] == 2]
DL_2 = dlrlc_2['RxBytes'].sum()/1000/(dlrlc_2['end'].max()-dlrlc_2['% start'].min())

print(f'Abonent 1:\n\tUL Throughput: {UL_1:10.4f} kbps\n\tDL Throughput: {DL_1:10.4f} kbps\n')
print(f'Abonent 2:\n\tUL Throughput: {UL_2:10.4f} kbps\n\tDL Throughput: {DL_2:10.4f} kbps\n')