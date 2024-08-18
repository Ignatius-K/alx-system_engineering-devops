# 0-strace_is_your_friend.pp
# Script fixes the 500-server-error on Apache
# 
# Requirements:
# - puppet
file {'File created':
  ensure => present,
  path   => '/var/www/html/wp-includes/class-wp-locale.phpp',
  source => '/var/www/html/wp-includes/class-wp-locale.php'
}
