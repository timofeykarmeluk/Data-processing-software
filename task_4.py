import os
import pandas as pd

dataset = os.path.join("../data/UCI HAR Dataset")
xTrain = pd.read_csv(os.path.join(dataset, "train", "x_train.txt"), sep="\\s+", header=None)
yTrain = pd.read_csv(os.path.join(dataset, "train", "y_train.txt"), sep="\t", header=None)
subjectTrain = pd.read_csv(os.path.join(dataset, "train", "subject_train.txt"), sep="\t", header=None)
xTest = pd.read_csv(os.path.join(dataset, "test", "x_test.txt"), sep="\\s+", header=None)
yTest = pd.read_csv(os.path.join(dataset, "test", "y_test.txt"), sep="\t", header=None)
subjectTest = pd.read_csv(os.path.join(dataset, "test", "subject_test.txt"), sep="\t", header=None)
features = pd.read_csv(os.path.join(dataset, "features.txt"), sep=" ", header=None)
activityLabels = pd.read_csv(os.path.join(dataset, "activity_labels.txt"), sep=" ", header=None)

xTrain.columns = features[1]
yTrain.columns = ["activityId"]
subjectTrain.columns = ["subjectId"]
xTest.columns = features[1]
yTest.columns = ["activityId"]
subjectTest.columns = ["subjectId"]
activityLabels.columns = ['activityId', 'activityType']

mergedTrain = pd.concat([xTrain, subjectTrain, yTrain], axis=1)
mergedTest = pd.concat([xTrain, subjectTrain, yTrain], axis=1)

print('1. Merges the training and the test sets to create one data set.')
mergedDataset = pd.concat([mergedTrain, mergedTest], axis=0)
mergedDataset.index = range(len(mergedDataset))
print(mergedDataset)

print('2. Extracts only the measurements on the mean and standard deviation for each measurement.')
print(mergedDataset[[i for i in mergedDataset.keys() if 'mean()' in i or 'std()' in i]])

print('3. Uses descriptive activity names to name the activities in the data set')
mergedDataset = mergedDataset.merge(activityLabels, on='activityId')
print(mergedDataset)

print('4. Appropriately labels the data set with descriptive variable names')
print('Done!')

print('5. From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject.')
tidyDataset = mergedDataset.groupby(['subjectId', 'activityId']).mean()
print(tidyDataset)