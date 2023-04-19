import sys
import datetime
from playwright.sync_api import sync_playwright, PdfMargins

PDF_PRINT_FORMAT = 'Letter'
PDF_PRINT_MARGIN = '20px'
FILENAME_SUFFIX = datetime.datetime.now().strftime('%Y%m%d%H%M')

def filename(url: str, ext: str):
    """ output file name. """
    return f"screenshot/{url.replace('/', '_').replace(':', '')}_{'screenshot' if ext == 'png' else 'page'}_{FILENAME_SUFFIX}.{ext}"

def print_margin(margin: str='0px') -> PdfMargins:
    """ pdf print margin. """
    return print_margins(top=margin, right=margin, bottom=margin, left=margin)

def print_margins(top: str='0px', right: str='0px', bottom: str='0px', left: str='0px') -> PdfMargins:
    """ pdf print margin. """
    return PdfMargins(top=top, right=right, bottom=bottom, left=left)

def screenshot(playwright, url: str):
    """ image file screen shot. """
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.screenshot(path=filename(url, 'png'), full_page=True)
    browser.close()

def print_pdf(playwright, url: str):
    """ pdf file print. """
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    page.emulate_media(media="print") # screen / print
    page.pdf(path=filename(url, 'pdf'),
             margin=print_margin(PDF_PRINT_MARGIN),
             format=PDF_PRINT_FORMAT)
    browser.close()

def main(urls: list[str]):
    with sync_playwright() as playwright:
        for url in urls:
            screenshot(playwright, url)
            print_pdf(playwright, url)

if __name__ == '__main__':
    main(sys.argv[1:])
