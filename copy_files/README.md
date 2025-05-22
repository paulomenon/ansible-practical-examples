# Ansible copy example

1. **src:** Path to the source file on the control node (i.e., the machine running Ansible), unless using delegate_to: localhost or running on localhost.

2. **dest:** Path where the file should be copied on the target host.

3. Make sure the destination directory exists or use the file module to create it beforehand.
   
4. Delete destination.txt under the destination folder before you test the play