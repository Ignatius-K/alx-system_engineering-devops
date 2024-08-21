# 0-the_sky_is_the_limit_not.pp
# 
# Puppet script that fixes the `ULIMIT`
# default setting on nginx

$target_file = '/etc/default/nginx'
$command = "sed -Ei 's/(^ULIMIT=\"-n ).*/\\11048572\"/' ${target_file}"
$cmd_path = ['/usr/bin', '/usr/sbin', '/bin']

exec {'set_nginx_ulimit':
  command => $command,
  onlyif  =>  ['test -f $target_file'],
  path    => $cmd_path,
  notify  => Exec['restart_nginx']
}

exec {'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/bin'
}

