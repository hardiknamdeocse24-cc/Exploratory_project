import os, json

BASE   = "/content/drive/MyDrive/nlp_lab"
DATA   = f"{BASE}/data/raw/PART-2"
OUT    = f"{BASE}/ep10_outputs"
os.makedirs(OUT, exist_ok=True)
os.makedirs(f"{OUT}/reports", exist_ok=True)

BHO_RAW      = f"{DATA}/bho-hin.bho.txt"
HIN_RAW      = f"{DATA}/bho-hin.hin.txt"
BHO_NORM     = f"{OUT}/bho.norm.txt"
HIN_NORM     = f"{OUT}/hin.norm.txt"
BHO_REPAIRED = f"{OUT}/bho.repaired.txt"
HIN_REPAIRED = f"{OUT}/hin.repaired.txt"
PARALLEL_TSV = f"{OUT}/bho-hin.parallel.tsv"
SEED_SCORED  = f"{OUT}/bho-hin.scored.tsv"

for label, path in [("Bho", BHO_RAW), ("Hin", HIN_RAW)]:
    print(f"{'OK' if os.path.exists(path) else 'MISSING'} [{label}] {path}")
