from fabric.api import env

os_username = 'admin'
os_password = 'contrail123'
os_tenant_name = 'demo'
multi_tenancy = True

host1 = 'root@10.84.13.1'

ext_routers = []
router_asn = 64512
public_vn_rtgt = 10000
public_vn_subnet = "10.84.41.0/24"

host_build = 'dsetia@10.84.5.101'

env.roledefs = {
    'all': [host1],
    'cfgm': [host1],
    'openstack': [host1],
    'collector': [host1],
    'webui': [host1],
    'control': [host1],
    'compute': [host1],
    'database': [host1],
    'build': [host_build],
}

env.passwords = {
    host1: 'c0ntrail123',
    host_build: 'dsetia123',
}

env.hostnames = {
    'all': ['a6s1']
}

env.test_repo_dir='/home/dsetia/test'
env.pkg_dir='/home/dsetia/rpmbuild/RPMS'
env.mail_from='dsetia@juniper.net'
env.mail_to='dsetia@juniper.net'
