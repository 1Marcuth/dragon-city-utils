from typing import Optional

from ..base import BaseStaticDownloader
from .config import get_music_name_from_tag

class GeneralMusic(BaseStaticDownloader):
    def __init__(
        self,
        music_name: Optional[str] = None,
        tag: Optional[str] = None
    ) -> None:
        if not tag and not music_name:
            raise ValueError("You must enter at least one name or tag!")

        if tag:
            music_name = get_music_name_from_tag(tag)

        if not music_name:
            raise ValueError("Please enter a valid song name! If you have entered a tag please check it as it was not possible to get a song name from it.")

        self.url = f"http://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/sounds/music/{music_name}.mp3"

__all__ = [ "GeneralMusic" ]