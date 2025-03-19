import pandas as pd

folders = ["correlation", "GainRatio", "InfoGain", "nonweka", "CFS"]
files = ["train", "test", "validation"]

def replaceVal(x):
    return "NO DAMAGE" if x == "'NO DAMAGE'" else x

for folder in folders:
    for file in files:
        df = pd.read_csv(folder+"/"+file+".csv")
        df["'Vehicle Damage Extent'"] = df["'Vehicle Damage Extent'"].apply(replaceVal)
        df.to_csv(folder+"/"+file+"_ND.csv", index=False)
        print(f"{folder}/{file} is done")