import win32com.shell.shell as shell
commands = 'net stop MongoDB'
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
