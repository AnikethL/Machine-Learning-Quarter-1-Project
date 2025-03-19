# Machine-Learning-Quarter-1-Project

**Data setup**
Download the trainMerged_ND.csv under ML Q1 Project > Cleaned and Split Data > nonweka
OR
Manual data setup
Download data from: https://catalog.data.gov/dataset/crash-reporting-drivers-data
Run cleaner.py under “ML Q1 Project” Google Drive folder
Run base_preprocessing.py under “ML Q1 Project” Google Drive folder
Run encoder.py under “ML Q1 Project” Google Drive folder
Open csv outputted by previous step in Weka. Perform a train-test-validation split using stratified random sampling in Weka.
Under Filter, press Choose and go to weka > filters > supervised > instance > Resample



Then, click on the box to the right of the Choose button (the box should say Resample if you chose the correct filter) to open the weka.gui.GenericObjectEditor where you can then edit the parameter of the Resample filter. 



Then, set the noReplacement parameter to True, so each instance is only selected once. Set the sampleSizePercent to the proportion of the dataset to be in your training dataset (in our case, we are doing a 70/15/15 split so the training set has 70% of the data). 


Press Ok and then Apply to run the filter. Congratulations, you have your training set. Now press Save… to save the newly made subset. Now, you have to run another Resample filter to get your testing and validation sets. Reopen your original dataset, and repeat the prior steps until you are on the screen where you edited all the parameters for the Resample filter. Use the exact same parameters as before, but now, this time set invertSelection to True. This will give you the other 30% of the dataset, which you will now split into your test and validation sets.


Repeat the same steps as before on this dataset, but now set your sampleSizePercent accordingly to how you want to split your dataset (We are making the test and validation sets both 15% of the dataset, so we will set our sampleSizePercent to 50.0 since we are working with 30% of the data right now). Run the filter and save your test set, then repeat that again, but setting invertSelection to True this time to get your validation set.


Perform attribute selection algorithms as detailed in Part 4. As each arff file is being produced, place said file in a folder with its respective name (correlation, GainRatio, InfoGain, nonweka, CFS)
Run merge.py to combine the training and validation sets
Run fixNoDamage.py to clean up the class labels (this is to get rid of stray quotations added by Weka)
**Open Weka and load the file trainMerged_ND.csv **
If this was downloaded from Google Drive, it should be in home directory
If this was created from scratch, it should be under the “nonweka” folder
**Navigate to the classify tab choose the RandomForest classifier under weka > classifiers > trees **
**Press start and view the results in the classifier output window**
