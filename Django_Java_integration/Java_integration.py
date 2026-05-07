from biembed.interop import JavaBridge

JAVA_EMB_PATH = f"{OUT}/java_embeddings.txt"

# Use FastText embeddings for Java export
bridge = JavaBridge(cfg_ft.config)

# Export embeddings in text format readable by Java
bridge.export_embeddings_to_java(
    res_ft["source_embeddings"],
    JAVA_EMB_PATH,
    format='text'
)

print("Embeddings exported for Java:", JAVA_EMB_PATH)

# Verify file
with open(JAVA_EMB_PATH) as f:
    lines = f.readlines()
print(f"Total entries exported: {len(lines)}")
print("Sample line:", lines[1].strip()[:80])
