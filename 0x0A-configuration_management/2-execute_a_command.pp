# Manifest kills a process

$process_name = 'killmenow'
exec { 'Kill process':
  command => "/usr/bin/pkill -f ${process_name}",
}
