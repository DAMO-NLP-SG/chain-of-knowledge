export CUDA_VISIBLE_DEVICES=0
BASE_MODEL="meta-llama/Llama-2-7b-hf"
DATASET_NAME="veggiebird/sparql-contrastive"
OUTPUT_DIR="model/llama-2-7b-8bit-sparql-contrastive"
HUB_MODEL_ID="YOUR_HUB_MODEL_ID"

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