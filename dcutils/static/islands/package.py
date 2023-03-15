from ..base import BaseStaticDownloader

class IslandPackage(BaseStaticDownloader):
    def __init__(
        self,
        uri: str
    ) -> None:
        uri_splited = uri.split("/")
        type_ = uri_splited[3]
        filename = uri_splited[4]

        if type_ == "grid_islands":
            filename.replace(".zip", "_optim.zip")

        self.url = f"https://www.socialpointgames.com/static/dragoncity/mobile/ui/{type_}/HD/dxt5/{filename}"

__all__ = [ "IslandPackage" ]