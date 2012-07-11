# coding: utf-8
"""
During import some checking/sessions of Plone may fail,
in a hard to work around way when performing the actual import.

A way to get through is to disable certain code which can't work properly
during the import context.

Thios section should be placed after any "source" sections,
as it has to restore the original cde after all objects are past
through the pipeline

For the task we have at hand, trying to enable syndcation on ATTopics
wrecks teh whole importing process - so we disable the code for that
for the lenght of the import.

"""

from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISection, ISectionBlueprint

from Products.ATContentTypes.content import topic


class Container(object):
    def initializeArchetype(self, **kwargs):    
        ret_val = ATCTFolder.initializeArchetype(self, **kwargs)
        return ret_val
    
        
        ## Enable topic syndication by default
        #syn_tool = getToolByName(self, 'portal_syndication', None)
        #if syn_tool is not None:
            #if (syn_tool.isSiteSyndicationAllowed() and
                                    #not syn_tool.isSyndicationAllowed(self)):
                ##syn_tool.enableSyndication(self)
        #return ret_val

def apply():
    global original_method
    original_method = topic.ATTopic.__dict__["initializeArchetype"]
    topic.ATTopic.initializeArchetype = Container.__dict__["initializeArchetype"]
    
def restore():
    topic.ATTopic.initializeArchetype = original_method
    

class MonkeyPatcherSession(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous

    def __iter__(self):
        apply()
        for item in self.previous:
            yield item
        restore()
