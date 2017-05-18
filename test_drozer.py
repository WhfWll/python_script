from drozer.console.console import Console
from drozer.console.session import Session
from drozer.connector import ServerConnector

md=Console()
arguments=md.parse_arguments(md._parser, ['', ''])
server=ServerConnector(arguments, None)
devices=server.listDevices().system_response.devices
response=server.startSession(devices[0].id, None)
session_id=response.system_response.session_id
drozer_session=Session(server, session_id, arguments)
command='scanner.misc.writablefiles /data/data/ --privileged'
drozer_session.do_run(command)
