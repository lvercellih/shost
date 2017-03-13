from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.renderers import SwaggerUIRenderer


class JSONOpenAPIRenderer(JSONRenderer):
    format = 'openapi'


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        SwaggerUIRenderer,
        JSONOpenAPIRenderer
    ]
    schema = None

    def get(self, request):
        return Response(self.schema)
