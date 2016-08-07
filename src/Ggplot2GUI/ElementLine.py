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

class ElementLine(Element):
    def __init__(self):
        super(ElementLine, self).__init__(False)
        self.linetype = "solid"
        self.lineend = "butt"

    def set_linetype_blank(self):
        self.linetype = "blank"

    def set_linetype_solid(self):
        self.linetype = "solid"

    def set_linetype_dashed(self):
        self.linetype = "dashed"

    def set_linetype_ddash(self):
        self.linetype = "dotdash"

    def set_linetype_ldash(self):
        self.linetype = "longdash"

    def set_linetype_tdash(self):
        self.linetype = "twodash"

    def set_lineend_round(self):
        self.lineend = "round"

    def set_lineend_butt(self):
        self.lineend = "butt"

    def set_lineend_squared(self):
        self.lineend = "squared"

    def get_linetype(self):
        return self.linetype

    def get_lineend(self):
        return self.lineend

    def __str__(self):
        mystr = super(ElementLine,self).__str__()
        mystr += ', linetype=\"{0}\"'.format(self.linetype)
        mystr += ', lineend=\"{0}\"'.format(self.lineend)
        return 'element_line({0})'.format(mystr)
