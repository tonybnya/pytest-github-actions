"""Tests for Person."""

import pytest

from beings import Person


@pytest.fixture()
def person():
    """Create a different instance of Person for testing purpose."""
    return Person("Tony NYA", 37, jobs=["Software Engineer"])


def test_init(person: Person):
    """Test the initialization process."""

    assert person.name == "Tony NYA"
    assert person.age == 37
    assert person.jobs == ["Software Engineer"]


def test_forename(person: Person):
    """Test forename."""

    assert person.forename == "Tony"


def test_surname(person: Person):
    """Test surname."""

    assert person.surname == "NYA"


def test_no_surname(person: Person):
    """Test no surname."""

    person.name = "Tony"
    assert not person.surname


def test_celebrate_birthday(person: Person):
    """Test celebrate_birthday."""

    person.celebrate_birthday()

    assert person.age == 38


def test_add_job(person: Person):
    """Test add_job."""

    job = "Freelancer"
    person.add_job(job)

    assert person.jobs == ["Software Engineer", "Freelancer"]
