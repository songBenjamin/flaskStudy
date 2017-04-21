from flaskstudy import app 

from flask.ext.script import Manager, Server
#from flask_migrate import Migrate, MigrateCommand

manager = Manager(app,with_default_commands=True)

manager.add_command("runserver",Server(host="127.0.0.1", port=5000, use_debugger=True))

#migrate = Migrate(app,db)
#manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
