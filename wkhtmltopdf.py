# -*- coding: utf-8 -*-
import os

from luckyappscanner import settings


class Wkhtmltopdf(object):

    def __init__(self, *args, **kwargs):
        self.url = None
        self.output_file = None

        try:
            self.url, self.output_file = args[0], args[1]
        except IndexError:
            pass

        if not self.url or not self.output_file:
            raise Exception("Missing url and output file arguments")

        output_path = os.path.split(self.output_file)[0]
        if not output_path:
            self.output_file = os.path.join('/tmp', self.output_file)

        self.defaults = {
            'screen_resolution': [kwargs.get('screen_resolution', [1024, 768]), list],
            'color_depth': [kwargs.get('color_depth', 24), int],
            'flash_plugin': [kwargs.get('flash_plugin', False), bool],
            'disable_javascript': [kwargs.get('disable_javascript', False), bool],
            'delay': [kwargs.get('delay', 0), int],
            'dpi': [kwargs.get('dpi', 100), int],
            'no_background': [kwargs.get('no_background', False), bool],
            'grayscale': [kwargs.get('grayscale', False), bool],
            'http_username': [kwargs.get('http_username', ""), str],
            'http_password': [kwargs.get('http_password', ""), str],
            'margin_bottom': [kwargs.get('margin_bottom', "10mm"), str],
            'margin_left': [kwargs.get('margin_left', "10mm"), str],
            'margin_right': [kwargs.get('margin_right', "10mm"), str],
            'margin_top': [kwargs.get('margin_top', "10mm"), str],
            'page_size': [kwargs.get('page_size', "A4"), str],
            'cover': [kwargs.get('cover', ""), str],
            'footer_font_name': [kwargs.get('footer_font_name', "Arial"), str],
            'footer_font_size': [kwargs.get('footer_font_size', "11"), str],
            'footer_html': [kwargs.get('footer_html', ""), str],
            'footer_left': [kwargs.get('footer_left', ""), str],
            'footer_center': [kwargs.get('footer_center', ""), str],
            'footer_right': [kwargs.get('footer_right', ""), str],
            'footer_line': [kwargs.get('footer_line', False), bool],
            'footer_spacing': [kwargs.get('footer_spacing', ''), str],
            'header_font_name': [kwargs.get('header_font_name', "Arial"), str],
            'header_font_size': [kwargs.get('header_font_size', "11"), str],
            'header_html': [kwargs.get('header_html', ""), str],
            'header_left': [kwargs.get('header_left', ""), str],
            'header_center': [kwargs.get('header_center', ""), str],
            'header_right': [kwargs.get('header_right', ""), str],
            'header_line': [kwargs.get('header_line', False), bool],
            'header_spacing': [kwargs.get('header_spacing', ''), str],
            'toc': [kwargs.get('toc', False), bool],
            'toc_header_text': [kwargs.get('toc_header_text', ''), str],
            'toc_level_indentation': [kwargs.get('toc_level_indentation', ''), str],
        }

        for k, v in self.defaults.items():
            if not isinstance(v[0], v[1]):
                try:
                    v[0] = v[1](v[0])
                    print v[0]
                except TypeError:
                    raise TypeError("%s argument required for %s" % (v[1].__name__.capitalize(), k))
            if k is "orientation" and v[0] not in ['Portrait', 'Landscape']:
                raise TypeError("Orientation argument must be either Portrait or Landscape")
            setattr(self, k, v[0])

    def _create_option_list(self):
        """
        Add command option according to the default settings.
        """
        option_list = []
        if self.disable_javascript:
            option_list.append("--disable-javascript")
        if self.no_background:
            option_list.append("--no-background")
        if self.grayscale:
            option_list.append("--grayscale")
        if self.delay:
            option_list.append("--redirect-delay %s" % self.delay)
        if self.http_username:
            option_list.append("--username %s" % self.http_username)
        if self.http_password:
            option_list.append("--password %s" % self.http_password)
        if self.dpi != 100:
            option_list.append("--dpi %s" % self.dpi)
        if self.margin_bottom != '10mm':
            option_list.append("--margin-bottom %s" % self.margin_bottom)
        if self.margin_left != '10mm':
            option_list.append("--margin-left %s" % self.margin_left)
        if self.margin_right != '10mm':
            option_list.append("--margin-right %s" % self.margin_right)
        if self.margin_top != '10mm':
            option_list.append("--margin-top %s" % self.margin_top)
        if self.page_size != 'A4':
            option_list.append("--page-size %s" % self.page_size)
        if self.footer_font_name != 'Arial':
            option_list.append("--footer-font-name %s" % self.footer_font_name)
        if self.footer_font_size != '11':
            option_list.append("--footer-font-size %s" % self.footer_font_size)
        if self.footer_html != '':
            option_list.append("--footer-html %s" % self.footer_html)
        if self.footer_left != '':
            option_list.append("--footer-left %s" % self.footer_left)
        if self.footer_center != '':
            option_list.append("--footer-center %s" % self.footer_center)
        if self.footer_right != '':
            option_list.append("--footer-right %s" % self.footer_right)
        if self.footer_line:
            option_list.append("--footer-line")
        if self.footer_spacing != '':
            option_list.append("--footer-spacing %s" % self.footer_spacing)
        if self.header_font_name != 'Arial':
            option_list.append("--header-font-name %s" % self.header_font_name)
        if self.header_font_size != '11':
            option_list.append("--header-font-size %s" % self.header_font_size)
        if self.header_html != '':
            option_list.append("--header-html %s" % self.header_html)
        if self.header_left != '':
            option_list.append("--header-left %s" % self.header_left)
        if self.header_center != '':
            option_list.append("--header-center %s" % self.header_center)
        if self.header_right != '':
            option_list.append("--header-right %s" % self.header_right)
        if self.header_line:
            option_list.append("--header-line")
        if self.header_spacing != '':
            option_list.append("--header-spacing %s" % self.header_spacing)
        if self.cover != '':
            option_list.append("cover %s" % self.cover)
        if self.toc:
            option_list.append("toc")
        if self.toc_header_text != '' and self.toc:
            option_list.append("--toc-header-text %s" % self.toc_header_text)
        if self.toc_level_indentation != '' and self.toc:
            option_list.append("--toc-level-indentation %s" % self.toc_level_indentation)

        return option_list

    def render(self):

        if not os.getenv('DISPLAY'):
            os.system("Xvfb :0 -screen 0 %sx%sx%s & " % (
                self.screen_resolution[0],
                self.screen_resolution[1],
                self.color_depth
            ))
            os.putenv("DISPLAY", '127.0.0.1:0')

        command = settings.BASE_DIR + '/dynamic_tester/tools/wkhtmltopdf %s %s %s' % (' '.join(self._create_option_list()), self.url, self.output_file)

        print command
        sys_output = int(os.system(command))

        if not sys_output:
            return True, self.output_file
        return False, sys_output


def wkhtmltopdf(*args, **kwargs):
    wkhp = Wkhtmltopdf(*args, **kwargs)
    wkhp.render()






