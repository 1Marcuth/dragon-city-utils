from pydantic import validate_call
from typing import Optional

from ...platform_prefixes import PlatformPrefixes
from ...base import BaseStaticDownloader

class DragonFlashAnimation(BaseStaticDownloader):
    @validate_call
    def __init__(
        self,
        image_name: str,
        phase: int,
        skin: Optional[str] = None,
        platform_prefix: str = PlatformPrefixes.IOS
    ) -> None:
        if phase < 0 or phase > 3:
            raise ValueError(f"{phase} Not a valid number for a dragon's phase. Choose a number between 0 and 3")

        if skin:
            skin = f"_{skin}"
            
        else:
            skin = ""

        self.url = f"https://{platform_prefix}-static-s1.socialpointgames.com/static/dragoncity/assets/sprites/{image_name}{skin}_{phase}.swf"