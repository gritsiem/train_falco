cd /projects/$USER
module load anaconda
conda install --yes --file requirements.txt
python3 /home/$USER/train_falco/load_data.py

# Specify the path for the new folder
folder_path = "./valid"

# Create the folder
os.mkdir(folder_path)