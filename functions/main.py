from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode

class TagFilterPreprocessor(Preprocessor):
    def __init__(self, allowed_tags, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_tags = set(allowed_tags)

    def preprocess(self, nb, resources):
        for cell in nb.cells:
            if 'metadata' in cell and 'tags' in cell.metadata:
                tags = set(cell.metadata['tags'])
                if not tags.intersection(self.allowed_tags):
                    nb.cells.remove(cell)
        return nb, resources