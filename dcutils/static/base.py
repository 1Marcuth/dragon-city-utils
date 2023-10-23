from urllib.request import urlretrieve
from pydantic import validate_call

class BaseStaticDownloader:
    url: str

    @validate_call
    def download(self, output: str):
        urlretrieve(self.url, output)

__all__ = [ "BaseStaticDownloader" ]