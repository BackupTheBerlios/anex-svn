[Setup] 
AppName=Astro-Nex 
AppVerName=Astro-Nex 1.2.2
AppPublisherURL=http://astro-nex.com
DefaultDirName={pf}\Astro-Nex-1.2.2
DefaultGroupName=Astro-Nex
DisableProgramGroupPage=true 
OutputBaseFilename=Astro-Nex-1.2.2p
Compression=lzma 
SolidCompression=true 
WizardImageFile=Styles\Office2007Gray.bmp
WizardSmallImageFile=compiler:WizModernSmallImage-IS.bmp
AllowUNCPath=false 
VersionInfoVersion=1.2.2
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
Source: ISSkin.dll; DestDir: {app}; Flags: dontcopy
Source: Styles\Office2007.cjstyles; DestDir: {tmp}; Flags: dontcopy
Source: astronex\resources\*; DestDir: {app}\astronex\resources; 
Source: share\*; DestDir: {app}\share; Flags: recursesubdirs createallsubdirs 
Source: etc\*; DestDir: {app}\etc; Flags: recursesubdirs createallsubdirs 
Source: lib\*; DestDir: {app}\lib; Flags: recursesubdirs createallsubdirs 
Source: *.pyd; DestDir: {app}; 
Source: *.dll; DestDir: {app}; 
Source: *.exe; DestDir: {app}; 
Source: library.zip; DestDir: {app};
Source: Microsoft.VC90.CRT.manifest; DestDir: {app};
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

[Code]
// Importing LoadSkin API from ISSkin.DLL
procedure LoadSkin(lpszPath: String; lpszIniFileName: String);
external 'LoadSkin@files:isskin.dll stdcall';

// Importing UnloadSkin API from ISSkin.DLL
procedure UnloadSkin();
external 'UnloadSkin@files:isskin.dll stdcall';

// Importing ShowWindow Windows API from User32.DLL
function ShowWindow(hWnd: Integer; uType: Integer): Integer;
external 'ShowWindow@user32.dll stdcall';

function InitializeSetup(): Boolean;
begin
	ExtractTemporaryFile('Office2007.cjstyles');
	LoadSkin(ExpandConstant('{tmp}\Office2007.cjstyles'), 'NormalAqua.ini');
	Result := True;
end;

procedure DeinitializeSetup();
begin
	// Hide Window before unloading skin so user does not get
	// a glimse of an unskinned window before it is closed.
	ShowWindow(StrToInt(ExpandConstant('{wizardhwnd}')), 0);
	UnloadSkin();
end;
