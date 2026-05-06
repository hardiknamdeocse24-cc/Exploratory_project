!python -m bilingual_embeddings.evaluate_cli --task lexicon \
    --predicted-lexicon "{FT_DICT}" \
    --gold-lexicon      "{SEED_SCORED}" \
    --output            "{OUT}/reports/eval_fasttext.json"

with open(f"{OUT}/reports/eval_fasttext.json") as f:
    ft_metrics = json.load(f)
print("FastText metrics:", ft_metrics)

pipe_ft.visualize(f"{OUT}/tsne_fasttext.png")
from IPython.display import Image
Image(f"{OUT}/tsne_fasttext.png")
