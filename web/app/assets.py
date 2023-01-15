from flask_assets import Bundle, Environment, Filter


class ConcatFilter(Filter):
    """
    Filter that merges files, placing a semicolon between them.

    Fixes issues caused by missing semicolons at end of JS assets, for example
    with last statement of jquery.pjax.js.
    """

    def concat(self, out, hunks, **kw):
        out.write(';'.join([h.data() for h, info in hunks]))


js = Bundle(
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js',
    'js/application.js',
    filters=(ConcatFilter, 'jsmin'),
    output='gen/packed.js'
)

css = Bundle(
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css',
    'css/fonts.css',
    'css/style.css',
    filters=('cssmin', 'cssrewrite'),
    output='gen/packed.css'
)

assets = Environment()
assets.register('js_all', js)
assets.register('css_all', css)
