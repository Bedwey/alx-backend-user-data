#!/usr/bin/env python3
"""
This module contains the BasicAuth class which
serves as a template for basic authentication systems.
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    This class is a template for basic authentication systems.
    It inherits from the Auth class.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the
        Authorization header for a Basic Authentication.

        :param authorization_header: a string
        representing the Authorization header
        :return: None if the authorization_header is None,
        not a string, or doesn't start with "Basic ",
        otherwise the part of the string after "Basic "
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string
        base64_authorization_header.

        :param base64_authorization_header: a Base64 string
        :return: None if base64_authorization_header is None,
        not a string, or not a valid Base64,
        otherwise the decoded value as a UTF-8 string
        """
        if base64_authorization_header is None or \
           type(base64_authorization_header) is not str:
            return None

        try:
            return base64.b64decode(base64_authorization_header) \
                .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value.

        :param decoded_base64_authorization_header: a Base64 decoded string
        :return: (None, None) if decoded_base64_authorization_header is None,
        not a string, or doesn't contain a colon,
        otherwise the user email and password as a tuple
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str or \
                ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password.

        :param user_email: a string representing the user's email
        :param user_pwd: a string representing the user's password
        :return: None if user_email or user_pwd is None or not a string,
        if the database doesn't contain a User instance
        with email equal to user_email,
        or if user_pwd is not the password of the User instance found,
        otherwise the User instance
        """
        if user_email is None or type(user_email) is not str or \
                user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
