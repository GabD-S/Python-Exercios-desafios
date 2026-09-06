$ips = @(
"192.168.0.17",
"192.168.0.22",
"192.168.0.30",
"192.168.0.64",
"192.168.0.27",
"192.168.0.28",
"192.168.0.32",
"192.168.0.33"
)

foreach ($ip in $ips) {
    $ping = Test-Connection $ip -Count 1 -Quiet
    Write-Host "$ip -> $ping"
}




$ips = @(
"192.168.0.17",
"192.168.0.22",
"192.168.0.30",
"192.168.0.64",
"192.168.0.27",
"192.168.0.28",
"192.168.0.32",
"192.168.0.33"
)

$ports = @(80,443,554,8000)

foreach ($ip in $ips) {
    Write-Host "`n--- $ip ---"
    foreach ($port in $ports) {
        $r = Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue
        Write-Host "Porta $port -> $($r.TcpTestSucceeded)"
    }
}
