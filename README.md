# CURC training pipeline for Falco

This repository is intended to be used to train a vision model for FALCO on CURC infrastructure using Heridal dataset for now.  

1. create a curc account (you need PUTTY software to be able to login)
2. After logging in, create an ssh key to be able to clone the git repository 
3. clone it using ssh
Login error possible with it -- don't use sudo!
run: 
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa (or whatever key file you are using)

Todo

1. Store the heridal data in one of the nodes -- possibly project folder --  also a test set
2. Store the python file to load and train a model and also handle resulting stuff
3. Use the best model to work on test set 

Folder structure:
data:
    train (generated by heridal)
    valid ( generated by python code )
    test (contain's hunter's stuff)
training pipepline class file ( will act as interface for any other type of model you want to train on -- either generates train/valid or uses the one that is already there --  for now we are only dealing with heridal so whatever )
        - will have data loading function
        - will have training function
        - will have a way to store the result for that model training in the project folder
        - will have a testing module
        - will have a way to zip and transfer results to your local for further analysis

model folder:
        model file (for yolo type of models, there is a similar type of way to do it, but there may be other models)
        - implements the training pipeline for a particular type of model
        - when a new model type is to be tried on, you create a new file for it.

finally -- curc script which I have to figure out a little bit
        - stores the data and models folder in project
        - 

