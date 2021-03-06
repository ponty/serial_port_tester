from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages
import os

# logging.basicConfig(level=logging.DEBUG)
import paver.doctools
import paver.virtual
import paver.misctasks
from paved import *
from paved.dist import *
from paved.util import *
from paved.docs import *
from paved.pycheck import *
from paved.pkg import *
from pyavrutils import support


options(
    sphinx=Bunch(
        docroot='docs',
        builddir="_build",
    ),
#    pdf=Bunch(
#        builddir='_build',
#        builder='latex',
#    ),
)


options.paved.clean.rmdirs += ['.tox',
                               'dist',
                               'build',
                               ]
options.paved.clean.patterns += ['*.pickle',
                                 '*.doctree',
                                 '*.gz',
                                 'nosetests.xml',
                                 'sloccount.sc',
                                 '*.pdf', '*.tex',
                                 '*.png',

                                 'generated_*',  # generated files
                                 '*.zip',
                                 'distribute_setup.py',
                                 ]

options.paved.dist.manifest.include.remove('distribute_setup.py')
options.paved.dist.manifest.include.remove('paver-minilib.zip')
options.paved.dist.manifest.include.add('requirements.txt')
options.paved.dist.manifest.recursive_include.add('softusbduino *.csv')

docroot = path(options.sphinx.docroot)
root = path(__file__).parent.parent.abspath()
examples = support.find_examples(root)


@task
@needs(
    'sloccount',
    'html',
#    'pdf',
    #    'sdist',
    #    'nose',
    #    'tox',
)
def alltest():
    'all tasks to check'
    pass


@task
@needs('manifest', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our MANIFEST.in is generated.
    """
    pass
