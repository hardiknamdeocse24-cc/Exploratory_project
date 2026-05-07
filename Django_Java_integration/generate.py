from biembed.interop import DjangoAPI

DJANGO_APP = f"{OUT}/django_bho_hin_app"

# Use config from any of the three models — using FastText here as default
api = DjangoAPI(cfg_ft.config)

# Generate Django app with REST API scaffold
api.generate_django_app(DJANGO_APP)

# Export trained embeddings into the app's data folder
api.export_embeddings(
    res_ft["source_embeddings"],
    res_ft["target_embeddings"],
    f"{DJANGO_APP}/data"
)

print("Django app generated at:", DJANGO_APP)
print("Files created:", os.listdir(DJANGO_APP))
