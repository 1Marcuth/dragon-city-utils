from pydantic import validate_arguments

from ...base import BaseStaticDownloader

class DragonFlashAnimation(BaseStaticDownloader):
    @validate_arguments
    def __init__(
        self,
        image_name: str,
        phase: int
    ) -> None:
        if phase < 0 or phase > 3:
            raise ValueError(f"{phase} Not a valid number for a dragon's phase. Choose a number between 0 and 3")

        self.url = f"https://dci-static-s1.socialpointgames.com/static/dragoncity/assets/sprites/{image_name}_{phase}.swf"

__all__ = [ DragonFlashAnimation ]