import jinja2

switch_vars = {
    'host_name': 'leaf1',
    'domain_name':'ntc.com',
    'vlan_10_id': '10',
    'vlan_10_name': 'web',
    'vlan_20_id': '20',
    'vlan_20_name': 'app',
    'vlan_30_id': '30',
    'vlan_30_name': 'db'
}

switch_template = '''
hostname {{ host_name }}
ip domain-name {{ domain_name }}
!
vlan {{ vlan_10_id }}
   name {{ vlan_10_name }}
!
vlan {{ vlan_20_id }}
   name {{ vlan_20_name }}
!
vlan {{ vlan_30_id }}
   name {{ vlan_30_name }}
'''

templ = jinja2.Template(switch_template)
ren_templ = templ.render(switch_vars)
print(ren_templ)