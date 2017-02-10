import os
import glyphsLib
import defcon


class Builder:

    def __init__(self, params=None):
        self.params=params

    def merge(self, *sources):
        new_font=defcon.Font()

        for path in sources:
            source=defcon.Font(path)
            if new_font.info.familyName==None:
                new_font.info.__dict__=source.info.__dict__
            for layer in source.layers:
                if not layer.name in new_font.layers:
                    new_font.newLayer(layer.name)

                for glyph in layer:
                    new_font.layers[layer.name].insertGlyph(glyph)

            new_font.kerning.update(source.kerning)
            new_font.groups.update(source.groups)
        return new_font

    def save_ufo(self, ufo, path):
        ufo.save(path)

    def get_ufo(self, path):
        root, ext=os.path.splitext(path)
        ext=ext.lower()
        if ext==".glyphs":
            return glyphsLib.load_to_ufos(path)
        elif ext==".ufo":
            return defcon.font(path)
