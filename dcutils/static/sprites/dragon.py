from pydantic import validate_call
from typing import Optional

from ..platform_prefixes import PlatformPrefixes
from ..base import BaseStaticDownloader

class DragonSprite(BaseStaticDownloader):
    @validate_call
    def __init__(
        self,
        image_name: str,
        phase: int,
        skin: Optional[str] = None,
        image_quality: int = 1,
        platform_prefix: str = PlatformPrefixes.IOS
    ) -> None:
        if phase < 0 or phase > 3:
            raise ValueError(f"{phase} Not a valid number for a dragon's phase. Choose a number between 0 and 3")

        if skin:
            skin = f"_{skin}"
        else:
            skin = ""

        if image_quality == 1:
            image_quality_str = ""

        elif image_quality == 2:
            image_quality_str = "@2x"

        else:
            raise ValueError(f"{image_quality} Not a valid number for image quality of a dragon. Choose a number between 1 and 2")

        self.url = f"https://{platform_prefix}-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/dragons/ui_{image_name}{skin}_{phase}{image_quality_str}.png"