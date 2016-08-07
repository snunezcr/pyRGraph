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

class ElementRect(Element):
    def __init__(self):
        super(ElementRect, self).__init__(False)
        self.fill = "#FFFFFF"
        self.linetype = "solid"

    def set_fill(self, fill):
        self.fill = fill

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

    def get_fill(self):
        return self.fill

    def get_linetype(self):
        return self.linetype

    def __str__(self):
        mystr = super(ElementRect,self).__str__()
        mystr += ', fill=\"{0}\"'.format(self.fill)
        mystr += ', linetype=\"{0}\"'.format(self.linetype)
        return 'element_line({0})'.format(mystr)
