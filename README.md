# Chain-of-Knowledge

### 1. Requirements
#### 1.1 OPENAI_API_KEY
Create an account and get the API key for OpenAI (https://openai.com).

```
OPENAI_API_KEY=YOUR_KEY
```
#### 1.2 SERPAPI_KEY
Create an account and get the API key for google retrieval (https://serpapi.com).

```
SERPAPI_KEY=YOUR_KEY
```

#### 1.3 Install requirements
```
conda env create -f requirements.yaml
```

#### 1.4 Setup Entity Linking for SPARQL

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

### 2. Instruction-tuning of adaptive query generator (AQG)
```
python sft_trainer.py \
    --model_name $BASE_MODEL \
    --dataset_name $DATASET_NAME \
    --load_in_8bit \
    --use_peft \
    --batch_size 32 \
    --gradient_accumulation_steps 2 \
    --output_dir $OUTPUT_DIR \
    --num_train_epochs 3 \
    --push_to_hub True\
    --hub_model_id $HUB_MODEL_ID \
```

### 3. Inference chain-of-knowledge (CoK)
```
python run.py \
    --model gpt-3.5-turbo-0613 \
    --dataset $DATASET_NAME \
    --output $OUTPUT_DIR \
    --step True \
```

### Citation
```
@inproceedings{
    li2024cok,
    title={Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources},
    author={Xingxuan Li and Ruochen Zhao and Yew Ken Chia and Bosheng Ding and Shafiq Joty and Soujanya Poria and Lidong Bing},
    booktitle={International Conference on Learning Representations},
    year={2024},
    url={https://openreview.net/forum?id=cPgh4gWZlz}
}
```
