import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
plots = [
    (f"{OUT}/tsne_word2vec.png",    "Word2Vec (skip-gram)"),
    (f"{OUT}/tsne_fasttext.png",    "FastText (subword)"),
    (f"{OUT}/tsne_transformer.png", "Transformer (MuRIL)"),
]
for ax, (path, title) in zip(axes, plots):
    img = mpimg.imread(path)
    ax.imshow(img)
    ax.set_title(title, fontsize=12, pad=8)
    ax.axis("off")

plt.suptitle("EP10 — Bilingual Embedding Spaces (bho-hin)", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(f"{OUT}/ep10_tsne_comparison.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved:", f"{OUT}/ep10_tsne_comparison.png")
