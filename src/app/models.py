"""Pydantic models for API requests and responses."""

from typing import Literal

from pydantic import BaseModel, Field, field_validator


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    redis: dict[str, bool | int]
    timestamp: str


class MainResponse(BaseModel):
    """Main endpoint response model."""

    message: str
    redis_data: str | None
    timestamp: str


class LoadRequest(BaseModel):
    """Load simulation request model."""

    level: Literal["low", "medium", "high"] = Field(
        default="low",
        description="Load level: low, medium, or high"
    )
    duration_seconds: int = Field(
        default=60,
        ge=1,
        le=3600,
        description="Duration in seconds (1-3600)"
    )

    @field_validator('level')
    @classmethod
    def validate_level(cls, v: str) -> str:
        """Validate load level."""
        if v not in ['low', 'medium', 'high']:
            raise ValueError('Level must be low, medium, or high')
        return v


class LoadResponse(BaseModel):
    """Load simulation response model."""

    status: str
    level: str
    duration_seconds: int


class HangRequest(BaseModel):
    """Hang request model."""

    duration_seconds: int = Field(
        default=0,
        ge=0,
        le=3600,
        description="Hang duration in seconds (0 means permanent, max 3600)"
    )


class RedisResetRequest(BaseModel):
    """Redis connection reset request model."""

    force: bool = True


class RedisResetResponse(BaseModel):
    """Redis connection reset response model."""

    status: str
    connections_closed: int
    timestamp: str


class ChaosStatusResponse(BaseModel):
    """Chaos status response model."""

    load: dict[str, bool | str | int]
    hang: dict[str, bool | int]
    redis: dict[str, bool | int | str | None]


class ErrorResponse(BaseModel):
    """Standardized error response model."""

    error: str
    detail: str | None = None
    timestamp: str
    request_id: str | None = None
