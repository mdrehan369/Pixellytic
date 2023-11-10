import os
import joblib
from sklearn.linear_model import LogisticRegression
import pywt
import pandas as pd
import numpy as np
import cv2


class BuildModel:

    def __init__(self, folder):

        self.training_images_folder = folder
        self.samples_folder = "samples/"
        self.cnt = 0
        self.faceCascade = cv2.CascadeClassifier("Haar Cascades/haarcascade_frontalface_default.xml")
        self.eyeCascade = cv2.CascadeClassifier("Haar Cascades/haarcascade_eye.xml")
        self.image_files1 = pd.DataFrame(columns=range(11025)).add_prefix('pixels_')
        # self.image_files2 = pd.DataFrame(columns=range(11025)).add_prefix('pixels_')
        self.image_files2 = pd.read_csv("sample.csv", index_col=0)

    def _w2d(self, img, mode='haar', level=1):
        imArray = img
        # Datatype conversions
        # convert to grayscale
        imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
        # convert to float
        imArray = np.float32(imArray)
        imArray /= 255
        # compute coefficients
        coeffs = pywt.wavedec2(imArray, mode, level=level)

        # Process Coefficients
        coeffs_H = list(coeffs)
        coeffs_H[0] *= 0

        # reconstruction
        imArray_H = pywt.waverec2(coeffs_H, mode)
        imArray_H *= 255
        imArray_H = np.uint8(imArray_H)

        return imArray_H

    def _makeDataframe(self):

        folder = self.training_images_folder
        df = self.image_files1

        for image in os.scandir(folder):
            splitfile = os.path.splitext(image.path)
            if splitfile[1] != ".jpg":
                continue

            img = cv2.imread(image.path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = self.faceCascade.detectMultiScale(gray)
            for (x, y, w, h) in face:
                roi_gray = gray[y: y + h, x: x + w]
                roi_img = img[y: y + h, x: x + w]
                eyes = self.eyeCascade.detectMultiScale(roi_gray)
                if len(eyes) >= 2:
                    w2d_img = self._w2d(roi_img, "db1", 5)
                    resized_img = cv2.resize(w2d_img, (105, 105)).astype(np.float32)
                    resized_img = resized_img.reshape(-1)
                    df.loc[f'image_{self.cnt}', 'pixels_0':] = resized_img
                    self.cnt += 1

    def trainModel(self, name):
        print("Training")
        self._makeDataframe()
        self.image_files1["pred"] = 1

        self.image_files2["pred"] = 0

        X = pd.concat([self.image_files1, self.image_files2])
        y = X["pred"]
        X.drop(["pred"], axis=1, inplace=True)

        model = LogisticRegression(solver="liblinear", dual=True, C=0.2)
        model.fit(X, y)

        if os.path.exists("models") is False:
            os.mkdir("models")

        joblib.dump(model, f"models/{name}.pkl")

    def predictAndSave(self, source, destination, model_path):

        model = joblib.load(f"models/{model_path}.pkl")
        i = 0

        for image in os.scandir(source):
            splitfile = os.path.splitext(image.path)
            if splitfile[1] != ".jpg":
                continue
            img = cv2.imread(image.path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = self.faceCascade.detectMultiScale(gray)
            for (x, y, w, h) in face:
                roi_gray = gray[y: y + h, x: x + w]
                roi_img = img[y: y + h, x: x + w]
                eyes = self.eyeCascade.detectMultiScale(roi_gray)
                if len(eyes) >= 2:

                    img_w2d = self._w2d(roi_img, "db1", 5)
                    Ximg = cv2.resize(img_w2d, (105, 105)).astype(np.float32)
                    Ximg = Ximg.reshape(1, -1)
                    y = model.predict(Ximg)
                    print(y[0])
                    if y[0] == 1:
                        cv2.imwrite(destination + f"/image{i}.jpg", img)
                        i += 1


if __name__ == "__main__":
    print("hello")
