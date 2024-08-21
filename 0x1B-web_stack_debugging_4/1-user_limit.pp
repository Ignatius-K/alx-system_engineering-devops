# 1-user-limit.pp
#
# Puppet manifest file that changes the open file
# limit of user `holberton`
#
# Requirements:
#  - puppet

$target_file = '/etc/security/limits.conf'
$command = "sed -Ei 's/(^holberton .* nofile).*/\\1 8096/' ${target_file}"
$cmd_path = ['/usr/bin', '/usr/sbin', '/bin']

exec {'set_holberton_limits':
  command => $command,
  path    => $cmd_path
}
