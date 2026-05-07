# Export all three models so Java/Bhaashik can use any of them

models = [
    ("word2vec",    res_w2v, cfg_w2v),
    ("fasttext",    res_ft,  cfg_ft),
    ("transformer", res_tfm, cfg_tfm),
]

for name, res, cfg in models:
    path = f"{OUT}/java_{name}_embeddings.txt"
    b = JavaBridge(cfg.config)
    b.export_embeddings_to_java(
        res["source_embeddings"],
        path,
        format='text'
    )
    print(f"Exported {name} -> {path}")
