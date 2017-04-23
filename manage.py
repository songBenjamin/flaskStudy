import os
from app import create_app, db
from app.models import  User, Role
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

manager.add_command("runserver",Server(host="127.0.0.1", port=5000, use_debugger=True))

migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db, User=User, Role=Role)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
