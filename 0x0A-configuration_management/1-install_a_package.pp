#install flask using puppet
exec { 'install flask':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/local/bin', '/usr/bin'],
}
