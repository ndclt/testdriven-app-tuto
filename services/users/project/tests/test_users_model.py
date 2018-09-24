import unittest

from sqlalchemy.exc import IntegrityError

from project import db
from project.api.models import User
from project.tests.utils import add_user
from project.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_add_user(self):
        user = add_user('justatset', 'test@test.com', 'greaterthaneight')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatset')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        add_user('justatset', 'test@test.com', 'greaterthaneight')
        duplicate_user = User(
            username='justatset',
            email='test2@test.com',
            password='greaterthaneight'
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        add_user('justatset', 'test@test.com', 'greaterthaneight')
        duplicate_user = User(
            username='justatset2',
            email='test@test.com',
            password='greaterthaneight'
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user('justatset', 'test@test.com', 'greaterthaneight')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passwords_are_random(self):
        user_one = add_user('justatset', 'test@test.com', 'greaterthaneight')
        user_two = add_user('justatset2', 'test2@test.com', 'greaterthaneight')
        self.assertNotEqual(user_one.password, user_two.password)


if __name__ == '__main__':
    unittest.main()
