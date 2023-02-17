# Import installed packages
from apispec import APISpec
from flask_apispec import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin

# Import app code
from ...main import app
from ...core import data

#security_definitions = {
#   'bearer': {
#        'type': 'oauth2',
#        'flow': 'password',
#        'tokenUrl': '/v1/users/login/',
#    }
#}

app.config.update({
    'APISPEC_SPEC':
    APISpec(
        title='Portal tramites API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='3.0.3'
        ),  
    'APISPEC_SWAGGER_URL':
    '/v1/swagger/'
    
})
docs = FlaskApiSpec(app)

security_params = [{'bearer': []}]
