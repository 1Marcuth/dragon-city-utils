from pydantic import validate_arguments

from ..base import BaseStaticDownloader

class ChestSprite(BaseStaticDownloader):
    @validate_arguments
    def __init__(
        self,
        image_name: str,
        image_quality: int = 1
    ) -> None:
        if image_quality == 1:
            image_quality = ""

        elif image_quality == 2:
            image_quality = "@2x"
        
        self.url = f"https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/chests/ui_{image_name}{image_quality}.png"

__all__ = [ ChestSprite ]