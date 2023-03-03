from pydantic import validate_arguments
from urllib.request import urlretrieve

class BaseStaticDownloader:
    url: str

    @validate_arguments
    def download(self, output: str):
        urlretrieve(self.url, output)

__all__ = [ BaseStaticDownloader ]