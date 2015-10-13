from django.shortcuts import render
from django.http import JsonResponse
from extractors.text import TextExtractor
from extractors.image import ImageExtractor
from extractors.music import MusicExtractor
from categoriser import Categoriser
from runner import Runner
from combiner import Combiner

# Create your views here.


def index(request):


    return JsonResponse({'foo': 'bar'})


def process(request):
    process_type = request.REQUEST['type']
    extractor = None

    if process_type == 'text':
        extractor = TextExtractor()
    elif process_type == 'image':
        extractor = ImageExtractor()
    elif process_type == 'music':
        extractor = MusicExtractor()

    processed_text = extractor.get_text(request.REQUEST)

    categoriser = Categoriser()

    categories = categoriser.categorise(processed_text)

    runner = Runner(4)

    experiences = runner.gather_experiences(processed_text, categories)

    combiner = Combiner()

    combined = combiner.combine(experiences)

    return JsonResponse({'html': combined})
