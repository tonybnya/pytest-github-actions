"""Person Module."""

from __future__ import annotations

from typing import List, Optional


class Person:
    """Definition of a Person."""

    def __init__(
        self,
        name: str,
        age: int,
        *,
        jobs: Optional[List[str]] = None,
    ) -> None:
        """Definition of a Person."""
        self.name = name
        self.age = age
        self.jobs = jobs or []

    @property
    def forename(self) -> str:
        """Get the firstname."""
        return self.name.split(" ")[0]

    @property
    def surname(self) -> Optional[str]:
        """Get the lastname."""
        name = self.name.split(" ")[-1]
        return name if name != self.forename else None

    def celebrate_birthday(self) -> None:
        """Increment age."""
        self.age += 1

    def add_job(self, title: str) -> None:
        """Add a new job to the list of jobs."""
        self.jobs.append(title)
