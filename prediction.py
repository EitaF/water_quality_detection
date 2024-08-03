def prediction(h5file, image):
    model = load_vggmodel(h5file)
    image = predicted_image(image)
    predicted_result = model.predict(image.reshape(-1, 224, 224, 3))
    return predicted_result
