# Stop the server
server.terminate()
print("Django server stopped")

# Final summary of all outputs
print("\n===== EP10 All Outputs =====")
outputs = {
    "Corpus repair stats":    repair_stats,
    "Parallel TSV":           PARALLEL_TSV,
    "Seed lexicon":           SEED_SCORED,
    "Word2Vec dict":          W2V_DICT,
    "FastText dict":          FT_DICT,
    "Transformer dict":       TFM_DICT,
    "W2V eval report":        f"{OUT}/reports/eval_word2vec.json",
    "FastText eval report":   f"{OUT}/reports/eval_fasttext.json",
    "Transformer eval report":f"{OUT}/reports/eval_transformer.json",
    "Final comparison":       f"{OUT}/reports/ep10_final_report.json",
    "t-SNE comparison plot":  f"{OUT}/ep10_tsne_comparison.png",
    "Django app":             DJANGO_APP,
    "Java embeddings (FT)":   JAVA_EMB_PATH,
}

for label, path in outputs.items():
    exists = os.path.exists(path) if isinstance(path, str) else True
    print(f"  {'OK' if exists else 'MISSING'} | {label}")

# Save final report with everything
with open(f"{OUT}/reports/ep10_final_report.json", "w") as f:
    json.dump({
        "corpus_repair":     repair_stats,
        "model_comparison":  rows,
        "django_app_path":   DJANGO_APP,
        "java_export_path":  JAVA_EMB_PATH,
    }, f, indent=2, ensure_ascii=False)

print("\nAll done! Full report saved.")
