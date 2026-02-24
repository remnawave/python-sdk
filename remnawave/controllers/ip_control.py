from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    DropConnectionsRequestDto,
    DropConnectionsResponseDto,
    FetchIpsResponseDto,
    FetchIpsResultResponseDto,
)
from remnawave.rapid import BaseController, get, post


class IpControlController(BaseController):
    @post("/ip-control/fetch-ips/{uuid}", response_class=FetchIpsResponseDto)
    async def fetch_user_ips(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> FetchIpsResponseDto:
        """Request IP List for User.

        Starts a background job that queries all connected nodes for the IPs
        used by the given user.  The returned ``job_id`` must be passed to
        :meth:`get_fetch_ips_result` to retrieve the actual list once the job
        is complete.
        """
        ...

    @get("/ip-control/fetch-ips/result/{jobId}", response_class=FetchIpsResultResponseDto)
    async def get_fetch_ips_result(
        self,
        jobId: Annotated[str, Path(description="Job ID returned by fetch_user_ips")],
    ) -> FetchIpsResultResponseDto:
        """Get IP List Result by Job ID.

        Poll this endpoint after calling :meth:`fetch_user_ips`.  When
        ``is_completed`` is ``True`` the ``result`` field contains per-node
        IP lists.  When ``is_failed`` is ``True`` the job encountered an
        error.
        """
        ...

    @post("/ip-control/drop-connections", response_class=DropConnectionsResponseDto)
    async def drop_connections(
        self,
        body: Annotated[DropConnectionsRequestDto, PydanticBody()],
    ) -> DropConnectionsResponseDto:
        """Drop active connections.

        Sends a drop-connections event to the target nodes.  You can specify
        the connections to drop either by user UUIDs or by IP addresses, and
        you can target all connected nodes or a specific subset.
        """
        ...
