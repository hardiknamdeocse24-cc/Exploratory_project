# Build parallel TSV
with open(BHO_REPAIRED) as b, open(HIN_REPAIRED) as h, \
     open(PARALLEL_TSV, "w") as out:
    out.write("bho\thin\n")
    for bl, hl in zip(b, h):
        out.write(f"{bl.rstrip()}\t{hl.rstrip()}\n")
print(f"Parallel TSV saved: {PARALLEL_TSV}")

# Extract seed lexicon
!python -m bilingual_embeddings.lexicon_cli extract \
    --source      "{BHO_REPAIRED}" \
    --target      "{HIN_REPAIRED}" \
    --source-lang bho \
    --target-lang hin \
    --output      "{OUT}/bho-hin.seed.tsv"

# Score seed lexicon
!python -m bilingual_embeddings.lexicon_cli score \
    --input       "{OUT}/bho-hin.seed.tsv" \
    --output      "{SEED_SCORED}" \
    --edit-weight 0.3

print(f"Seed lexicon saved: {SEED_SCORED}")
