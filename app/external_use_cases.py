from app.models import *
from app import exceptions
from app.apis.rails_service import *
from app.use_cases import *

def external_get_all_queues():
    rails_queues = rails_get_all_queues()
    local_queues = get_all_queues()
    #PHP_QUEUES = ?

    return local_queues + rails_queues