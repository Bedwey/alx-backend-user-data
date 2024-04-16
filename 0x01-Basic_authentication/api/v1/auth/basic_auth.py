#!/usr/bin/env python3
"""
This module contains the BasicAuth class which
serves as a template for basic authentication systems.
"""

from api.v1.auth.auth import Auth
import base64


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
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
