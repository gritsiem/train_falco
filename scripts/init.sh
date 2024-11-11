#!/bin/bash

#SBATCH --gres=gpu
#SBATCH --partition=aa100
#SBATCH --job-name=train-job
#SBATCH --output=train-job.%j.out
#SBATCH --time=01:00:00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ghritachi.mahajani@colorado.edu

codedir=/home/$USER/train_falco
cd /projects/$USER
module load anaconda
conda activate yolo

# if { conda env list | grep ".yolo."; } >dev/null 2>&1:
# then
#     conda activate yolo
# else 
#     conda env create yolo
#     conda activate yolo
# fi
# need python<=3.12
# pip install -r $codedir/requirementxt

# echo "Enter yolo model to train"
# read model
# python "../../$codedir/load_data.py" $model

cp -r /projects/$USER/Heridal-2 $SLURM_SCRATCH # takes a few
# next time use time utility 5m:15s

time python "$codedir/yolo.py"


