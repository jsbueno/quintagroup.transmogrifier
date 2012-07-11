# coding: utf-8
from collective.transmogrifier.transmogrifier import Transmogrifier

from Products.Five import BrowserView


class ImportView(BrowserView):
    def __init__(self, *args, **kw):
        BrowserView.__init__(self, *args, **kw)
        tr = Transmogrifier(self.context)
        print "Iniciando importações"
        #Name "import" as registered in this packages configure.zcml
        tr("import")
        self.request.RESPONSE.redirect(self.context.absolute_url())

class ExportView(BrowserView):
    def __init__(self, *args, **kw):
        BrowserView.__init__(self, *args, **kw)
        tr = Transmogrifier(self.context)
        print "Iniciando exportação"
        #Name "export" as registered in this packages configure.zcml
        tr("export")
        self.request.RESPONSE.redirect(self.context.absolute_url())
