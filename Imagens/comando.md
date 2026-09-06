1..254 | ForEach-Object {
    $ip = "192.168.0.$_"
    if (Test-Connection $ip -Count 1 -Quiet -ErrorAction SilentlyContinue) {
        Write-Host "$ip ONLINE"
    }
}
