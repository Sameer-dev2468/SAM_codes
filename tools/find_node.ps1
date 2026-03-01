# Helper: locate node.exe and npm.cmd, then install frontend deps and start dev server

# Try to find node.exe quickly under common folders
$node = $null
try {
  $found = Get-ChildItem -Path 'C:\Program Files', "$env:LOCALAPPDATA" -Filter 'node.exe' -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($found) { $node = $found.FullName }
} catch { }

if (-not $node) { Write-Output 'NODE_NOT_FOUND'; exit 2 }

Write-Output "FOUND_NODE:$node"
& $node --version

$bindir = Split-Path $node
$npmcmd = Join-Path $bindir 'npm.cmd'
if (Test-Path $npmcmd) { Write-Output "FOUND_NPMCMD:$npmcmd"; & $npmcmd --version } else { Write-Output 'NPMCMD_NOT_FOUND' }

Set-Location 'C:\Users\tumam\OneDrive\Desktop\SAM_codes\sam-ecommerce\frontend'
if (Test-Path $npmcmd) {
  & $npmcmd install
  & $npmcmd run dev
} else {
  Write-Output 'Cannot run npm because npm.cmd not found in node folder.'
}
