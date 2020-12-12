#  mpvQC
#
#  Copyright (C) 2020 mpvQC developers
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


from pathlib import Path
from typing import NamedTuple, Optional, Tuple

from mpvqc.engine.comment import Comment


class Document(NamedTuple):
    file: Optional[Path] = None
    video: Optional[Path] = None
    comments: Tuple[Comment] = tuple()


class Incompatible(NamedTuple):
    file: Path


class DocumentImport(NamedTuple):
    documents: Tuple[Document]
    incompatibles: Tuple[Incompatible]
