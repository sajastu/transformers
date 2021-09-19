
#user_space_tr=$(python disk.py)

#! ln -sf $user_space_tr /home/code-base/user_space/
#
#for f in /home/code-base/user_space/tr*
#do
#  export SAVE_MODEL_DIR="${f}"
#done


export CUDA_VISIBLE_DEVICES=0,1
export MODEL=bart
export M_ID=bart-intro-arxiv-cnn
export DS_BASE_DIR=/disk1/sajad/datasets/sci/arxiv-dataset/single_files/intro_abstract

export SAVE_MODEL_DIR=/disk1/sajad/sci-trained-models/$MODEL/

echo "SAVE_MODEL_DIR is $SAVE_MODEL_DIR"
