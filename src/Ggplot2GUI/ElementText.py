# Author: Santiago Nunez-Corrales
#
# This file is part of pyRGraph.
#
# pyRGraph is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyRGraph is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyRGraph.  If not, see <http://www.gnu.org/licenses/>.

from Element import Element
from Margin import Margin

class ElementText(Element):
    def __init__(self):
        super(ElementText, self).__init__(False)
        # Now we add all additional elements of element_text
        # Special case: use the default font
        self.family = None
        self.face = "plain"
        # We standarize font sizes to 10
        super(ElementText, self).set_size(10)
        self.hjust = 0
        self.vjust = 0
        self.angle = 0
        self.lineheight = 1.0
        self.margin = Margin()
        self.debug = False

    # Not implemented for safety
    def set_family(self, family):
        self.family = family

    # Face settings are implemented as closed options
    def set_face_plain(self):
        self.face = "plain"

    def set_face_italic(self):
        self.face = "italic"

    def set_face_bold(self):
        self.face = "bold"

    def set_face_boldit(self):
        self.face = "bold.italic"

    def set_hjust(self, hjust):
        self.hjust = hjust

    def set_vjust(self, vjust):
        self.vjust = vjust

    def set_angle(self, angle):
        self.angle = angle

    def set_lineheight(self, lineheight):
        if -0.5 <= lineheight <= 2.0:
            self.lineheight = lineheight

    def set_margin(self, margin):
        self.margin = margin

    def set_debug(self, debug):
        self.debug = debug

    def get_family(self):
        return self.family

    def get_face(self):
        return self.face

    def get_hjust(self):
        return self.hjust

    def get_vjust(self):
        return self.vjust

    def get_angle(self):
        return self.angle

    def get_lineheight(self):
        return self.lineheight

    def get_margin(self):
        return self.margin

    def get_debug(self):
        return self.debug

    def __str__(self):
        mystr = super(ElementText,self).__str__()
        if self.family is not None:
            mystr += ', family=\"{0}\"'.format(self.family)
        if self.face is not None:
            mystr += ', face=\"{0}\"'.format(self.face)
        mystr += ', hjust={0}'.format(self.hjust)
        mystr += ', vjust={0}'.format(self.vjust)
        mystr += ', angle={0}'.format(self.angle)
        mystr += ', lineheight={0}'.format(self.lineheight)
        mystr += ', margin={0}'.format(self.margin)
        if self.debug:
            mystr += ', debug=TRUE'
        return 'element_text({0})'.format(mystr)
