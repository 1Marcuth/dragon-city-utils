from pydantic import validate_call
from PIL import Image, ImageOps
import numpy as np

from .base import BaseAI, BaseAIConfig

class ElementsDetectorAI(BaseAI):
    def __init__(self) -> None:
        config = BaseAIConfig(
            model_zip_url = "https://cdn.discordapp.com/attachments/1061480758419664900/1099397120961822730/elements_detector_model.zip",
            model_out_dir = ".dcutils/ai_data/elements_detector/",
            model_zip_filename = "elements_detector_model.zip",
            model_filename = "keras_model.h5",
            labels_filename = "labels.txt"
        )

        super().__init__(config)
    
    @validate_call
    def detect(self, image_path: str, limit=4) -> list[dict]:
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

        sorted_indices = np.argsort(-prediction)
        top_limit_indices = sorted_indices[0][:limit]

        results = [
            {
                "element": self.model.labels[top_index].lower().split()[1],
                "confidence_score": float(prediction[0][top_index])
            }
            for top_index in top_limit_indices
        ]

        return results

__all__ = [ "ElementsDetectorAI" ]