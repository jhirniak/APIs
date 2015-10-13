from extractor import Extractor


class ImageExtractor(Extractor):
    def get_text(self, o):
        return 'image'
