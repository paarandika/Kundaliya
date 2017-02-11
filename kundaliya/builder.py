import os
import glyphsLib
import defcon
import io
import logging
from params import Params

logger = logging.getLogger(__name__)


class Builder:
    def __init__(self, params=None):
        logging.basicConfig(level=logging.WARNING)
        self.params = params

    def execute(self):
        if self.params is None:
            return

        if hasattr(self.params, 'merge') and self.params.merge is not None:
            for job in self.params.merge['jobs']:
                info_params = Params(os.path.join(self.params.cwd, job['output info file']))
                merged = self.merge(job['sources'], info_params, job['output feature file'])
                self.save_ufo(merged, job['out'])

    def merge(self, sources, info_params=None, features_path=None):
        new_font = defcon.Font()

        for path in sources:
            source = defcon.Font(os.path.join(self.params.cwd, path))
            if new_font.info.familyName is None:
                new_font.info.__dict__ = source.info.__dict__
            for layer in source.layers:
                if not layer.name in new_font.layers:
                    new_font.newLayer(layer.name)

                for glyph in layer:
                    new_font.layers[layer.name].insertGlyph(glyph)

            new_font.kerning.update(source.kerning)
            new_font.groups.update(source.groups)

        if features_path is not None:
            try:
                with io.open(os.path.join(self.params.cwd, features_path)) as features:
                    new_font.features.text = features.read()
            except IOError:
                logger.error("File error")
            except RuntimeError as e:
                logger.error("Unknown error", e)

        if info_params is not None:
            new_font = self.set_info_params(new_font, info_params)

        return new_font

    def save_ufo(self, ufo, path):
        ufo.save(os.path.join(self.params.cwd, path))

    def get_ufo(self, path):
        root, ext = os.path.splitext(path)
        ext = ext.lower()
        if ext == ".glyphs":
            return glyphsLib.load_to_ufos(path)
        elif ext == ".ufo":
            return defcon.font(path)

    def set_info_params(self, ufo, info_params):
        params = info_params.__dict__
        for param in params:
            setattr(ufo.info, param, params[param])
        return ufo
