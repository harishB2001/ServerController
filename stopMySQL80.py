import win32com.shell.shell as shell
commands = 'net stop MySQL80'
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
