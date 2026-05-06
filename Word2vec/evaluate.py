!python -m bilingual_embeddings.evaluate_cli --task lexicon \
    --predicted-lexicon "{W2V_DICT}" \
    --gold-lexicon      "{SEED_SCORED}" \
    --output            "{OUT}/reports/eval_word2vec.json"

with open(f"{OUT}/reports/eval_word2vec.json") as f:
    w2v_metrics = json.load(f)
print("Word2Vec metrics:", w2v_metrics)

pipe_w2v.visualize(f"{OUT}/tsne_word2vec.png")
from IPython.display import Image
Image(f"{OUT}/tsne_word2vec.png")
