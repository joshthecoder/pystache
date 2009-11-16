import pystache

class TemplatePartial(pystache.View):
    template_path = 'examples'

    def title(self):
        return "Welcome"

    def title_bars(self):
        return '-' * len(self.title())
