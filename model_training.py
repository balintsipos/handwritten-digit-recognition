from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle
import cv2

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
model = svm.SVC(gamma=0.001)

X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)

model.fit(X_train, y_train)
predict = model.predict(X_test)

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, predict in zip(axes, X_test, predict):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(f"Prediction: {predict}")

pickle.dump(model, open("model.pkl", 'wb'))

loaded_model = pickle.load(open('model.pkl', 'rb'))

file = r'nine.jpg'
test_image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
plt.imshow(test_image, cmap='gray')

img_resized = cv2.resize(test_image, (8, 8), interpolation=cv2.INTER_LINEAR)
img_resized = cv2.bitwise_not(img_resized)
plt.imshow(img_resized, cmap='gray')

print(loaded_model.predict(img_resized))