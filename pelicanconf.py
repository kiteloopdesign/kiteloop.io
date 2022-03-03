# If using a theme, "AUTHORS" variable IS needed
AUTHORS = "Pablo M"
# AUTHOR = 'pablo m'
SITENAME = 'Ramblings from the post-capitalism'
# SITEURL = 'www.kiteloop.io'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# PMV:
LOAD_CONTENT_CACHE = False
# DISPLAY_PAGES_ON_MENU = True
WITH_FUTURE_DATES = True
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
# DEFAULT_DATE_FORMAT = '%d/%m/%Y'


# Specify name of a built-in theme
# THEME = "notmyidea"
# # Specify name of a theme installed via the pelican-themes tool
# THEME = "chunk"
# # Specify a customized theme, via path relative to the settings file
# THEME = "themes/mycustomtheme"
# # Specify a customized theme, via absolute path
THEME = "/home/kitesutra/www/pelican-themes/elegant/"


# STATIC_PATHS = [
#     'images',
#     'extra',  # this
# ]
# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'custom.css'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
#     'extra/CNAME': {'path': 'CNAME'},
#     'extra/LICENSE': {'path': 'LICENSE'},
#     'extra/README': {'path': 'README'},
# }


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
