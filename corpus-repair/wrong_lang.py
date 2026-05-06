!python examples/corpus_cleaning.py \
    --source      "{BHO_NORM}" \
    --source-lang bho \
    --target      "{HIN_NORM}" \
    --target-lang hin \
    --output-dir  "{OUT}/langid_report"

print("Lang ID report saved to:", f"{OUT}/langid_report")
