from extractor import Extractor


class TextExtractor(Extractor):
    def get_text(self, o):
        return o['text']
