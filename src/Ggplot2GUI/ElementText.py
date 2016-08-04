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
        # lineheight and margin set to None for the moment
        self.lineheight = None
        self.margin = None
        self.debug = False

    # Not implemented for safety
    def set_family(self):
        pass

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
        self.lineheight = lineheight

    def set_margin(self, margin):
        self.margin = margin

    def set_debug(self, debug):
        self.debug = debug

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
