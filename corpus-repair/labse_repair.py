!python examples/repair_corpus.py \
    --source        "{BHO_NORM}" \
    --target        "{HIN_NORM}" \
    --source-lang   bho \
    --target-lang   hin \
    --output-source "{BHO_REPAIRED}" \
    --output-target "{HIN_REPAIRED}" \
    --similarity-model LaBSE

print("Repair done.")
print("Bho repaired:", BHO_REPAIRED)
print("Hin repaired:", HIN_REPAIRED)
