import numpy as np

class ArrayStr():
    def __init__(self, array):
        self.array1 = array
    def Min(self):
        return np.min(self.array1)
    def Max(self):
        return np.max(self.array1)
    def Mean(self):
        return np.average(self.array1)
    def Range(self):
        return np.max(self.array1) - np.min(self.array1)
    def ZScore(self):
        return (self.array1 - np.min(self.array1)) / (np.max(self.array1) - np.min(self.array1)) # My zscore is Zi=(Xi-MİN)/RANGE --> Min of Zscore is 0 Max of Zscore is 1


#Solution Trials
my_array = [4, 2, 4, 4, 8, 2, 4, 8, 10]
TestArray = ArrayStr(my_array)
print("for given array {}, Min value is: {}".format(my_array,TestArray.Min()))
print("for given array {}, Max value is: {}".format(my_array,TestArray.Max()))
print("for given array {}, Mean value is: {}".format(my_array,TestArray.Mean()))
print("for given array {}, Range is: {}".format(my_array,TestArray.Range()))
print("for given array {}, Zscores (Zi=(Xi-MİN)/RANGE)  values are: {}".format(my_array,TestArray.ZScore()))