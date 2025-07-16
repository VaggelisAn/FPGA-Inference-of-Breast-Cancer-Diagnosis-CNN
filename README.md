
## Compressed NN Implementation for Low Power Medical Imaging	
Vaggelis Ananiadis, Supervisor: Prof. Karakonstantis G.
ECE-284 - Processor Design	

```
Directory structure:
└───pd_project
    │   dataset_preprocessing.ipynb	# dataset_preprocessing.ipynb prepares the dataset by augmenting the dataset 
    │					# and storing the training, validation and testing .npy files.
    │   optimized.ipynb 		# contains the model architecture, model training and HLS compilation.
    │   README.md					
    │   requirements.txt 		# packages that need to be installed
    │
    ├───common	
    │   	callbacks.py		# custom callback functions from hls4ml tutorials
    │   	custom_plotting.py	# custom plotting functions from hls4ml tutorials
    │
    └───dataset
		grayscale_dataset.py	# tool used to convert dataset to grayscale
		X_test_8.npy	
	        X_test_16.npy
	        X_test_32.npy
	        X_train_8.npy
		X_train_16.npy
	        X_train_32.npy
		X_val_8.npy
	        X_val_16.npy
	        X_val_32.npy
	        y_test.npy
	        y_train.npy
	        y_val.npy
		classes.npy
```		
			
The original dataset can be found on: https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset)

How to use:
Create a conda environment: conda create -n hls4ml_env python=3.10
Activate conda environment: conda activate hls4ml_env
Install package dependencies: pip install -r requirements.txt
Open jupyter: jupyter notebook
Select optimized.ipynb to check the architecture, training and HLS compilation code.
Select dataset_preprocessing.ipynb to check the dataset generation code.
Note that a Vitis installation is required for the HLS synthesis. Use Vitis >= 2023.2.

