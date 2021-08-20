
user_space_tr=$(python disk.py)

! ln -sf $user_space_tr /home/code-base/user_space/

for f in /home/code-base/user_space/tr*
do
  export SAVE_MODEL_DIR="${f}"
done

export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export MODEL=bart
export M_ID=reddit-large-tldrQ
export DS_BASE_DIR=/home/code-base/user_space/trainman-k8s-storage-c91414be-d3d1-431d-a2c8-1d040368c6e8/tldrQ/


echo "SAVE_MODEL_DIR is $SAVE_MODEL_DIR"
