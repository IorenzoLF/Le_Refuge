# Vérification des privilèges administrateur
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "Ce script nécessite des privilèges administrateur. Veuillez relancer PowerShell en tant qu'administrateur."
    exit 1
}

# Définition du chemin d'installation
$installPath = "C:\BuildTools"
$output = "vs_buildtools.exe"

# Vérification si l'installation existe déjà
if (Test-Path $installPath) {
    Write-Host "Visual Studio Build Tools est déjà installé dans $installPath"
    Write-Host "Veuillez d'abord désinstaller la version existante via le Panneau de configuration."
    exit 1
}

try {
    # Téléchargement de l'installateur
    Write-Host "Téléchargement de Visual Studio Build Tools..."
    $url = "https://aka.ms/vs/17/release/vs_buildtools.exe"
    Invoke-WebRequest -Uri $url -OutFile $output -UseBasicParsing

    # Installation des composants
    Write-Host "Installation des composants..."
    $process = Start-Process -FilePath ".\$output" -ArgumentList "--quiet", "--wait", "--norestart", "--nocache", `
        "--installPath", $installPath, `
        "--add", "Microsoft.VisualStudio.Workload.VCTools", `
        "--add", "Microsoft.VisualStudio.Component.VC.Tools.x86.x64", `
        "--add", "Microsoft.VisualStudio.Component.Windows10SDK.19041", `
        "--add", "Microsoft.VisualStudio.Component.VC.Redist.14.Latest", `
        "--add", "Microsoft.VisualStudio.Component.VC.CMake.Project", `
        "--add", "Microsoft.VisualStudio.Component.Windows10SDK", `
        "--add", "Microsoft.VisualStudio.Component.VC.14.38.x86.x64" -PassThru -Wait

    if ($process.ExitCode -eq 0) {
        Write-Host "Installation terminée avec succès"
        
        # Vérification de l'installation
        if (Test-Path "$installPath\VC\Auxiliary\Build\vcvars64.bat") {
            Write-Host "Les composants de compilation sont correctement installés"
        } else {
            Write-Host "ATTENTION: Les composants de compilation ne semblent pas être correctement installés"
            exit 1
        }
    } else {
        Write-Host "L'installation a échoué avec le code de sortie: $($process.ExitCode)"
        exit 1
    }
}
catch {
    Write-Host "Une erreur s'est produite: $_"
    exit 1
}
finally {
    # Nettoyage
    if (Test-Path $output) {
        try {
            Remove-Item $output -Force
        }
        catch {
            Write-Host "Impossible de supprimer le fichier temporaire: $_"
        }
    }
} 