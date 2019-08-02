from scrapy import Selector


def extract_content(html, selector):
    value = Selector(text=html).xpath(selector).extract()
    if value:
        return value[0]
    return ""

def extract_list(html, selector, size=None):
    _list = Selector(text=html).xpath(selector).extract()
    if size:
        if _list:
            return _list[size]
    return _list

def extract_join(html, selector, char=" "):
    return char.join(Selector(text=html).xpath(selector).extract())