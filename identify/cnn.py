from keras.models import load_model

classifier = load_model("C:\\Users\\DELL\\Desktop\\florista\\identify\\templates\\identify\\model_75.h5")
classifier._make_predict_function()