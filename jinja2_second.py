import jinja2

switch_vars = {
    'host_name': 'leaf1',
    'domain_name':'ntc.com'
}

switch_template = '''
hostname {{ host_name }}
ip domain-name {{ domain_name }}
!
vlan 10
   name web
!
vlan 20
   name app
!
vlan 30
   name db
'''

templ = jinja2.Template(switch_template)
ren_templ = templ.render(switch_vars)
print(ren_templ)