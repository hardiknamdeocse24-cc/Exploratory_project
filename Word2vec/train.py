import sys
sys.path.insert(0, REPO)
from biembed import Config, EmbeddingPipeline

cfg_w2v = Config()
cfg_w2v.set("languages.source",          "bho")
cfg_w2v.set("languages.target",          "hin")
cfg_w2v.set("data.parallel_corpus_path", PARALLEL_TSV)
cfg_w2v.set("embedding.model_type",      "word2vec")
cfg_w2v.set("embedding.dimension",       100)
cfg_w2v.set("embedding.sg",              1)
cfg_w2v.set("embedding.window",          5)
cfg_w2v.set("embedding.min_count",       2)
cfg_w2v.set("mapping.method",            "orthogonal")
cfg_w2v.set("dictionary.top_k",          10)
cfg_w2v.set("dictionary.use_csls",       True)

pipe_w2v = EmbeddingPipeline(cfg_w2v)
res_w2v  = pipe_w2v.run()
W2V_DICT = f"{OUT}/dict_word2vec.json"
pipe_w2v.generate_dictionary(W2V_DICT)
print(f"Word2Vec dictionary: {len(res_w2v['dictionary'])} entries")
