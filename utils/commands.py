exit_commands = ['exit', 'out', 'quit']

def preprocessing_command(command: str) -> str:
  return command.strip()

def the_command_is_an_quit(command: str) -> bool:
  command = preprocessing_command(command).lower()

  return command in exit_commands