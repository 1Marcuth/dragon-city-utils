from ..base import BaseStaticDownloader

class GeneralMusic(BaseStaticDownloader):
    def __init__(
        self,
        music_name: str
    ) -> None:
        self.url = f"http://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/sounds/music/{music_name}.mp3"

__all__ = [ "GeneralMusic" ]