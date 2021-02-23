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

#Read jinja2 template file
switch_template_file = 'switch_tmpl.j2'
with open(switch_template_file) as f:
   switch_templ = f.read()

#Render template file and print
templ = jinja2.Template(switch_templ)
ren_templ = templ.render(switch_vars)
print(ren_templ)