$ips = @(
"192.168.0.4",
"192.168.0.7",
"192.168.0.20",
"192.168.0.23",
"192.168.0.26"
)

$ports = @(80,443,554,8000,8080,34567,37777)

foreach ($ip in $ips) {
    Write-Host "`n===== $ip ====="
    foreach ($port in $ports) {
        $r = Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue
        if ($r.TcpTestSucceeded) {
            Write-Host "ABERTA: $port"
        }
    }
}
