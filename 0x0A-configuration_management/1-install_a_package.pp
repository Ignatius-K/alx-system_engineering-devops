# Manifest install `flask` package

package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
  require  => Package['werkzeug']
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
}
