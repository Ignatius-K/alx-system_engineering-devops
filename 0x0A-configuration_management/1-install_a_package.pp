# Manifest install `flask` package

package { 'Install Flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
