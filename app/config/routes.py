
from system.core.router import routes
routes['default_controller'] = 'Courses'
routes['POST']['/courses/add'] = 'Courses#add'
routes['/courses/delete/<id>'] = 'Courses#delete'
routes['POST']['/yes_delete/<id>'] = 'Courses#yes_delete'
routes['POST']['/no'] = 'Courses#no_delete'
