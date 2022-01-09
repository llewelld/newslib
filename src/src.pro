TARGET = news
TEMPLATE = lib

SOURCES += newslib.cpp

HEADERS += newslib.h

INSTALL_HEADERS += newslib.h

HEADERS *= $$INSTALL_HEADERS

pcfiles.files = $$OUT_PWD/news.pc
pcfiles.CONFIG = no_check_exist
pcfiles.path += $$INSTALL_ROOT/$$[QT_INSTALL_LIBS]/pkgconfig

headers.files += $$INSTALL_HEADERS
headers.path += /usr/include/news

target.path += $$[QT_INSTALL_LIBS]

INSTALLS += target headers pcfiles

