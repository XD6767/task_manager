[Setup]
AppName=Task Manager
AppVersion=1.0
AppPublisher=XD
DefaultDirName={autopf}\Task Manager
DefaultGroupName=Task Manager
OutputDir=installer_output
OutputBaseFilename=TaskManagerSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Files]
Source: "dist\Task Manager\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Task Manager"; Filename: "{app}\Task Manager.exe"
Name: "{autodesktop}\Task Manager"; Filename: "{app}\Task Manager.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Создать ярлык на рабочем столе"; GroupDescription: "Дополнительные задачи:"

[Run]
Filename: "{app}\Task Manager.exe"; Description: "Запустить Task Manager"; Flags: nowait postinstall skipifsilent