import src


class UI(src.boiler_ui_module.BoilerUIModule):
    id_ = 'about'
    classes = {'scrolling-panel', 'info-panel'}
    name = 'About'

    def render(self):
        return self.render_string(
            '../panels/about/about.html')
