from pydantic import validate_call

from ..base import BaseStaticDownloader

class DragonThumb(BaseStaticDownloader):
    @validate_call
    def __init__(
        self,
        image_name: str,
        phase: int,
        skin: int | None = None
    ) -> None:
        if phase < 0 or phase > 3:
            raise ValueError(f"{phase} Not a valid number for a dragon's phase. Choose a number between 0 and 3")

        if skin and skin > 0:
            skin_str = f"_skin{skin}"
        
        else:
            skin_str = ""
        
        self.url = f"https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/dragons/HD/thumb_{image_name}{skin_str}_{phase}.png"

__all__ = [ "DragonThumb" ]