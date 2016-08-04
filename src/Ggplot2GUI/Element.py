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

class Element:
    def __init__(self, blank):
        self.is_blank = blank
        if blank:
            self.colour = None
            self.size = None
        else:
            # Defaults are black and size 1 for a generic element
            self.colour = "#000000"
            self.size = 1

    def set_colour(self, colour):
        self.colour = colour

    def set_size(self, size):
        self.size = size

    def __repr__(self):
        if (self.is_blank):
            return ''
        else:
            return 'colour={0}, size={1}'.format(self.colour, self.size)
