#execute a command
exec { 'kill process':
  command => 'pkill -f killmenow',
  path    => ['/usr/local/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
