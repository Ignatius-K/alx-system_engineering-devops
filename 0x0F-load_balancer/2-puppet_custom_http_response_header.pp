# Manifest adds a Custom Response Header
exec { 'Add Header':
  command  => <<-EOS
    apt-get -y update;
    apt-get -y install nginx;
    sed -i '/listen 80 default_server;/a add_header X-Served-By $hostname;' /etc/nginx/sites-available/default;
    service nginx restart
  EOS,
  provider => shell,
}
