#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent the Airbnb review.

    Attributes:
        place_id (str): The Airbnb Place id.
        user_id (str): The Airbnb User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
