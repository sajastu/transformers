
#    --model_name_or_path /disk1/sajad/saved_models/bart-tldr9/checkpoint-880000/ \
#python3 -m torch.distributed.launch --nproc_per_node=2 examples/pytorch/summarization/run_summarization.py \
CUDA_VISIBLE_DEVICES=0 python3 examples/pytorch/summarization/run_summarization.py \
    --model_name_or_path /disk1/sajad/saved_models/bart-tldrQ/\
    --do_predict \
    --output_dir /disk1/sajad/saved_models/bart-tldrQ/\
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=10 \
    --overwrite_output_dir \
    --evaluation_strategy steps  --eval_steps 20000 --save_steps 20000 --warmup_steps 32000 --logging_steps 200 \
    --text_column document \
    --summary_column summary \
    --train_file /disk1/sajad/datasets/reddit/tldr-9+/test.json  \
    --validation_file3 /disk1/sajad/datasets/reddit/tldr-9+/test.json  \
    --test_file /home/sajad/test-sample.json \
    --predict_with_generate \
#    --resume_from_checkpoint /disk1/sajad/saved_models/bart-tldr9/checkpoint-880000