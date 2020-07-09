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
        return cls(id=json["id"],
            name=json["nombre"],
            latitude=float(json["latitud"]),
            longitude=float(json["longitud"]),
            capacity=json["cupo"],
            actualClientId=-1,#WARNING
            ownerId=json["usuario_id"],
            description=json["descripcion"],
            entriesAmount=0, #WARNING
            systemId=system_variables.RAILS_SYSTEM_ID
            )

    @classmethod
    def from_php_json(cls, json):
        return cls(id=json["id"],
            name=json["name"],
            latitude=float(json["geo_localization_x"]),
            longitude=float(json["geo_localization_y"]),
            capacity=-1, #WARNING
            actualClientId=-1,  # WARNING
            ownerId=json["user_id"], #WARNING
            description=json["description"],
            entriesAmount=-1,  # WARNING
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
