import win32com.shell.shell as shell
commands = 'net start MySQL80'
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
