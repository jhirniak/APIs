from extractor import Extractor


class MusicExtractor(Extractor):
    def get_text(self, o):
        return 'music'
