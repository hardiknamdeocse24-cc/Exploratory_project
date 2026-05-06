!python -m bilingual_embeddings.evaluate_cli --task lexicon \
    --predicted-lexicon "{TFM_DICT}" \
    --gold-lexicon      "{SEED_SCORED}" \
    --output            "{OUT}/reports/eval_transformer.json"

with open(f"{OUT}/reports/eval_transformer.json") as f:
    tfm_metrics = json.load(f)
print("Transformer metrics:", tfm_metrics)

pipe_tfm.visualize(f"{OUT}/tsne_transformer.png")
from IPython.display import Image
Image(f"{OUT}/tsne_transformer.png")
