# Manifest creates file

file { 'school':
  ensure  => 'present',
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744'
}
