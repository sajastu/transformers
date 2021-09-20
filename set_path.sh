
#user_space_tr=$(python disk.py)

#! ln -sf $user_space_tr /home/code-base/user_space/
#
#for f in /home/code-base/user_space/tr*
#do
#  export SAVE_MODEL_DIR="${f}"
#done


#export CUDA_VISIBLE_DEVICES=0,1
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export MODEL=bart
export M_ID=bart-intro-arxiv-cnn
export DS_BASE_DIR=/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/saved_models/bart/arx-test/dataset

export SAVE_MODEL_DIR=/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/saved_models/bart/arx-test/

echo "SAVE_MODEL_DIR is $SAVE_MODEL_DIR"
