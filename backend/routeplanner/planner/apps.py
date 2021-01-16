from django.apps import AppConfig
from .domain.map import save_graph, check_graph
import logging

logger = logging.getLogger(__name__)

class PlannerConfig(AppConfig):
    name = 'planner'

    def ready(self):
        print("Checking if graph exists")
        if check_graph():
            print("Graph exists - I'm using it")
            return
        else:
            print("Dowloading new graph")
            save_graph()
