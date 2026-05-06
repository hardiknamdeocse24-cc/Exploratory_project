!python -m bilingual_embeddings.indic_normalize_cli \
    --language bho --input "{BHO_RAW}" --output "{BHO_NORM}"

!python -m bilingual_embeddings.indic_normalize_cli \
    --language hin --input "{HIN_RAW}" --output "{HIN_NORM}"

def count(p): return sum(1 for _ in open(p))
print(f"bho normalized: {count(BHO_NORM)} lines")
print(f"hin normalized: {count(HIN_NORM)} lines")
