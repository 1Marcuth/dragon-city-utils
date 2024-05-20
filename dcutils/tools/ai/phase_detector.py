from pydantic import validate_call
from PIL import Image, ImageOps
import numpy as np

from .base import BaseAI, BaseAIConfig

class PhaseDetectorAI(BaseAI):
    def __init__(self) -> None:
        config = BaseAIConfig(
            model_zip_url = "https://cdn.discordapp.com/attachments/1057469643402526781/1099397032805933148/phase_detector_model.zip",
            model_out_dir = ".dcutils/ai_data/phase_detector/",
            model_zip_filename = "phase_detector_model.zip",
            model_filename = "keras_model.h5",
            labels_filename = "labels.txt"
        )

        super().__init__(config)
    
    @validate_call
    def detect(self, image_path: str) -> dict:
        image_size = (224, 224)

        image = Image.open(image_path).convert("RGB")
        image = ImageOps.fit(
            image,
            image_size,
            Image.Resampling.LANCZOS
        )

        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        self.data[0] = normalized_image_array

        prediction = self.model.predict(self.data)

        top_index = np.argmax(prediction)

        result = {
            "phase": self.model.labels[top_index][2:].strip().lower(),
            "confidence_score": float(prediction[0][top_index])
        }

        return result