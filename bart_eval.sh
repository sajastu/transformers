
#    --model_name_or_path /disk1/sajad/saved_models/bart-tldr9/checkpoint-880000/ \
#CUDA_VISIBLE_DEVICES=0 python3 examples/pytorch/summarization/run_summarization.py \

#for (( step=10000; step<=10000; step+=10000 )); do
#    python -m torch.distributed.launch --nproc_per_node=8 examples/pytorch/summarization/run_summarization.py \
#          --model_name_or_path $SAVE_MODEL_DIR/checkpoint-$step \
#          --do_predict \
#          --output_dir $SAVE_MODEL_DIR/checkpoint-$step \
#          --per_device_train_batch_size=1 \
#          --per_device_eval_batch_size=15 \
#          --overwrite_output_dir \
#          --evaluation_strategy steps  --eval_steps 20000 --save_steps 20000 --warmup_steps 32000 --logging_steps 200 \
#          --text_column intro \
#          --summary_column summary \
#          --train_file $DS_BASE_DIR/val.json  \
#          --validation_file $DS_BASE_DIR/val.json  \
#          --test_file $DS_BASE_DIR/val.json \
#          --predict_with_generate
#done

##################################################

python -m torch.distributed.launch --nproc_per_node=8 examples/pytorch/summarization/run_summarization.py \
        --model_name_or_path /disk1/sajad/sci-trained-models/bart/saved_models/bart/bart-intro-arxivL-cnn/checkpoint-3000 \
        --do_predict \
        --output_dir /disk1/sajad/sci-trained-models/bart/saved_models/bart/bart-intro-arxivL-cnn/checkpoint-3000 \
        --per_device_train_batch_size=1 \
        --per_device_eval_batch_size=15 \
        --overwrite_output_dir \
        --evaluation_strategy steps  --eval_steps 20000 --save_steps 20000 --warmup_steps 32000 --logging_steps 200 \
        --text_column intro \
        --summary_column summary \
        --train_file $DS_BASE_DIR/test.json  \
        --validation_file $DS_BASE_DIR/test.json  \
        --test_file $DS_BASE_DIR/test.json \
        --predict_with_generate
