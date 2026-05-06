orig = count(BHO_NORM)
rep  = count(BHO_REPAIRED)
removed  = orig - rep
retained = round(rep / orig * 100, 2)

print("=" * 40)
print(f"  Original lines   : {orig}")
print(f"  Repaired lines   : {rep}")
print(f"  Lines removed    : {removed}")
print(f"  Retention rate   : {retained}%")
print("=" * 40)

repair_stats = {
    "original_lines": orig,
    "repaired_lines": rep,
    "lines_removed" : removed,
    "retention_pct" : retained
}
