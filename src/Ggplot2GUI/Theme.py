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

class Theme(object):
    def __init__(self, is_pd):
        self.is_pd = is_pd
        if (self.is_pd):
            self.predef = "gray"
            self.predef_bs = 11
            self.predef_bf = ""
        else:
            # Set predefs to none
            self.predef = None
            self.predef_bs = None
            self.predef_bf = None
            # No predef: be default-specific

    # Functions for predefined themes
    def set_predef(self, predef, bf):
        self.predef = predef
        self.predef_bf = bf
        if (predef == "grey" or predef == "gray"):
            self.predef_bs = 11
        else:
            self.predef_bs = 12

    def get_predef(self):
        return self.predef

    def get_predef_bs(self):
        self.predef_bs

    def get_predef_bf(self):
        self.predef_bf

    def __str__(self):
        if (self.is_pd):
            return 'theme_{0}(base_size={1}, base_family=\"{2}\")' \
                    .format(self.predef, self.predef_bs, self.predef_bf)
