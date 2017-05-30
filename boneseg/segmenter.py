import SimpleITK as sitk
import numpy as np

from boneseg.utils import reshape_volume


class Segmenter(object):
    def __init__(self, model, threshold=0.5):
        self.model = model
        self.threshold = threshold

    def __predict(self, vol_nda):
        predicted_label = self.model.predict_test(input_test_slices_arr=vol_nda)
        return predicted_label

    def segment_bone_volume(self, input_volume_path, output_mask_path, rows, cols):
        vol = sitk.ReadImage(input_volume_path)
        vol_nda = sitk.GetArrayFromImage(vol)
        original_shape = vol_nda.shape
        vol_nda = reshape_volume(vol_nda, rows, cols)
        vol_nda = np.expand_dims(vol_nda, axis=1)
        label_nda = self.__predict(vol_nda)
        label_nda = label_nda[:, 0, :, :]
        # TODO: Check the indices for shape!
        # since the zoom function interpolates, threshold it again
        label_nda = reshape_volume(label_nda, original_shape[1], original_shape[2])>0.5
        label = sitk.GetImageFromArray(label_nda.astype(np.uint8))
        label.CopyInformation(vol)
        writer = sitk.ImageFileWriter()
        writer.Execute(label, output_mask_path, True)
