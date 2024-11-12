import numpy as np
import keras as tfk


class Model:
    def __init__(self):
        """Initializes the model's internal state."""
        self.model: tfk.Model = tfk.saving.load_model("model.keras")

    def predict(self, X: np.ndarray) -> np.ndarray:  # noqa: N803
        """Returns a numpy array of labels for the given input X."""
        y = self.model.predict(X)
        if len(y.shape) == 2:
            labels = np.argmax(y, axis=1)
        return labels
