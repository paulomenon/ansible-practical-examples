# Ansible extra var example

## Command line example

<pre> ```bash ansible-playbook var_samples.yaml \ --extra-vars "username='P. E. Menon' uid_number=1000 gid_number=1000 user_email=pmenoninsights@gmail.com" ``` </pre>

## Ansible extra var as JSON format

You can pass extra var as json format as well

<pre> ```ansible-playbook use_variables/var_samples.yaml \
  --extra-vars '{"username": "P. E. Menon", "uid_number": 1000, "gid_number": 1000, "user_email": "pmenoninsights@gmail.com"}'``` </pre>
