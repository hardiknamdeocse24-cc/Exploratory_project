import pandas as pd

rows = [
    {
        "Model":        "Word2Vec (skip-gram)",
        "Dim":          100,
        "P@1":          round(w2v_metrics.get("precision@1",  0), 4),
        "P@5":          round(w2v_metrics.get("precision@5",  0), 4),
        "P@10":         round(w2v_metrics.get("precision@10", 0), 4),
        "MRR":          round(w2v_metrics.get("mrr",          0), 4),
        "Dict entries": len(res_w2v["dictionary"]),
    },
    {
        "Model":        "FastText (subword)",
        "Dim":          100,
        "P@1":          round(ft_metrics.get("precision@1",   0), 4),
        "P@5":          round(ft_metrics.get("precision@5",   0), 4),
        "P@10":         round(ft_metrics.get("precision@10",  0), 4),
        "MRR":          round(ft_metrics.get("mrr",           0), 4),
        "Dict entries": len(res_ft["dictionary"]),
    },
    {
        "Model":        "Transformer (MuRIL)",
        "Dim":          768,
        "P@1":          round(tfm_metrics.get("precision@1",  0), 4),
        "P@5":          round(tfm_metrics.get("precision@5",  0), 4),
        "P@10":         round(tfm_metrics.get("precision@10", 0), 4),
        "MRR":          round(tfm_metrics.get("mrr",          0), 4),
        "Dict entries": len(res_tfm["dictionary"]),
    },
]

df = pd.DataFrame(rows).set_index("Model")
print("\n===== EP10 Model Comparison =====\n")
print(df.to_string())

all_results = {"corpus_repair": repair_stats, "model_comparison": rows}
with open(f"{OUT}/reports/ep10_final_report.json", "w") as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)
print(f"\nSaved: {OUT}/reports/ep10_final_report.json")
