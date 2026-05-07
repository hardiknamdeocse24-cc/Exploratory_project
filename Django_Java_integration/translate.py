import requests

# Test single word translation
r = requests.get(
    "http://localhost:8000/api/embeddings/translate/",
    params={"word": "घर", "top_k": 5},
    timeout=5
)
print("Status:", r.status_code)
print("Response:", r.json())
