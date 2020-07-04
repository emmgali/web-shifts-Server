from app import system_variables
class DTOQueue:

    # WARNING = PARAMETROS QUE O NO SE PUEDEN OBTENER DE LA API EXTERNA O NO SON DE FIAR
    def __init__(self, id, name, capacity, latitude, longitude, actualClientId, ownerId, description, entriesAmount, systemId):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.latitude = latitude
        self.longitude = longitude
        self.actualClientId = actualClientId
        self.ownerId = ownerId
        self.description = description
        self.entriesAmount = entriesAmount
        self.systemId = systemId

    @classmethod
    def from_rails_json(cls, json):
        cls(id=json["Id"],
            name=json["name"],
            latitude=float(json["geoubicacion"].split(", ")[0]),
            longitude=float(json["geoubicacion"].split(", ")[1]),
            capacity=json["Cupo"],
            actualClientId=-1,#WARNING
            ownerId=json["Usuario_id"],
            description=json["descripcion"],
            entriesAmount=0, #WARNING
            systemId=system_variables.RAILS_SYSTEM_ID
            )


    {
        "id": 1,
        "created_at": "2020-06-29T03:46:54.000000Z",
        "updated_at": "2020-06-29T03:46:54.000000Z",
        "name": "McDonalds",
        "description": "Hamburguesas",
        "images": "https:\/\/www.2spacios.com\/archivos\/image\/_noticias\/medias\/la-importancia-de-un-buen-logotipo-y-una-imagen-de-marca-cuidada.png",
        "geo_localization_x": "-34.561991576282",
        "geo_localization_y": "-58.477015063477",
        "user_id": 1
    },

    @classmethod
    def from_php_json(cls, json):
        cls(id=json["id"],
            name=json["name"],
            latitude=float(json["geo_localization_x"]),
            longitude=float(json["geo_localization_y"]),
            capacity=0, #WARNING
            actualClientId=-1,  # WARNING
            ownerId=json["user_id"], #WARNING
            description=json["description"],
            entriesAmount=0,  # WARNING
            systemId=system_variables.PHP_SYSTEM_ID
            )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'capacity': self.capacity,
            'actualClientId':  self.actualClientId,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'entriesAmount': self.entriesAmount,
            'systemId': self.systemId
        }