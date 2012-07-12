Export/import transmogrifier blueprints
=======================================

This package contains blueprints for collective.transmogrifier
pipelines, that may be used to export/import Plone site content.
It also overrides GenericSetup ``Content`` step so this package
can be used out-the-box to migrate site content.


--------
jsbueno Branch:
    
    
    Includes ad-hoc modifications of quintagroup.transmogrifier
    for a specific migration task faced. 
    
    The changes are on the import pipeline (the export
    pipeline ad-hoc modifications where made on a Plone 2.1
    compatible version of the product, hosted elsewhere)
    
    The major modification is the item Path (including its ID) 
    which is picked not based from its position on the filesystem,
    but rather, transfered along on a separate plain text file, aside from
    the xml files used by the mainline product. This works around 
    the corner cases we had on this task (extra-long object IDs), and
    improves general reliability of the pipeline, as an identity of 
    file-system path to object path/id for the exported objects is no longer needed.
    
    Other changes include a Monkey patch aplied at transmogrifying time to
    disable an specific action (setting sindycation for ATTopic objects)
    that was raising an unauthorized exception at import time. 
    The respective "MonkeyPatcher" blueprint can be usefull for other tasks, and 
    should be factored out in a re-usable product in the near future.
    
    Also, there are included two views ("@@import" and "@@export") to trigger
    the pipelines without need to deal with portal_setup profiles activation.
    

    
    
    

Links
-----

Documentation and examples: http://projects.quintagroup.com/products/wiki/quintagroup.transmogrifier


Credits
-------

Design and development

    - Bohdan Koval
    - Andriy Mylenkyy
    - Taras Melnychuk
    - Vitaliy Stepanov
    - Vitaliy Podoba
    - Volodymyr Cherepanyak 
    - Myroslav Opyr 
    - Tom Lazar
    - Maurits Van Rees
    - Laurence Rowe
    - Mikko Ohtamaa

