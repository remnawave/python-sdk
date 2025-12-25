from typing import Annotated

from rapid_api_client import Path, Query

from remnawave.models import (
    GetNodeUserUsageByRangeResponseDto,
    GetNodesUsageByRangeResponseDto,
)
from remnawave.rapid import BaseController, get
