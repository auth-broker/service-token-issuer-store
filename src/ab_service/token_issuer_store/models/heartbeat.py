"""Heartbeat ORM Model."""

from ab_core.database.mixins.created_at import CreatedAtMixin
from ab_core.database.mixins.created_by import CreatedByMixin
from ab_core.database.mixins.id import IDMixin
from ab_core.database.mixins.updated_at import UpdatedAtMixin
from ab_core.token_issuer.token_issuers import TokenIssuer


class ManagedTokenIssuer(IDMixin, CreatedAtMixin, CreatedByMixin, UpdatedAtMixin, table=True):
    """Heartbeat ORM Model."""

    __tablename__ = "token_issuer"

    token_issuer: TokenIssuer
