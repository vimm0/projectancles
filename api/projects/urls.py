from apistar import Route
from . import views

projects_urls = [
    Route('/', 'GET', views.get_projects_list),
    Route('/', 'POST', views.create_project),
    Route('/{project_id}', 'GET', views.get_project),
]