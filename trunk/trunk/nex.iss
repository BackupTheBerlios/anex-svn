[Setup] 
AppName=Astro-Nex 
AppVerName=Astro-Nex 1.2
AppPublisherURL=http://astro-nex.com
DefaultDirName={pf}\Astro-Nex-1.2
DefaultGroupName=Astro-Nex
DisableProgramGroupPage=true 
OutputBaseFilename=Astro-Nex-1.2
Compression=lzma 
SolidCompression=true 
AllowUNCPath=false 
VersionInfoVersion=1.2
PrivilegesRequired=admin
AllowNoIcons=yes
AlwaysShowDirOnReadyPage=no
SetupIconFile=astronex\resources\nex.ico
UsePreviousAppDir=no

[Languages]
Name:"en"; MessagesFile:"compiler:Default.isl"
Name:"es"; MessagesFile:"compiler:Languages\Spanish.isl"
Name:"ca"; MessagesFile:"compiler:Languages\Catalan.isl"
Name:"de"; MessagesFile:"compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons" 
 
[Dirs] 
Name: {app}; Flags: uninsalwaysuninstall; 
 
[Files] 
Source: astronex\resources\*; DestDir: {app}\astronex\resources; 
Source: share\*; DestDir: {app}\share; Flags: recursesubdirs createallsubdirs 
Source: etc\*; DestDir: {app}\etc; Flags: recursesubdirs createallsubdirs 
Source: lib\*; DestDir: {app}\lib; Flags: recursesubdirs createallsubdirs 
Source: *.pyd; DestDir: {app}; 
Source: *.dll; DestDir: {app}; 
Source: *.exe; DestDir: {app}; 
Source: library.zip; DestDir: {app}; 
Source: astronex\db\local.db; DestDir: {app}\astronex\db; Flags: recursesubdirs createallsubdirs 
Source: astronex\locale\*; DestDir: {app}\astronex\locale; Flags: recursesubdirs createallsubdirs
Source: astronex\zoneinfo\*; DestDir: {app}\astronex\zoneinfo; Flags: recursesubdirs createallsubdirs
Source: astronex\resources\Astro-Nex.ttf; DestDir: {fonts}; FontInstall: "Astro-Nex"; Flags: uninsneveruninstall 
 
[Icons] 
Name: {group}\Astro-Nex; Filename: {app}\nex.exe; WorkingDir: {app}; IconFilename:{app}\astronex\resources\nex.ico;
Name: {group}\Desinstalar; Filename:"{uninstallexe}"
Name: "{userdesktop}\Astro-Nex"; Filename: "{app}\nex.exe"; WorkingDir:{app}; IconFilename:{app}\astronex\resources\nex.ico;  Tasks: desktopicon
  
[Run] 
Filename: {app}\nex.exe; Description: {cm:LaunchProgram,Astro-Nex}; Flags: nowait postinstall skipifsilent 

