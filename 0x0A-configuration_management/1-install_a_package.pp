# Manifest install `flask` package
# package { 'flask':
#   ensure   => '2.1.0',
#   provider => pip3,
# }

exec { 'Install Flask':
  command => '/usr/bin/pip3 install flask==2.1.0'
}
