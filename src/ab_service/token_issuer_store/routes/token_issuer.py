"""User-related API routes."""

from typing import Annotated
from fastapi import APIRouter
from fastapi import Depends as FDepends

from sqlalchemy.ext.asyncio import AsyncSession

from ab_core.database.session_context import db_session_async
from ab_service.token_issuer_store.models.heartbeat import ManagedTokenIssuer

router = APIRouter(prefix="/token-issuer", tags=["Token Issuer"])


@router.post("", response_model=ManagedTokenIssuer)
async def create(
    request: ManagedTokenIssuer,
    db_session: Annotated[AsyncSession, FDepends(db_session_async)],
):
    """Insert a heartbeat row and return it."""
    db_session.add(request)
    await db_session.flush()
    return request
