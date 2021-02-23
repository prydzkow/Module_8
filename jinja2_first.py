import jinja2

switch_vars = {}

switch_template = '''
hostname leaf1
ip domain-name ntc.com
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