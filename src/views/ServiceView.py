from flask import request, json, Response, Blueprint
from ..models.ServiceModel import ServiceModel, ServiceSchema
service_api = Blueprint("services", __name__)
service_schema = ServiceSchema()
@service_api.route("/", methods=["GET"])
def get_all():
    services = ServiceModel.get_all_services()
    ser_services = service_schema.dump(services, many=True)
    # ser_srv = ser_services.data
    # print(ser_srv)
    return custom_response(ser_services, 200)
@service_api.route("/<int:service_id>", methods=["GET"])
def get_a_service(service_id):
    # Get a single service
    service = ServiceModel.get_one_service(service_id)
    if not service:
        return custom_response({"error": "service not found"}, 404)
    ser_service = service_schema.dump(service).data
    return custom_response(ser_service, 200)
def custom_response(res, status_code):
    # Custom Response Function
    return Response(mimetype="application/json", response=json.dumps(res), status=status_code)