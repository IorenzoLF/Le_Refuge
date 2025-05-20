# Get current path
$currentPath = Get-Location
$batchPath = Join-Path $currentPath "demarrer_jardinier.bat"

# Create shortcut in startup folder
$startupFolder = [Environment]::GetFolderPath("Startup")
$shortcutPath = Join-Path $startupFolder "Jardinier.lnk"

# Create shortcut
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $batchPath
$Shortcut.WorkingDirectory = $currentPath
$Shortcut.Description = "Jardinier des Spheres"
$Shortcut.Save()

Write-Host "✅ Le jardinier sera lance automatiquement au demarrage de Windows"
Write-Host "Le raccourci a ete cree dans : $startupFolder" 