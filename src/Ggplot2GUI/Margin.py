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

class Margin(object):
    def __init__(self):
        self.t = 0
        self.r = 0
        self.b = 0
        self.l = 0

    def set_t(self, t):
        self.t = t

    def set_r(self, r):
        self.r = r

    def set_b(self, b):
        self.b = b

    def set_l(self, l):
        self.l = l

    def get_t(self):
        return self.t

    def get_r(self):
        return self.r

    def get_b(self):
        return self.b

    def get_l(self):
        return self.l

    def __str__(self):
        # Different units are not handled here. This must be added at
        # some point if relevant.
        return 'margin({0}, {1}, {2}, {3})'.format(self.t,self.r,self.b,self.l)
