#!/usr/bin/env python3
"""
This module contains the Auth class which serves
as a template for all authentication systems.
"""


from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth:
    """
    This class is a template for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path is within the list of excluded paths.

        :param path: a string representing the path of the request
        :param excluded_paths: a list of strings representing the
        paths that don't require authentication
        :return: False if the path is in the list of excluded paths,
        True otherwise
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the authorization header.

        :param request: the Flask request object from which
        the header should be retrieved
        :return: None for now, will be implemented in the future
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Returns the current authenticated user.

        :param request: the Flask request object from which
        the user should be retrieved
        :return: None for now, will be implemented in the future
        """
        return None
