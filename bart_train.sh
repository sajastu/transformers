#!/usr/bin/env bash

# debug
#CUDA_VISIBLE_DEVICES=7 python examples/pytorch/summarization/run_summarization.py \

python -m torch.distributed.launch --nproc_per_node=2 examples/pytorch/summarization/run_summarization.py \
    --model_name_or_path facebook/bart-large-cnn \
    --do_train \
    --do_eval \
    --do_predict \
    --output_dir $SAVE_MODEL_DIR/saved_models/$MODEL/$M_ID \
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=1  \
    --learning_rate 3e-5 \
    --weight_decay 0.01 \
    --adam_beta2 0.98 \
    --num_train_epochs 5 \
    --overwrite_output_dir \
    --evaluation_strategy steps  --eval_steps 100000 --save_steps 10000 --warmup_steps 20000 --logging_steps 100 \
    --text_column intro \
    --summary_column summary \
    --train_file $DS_BASE_DIR/train.json \
    --validation_file $DS_BASE_DIR/val.json \
    --test_file $DS_BASE_DIR/val.json \
    --predict_with_generate
#    --resume_from_checkpoint $SAVE_MODEL_DIR/saved_models/$MODEL/$M_ID/checkpoint-60000/
#    --do_train \
#    --do_eval \


