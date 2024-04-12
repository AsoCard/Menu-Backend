from django.core.exceptions import ValidationError as DjangoValidationError, PermissionDenied
from django.http import Http404
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.serializers import as_serializer_error
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from coffeeshop.core.exceptions import ApplicationError


def custom_exception_handler(exc, context):
    # Handling DjangoValidationError
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    # Handling Http404
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    # Handling PermissionDenied
    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    # Let DRF handle other exceptions
    response = exception_handler(exc, context)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return Response({"result": [], "message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # If the response data is a list or dictionary, wrap it in a "detail" key
    if isinstance(response.data, (list, dict)):
        response.data = {
            "result": response.data,
            "message": "Error"
        }
    return response


def hacksoft_proposed_exception_handler(exc, ctx):
    """
    {
        "message": "Error message",
        "extra": {}
    }
    """
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        if isinstance(exc, ApplicationError):
            data = {
                "message": exc.message,
                "extra": exc.extra
            }
            return Response(data, status=400)

        return response

    if isinstance(exc.detail, (list, dict)):
        response.data = {
            "detail": response.data
        }

    if isinstance(exc, exceptions.ValidationError):
        response.data["message"] = "Validation error"
        response.data["extra"] = {
            "fields": response.data["detail"]
        }
    else:
        response.data["message"] = response.data["detail"]
        response.data["extra"] = {}

    del response.data["detail"]

    return response
