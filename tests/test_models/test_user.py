#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):

    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        self.name = "User"
        self.value = User

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_first_name(self):
        """ """
        user = self.value()
        user.first_name = 'firstname'
        self.assertEqual(type(user.first_name), str)

    def test_last_name(self):
        """ """
        user = self.value()
        user.last_name = 'lastname'
        self.assertEqual(type(user.last_name), str)

    def test_email(self):
        """ """
        user = self.value()
        user.email = 'name@email.com'
        self.assertEqual(type(user.email), str)

    def test_password(self):
        """ """
        user = self.value()
        user.password = 'password'
        self.assertEqual(type(user.password), str)

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if models.storage_t == 'db':
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, "")


if __name__ == "__main__":
    unittest.main()
