from djangoseo import seo


class MetaAdd(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=150)
    keywords = seo.KeywordTag()