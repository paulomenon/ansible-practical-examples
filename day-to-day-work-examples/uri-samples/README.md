# Pre requirements to run uri_post_request.yaml

- Ansible installed (version 2.9+ recommended)
- Go to python-user-api and follow the README page to start the webserver running on localhost

# Example how to run the playbook
```bash 
ansible-playbook uri_post_request.yaml
```

# Test using curl 
```bash
curl -X GET http://localhost:8080/api/users/pamenon
```

This will show the payload, in memory.

You can change the playbook username and email run it again and test the GET
curl -X GET http://localhost:8080/api/users/<username> 

