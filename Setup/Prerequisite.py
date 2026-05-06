from google.colab import drive
drive.mount('/content/drive')

REPO = "/content/drive/MyDrive/nlp_lab/BilingualEmbeddings/BilingualEmbeddings-main"

%cd {REPO}
!pip install -e ".[corpus-repair,indic-align,transformers]" -q
!pip install pandas tabulate -q
print("Setup complete")
