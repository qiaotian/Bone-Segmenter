from __future__ import print_function

class CNNModel(object):
    def __init__(self, model, mean_val, max_val):
        self.mean_val = mean_val
        self.max_val = max_val
        self.model = model

    @staticmethod
    def preprocess(input_array, mean_val, max_val):
        input_array = input_array.astype('float32')
        input_array -= mean_val
        input_array /= max_val
        return input_array

    def predict_test(self, input_test_slices_arr):
        print("Preprocessing data.")
        test_slices_arr = self.preprocess(input_test_slices_arr, self.mean_val, self.max_val)
        print("Predicting the labelmap.")
        test_slices_prediction = self.model.predict(test_slices_arr, verbose=1, batch_size = 4) # reduce memory
        return test_slices_prediction
    
    def train(self, input_train_slices, input_train_segmentations, **kw_args):
        print("Preprocessing data.")
        train_slices_arr = self.preprocess(input_train_slices, self.mean_val, self.max_val)
        print("Training on the labelmap.")
        return self.model.fit(train_slices_arr, input_train_segmentations, verbose=1, shuffle = True, **kw_args)
