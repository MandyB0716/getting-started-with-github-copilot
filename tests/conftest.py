import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    yield

    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))