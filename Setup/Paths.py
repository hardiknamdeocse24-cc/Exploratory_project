import os, json 
BASE = "/content/drive/MyDrive/nlp_lab" 
DATA = f"{BASE}/data/raw/PART-2" 
OUT = f"{BASE}/ep10_outputs" 
os.makedirs(OUT, exist_ok=True) 
os.makedirs(f"{OUT}/reports", exist_ok=True) 
