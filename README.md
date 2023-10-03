# KA-LLM

### Stage 2: Knowledge Retrieval

#### 2.1 Setup Entity Linking for SPARQL

For linking text to KG facts using pretrained models for now.

Download mGENRE entity linking files:

```
mkdir -p utils/retrieval/linking_data/genre
cd utils/retrieval/linking_data/genre
wget https://dl.fbaipublicfiles.com/GENRE/lang_title2wikidataID-normalized_with_redirect.pkl
wget https://dl.fbaipublicfiles.com/GENRE/titles_lang_all105_marisa_trie_with_redirect.pkl
cd ../..
```

Preprocess entity information:

```
python linking.py process_titles
```

#### 2.2 SERPAPI_KEY
Create an account and get the API key for google retrieval (https://serpapi.com).

```
SERPAPI_KEY=YOUR_KEY
```