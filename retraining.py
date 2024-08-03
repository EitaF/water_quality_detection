def load_vggmodel(h5file):
    model = load_model(h5file)
    return model

#Retraining by using new data

def retraining(model, train_data_gen, val_data_gen):
    model.compile(loss = "binary_crossentropy",
                  optimizer = Adam(learning_rate = 0.001),
                  metrics = ['accuracy'])

    history = model.fit(train_data_gen,
                        epochs = 50,
                        verbose = 1,
                        validation_data = val_data_gen,
                        callbacks = [EarlyStopping(patience = 5)])

    return model, history
