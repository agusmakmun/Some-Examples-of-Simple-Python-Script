import warnings
import wikipedia

def _disableWarning():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    _disableWarning()
    ny = wikipedia.page("New York")
    print ny.title
    print ny.content
