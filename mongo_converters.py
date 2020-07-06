from werkzeug.routing import BaseConverter
from werkzeug.exceptions import BadRequest
from dateutil import parser
from datetime import datetime
import bson


class ObjectIdConverter(BaseConverter):
    """Converts string to :class:`~bson.objectid.ObjectId` and
    vise versa::
        @app.route('/users/<ObjectId:user_id>', methods=['GET'])
        def get_user(user_id):
            ...
    To register it in `Flask`, add it to converters dict::
        app.url_map.converters['ObjectId'] = ObjectIdConverter
    Alternative registration way::
        ObjectIdConverter.register_in_flask(app)
    """

    @classmethod
    def to_python(cls, value):
        try:
            return bson.ObjectId(value)
        except bson.errors.InvalidId as e:
            raise BadRequest(e)

    def to_url(self, value):
        return str(value)


class DateTimeConverter(BaseConverter):
    @classmethod
    def to_python(cls, value):
        if isinstance(value, datetime):
            return value

        try:
            return parser.parse(value)
        except ValueError as e:
            raise BadRequest(e)

    def to_url(self, value):
        return str(value)
