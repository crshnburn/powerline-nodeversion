# vim:fileencoding=utf-8:noet
from powerline.segments import Segment, with_docstring
from subprocess import check_output

class NodeSegment(Segment):

    def __call__(self, pl):
        pl.debug('Running powerline-nodeversion')

        version = check_output(['node', '--version']).strip()

        segments = [
            {'contents': version}
        ]

        return segments

nodeversion = with_docstring(NodeSegment(),
'''Returns the current version of node in the environment.
''')