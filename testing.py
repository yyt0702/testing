import requests
import pandas as pd  

url = "https://beta.neutrino.at/api/explorer"
total_issue = url + "/get_total_issued"
circulating_supply = url + "/get_circulating_supply"
backing_ratio = url + '/get_br'
deficit = url + '/get_deficit'


cs = requests.get(circulating_supply)
ts = requests.get(total_issue)
br = requests.get(backing_ratio)
df = requests.get(deficit)

print("circulating supply: " , cs.json())
print("total supply: " , ts.json())
print("backing ratio: " , br.json())
print("deficit: ", df.json())





url = "https://api.vires.finance/state"
res = requests.get(url).json() 
df = pd.DataFrame(res)
df.to_csv("vires.csv")
