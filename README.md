# qumulo-smb-lock-manager-webui
A lightweight WebUI for https://github.com/nivfreak/qumulo-smb-lock-manager

Summary
--------------------------
Intended to empower your helpdesk team to terminate locks from a simple WebUI,
leaving you more time to explore artisanal hot sauces. Hot Sauce not included.

Docker
--------------------------

* Developed with docker 20.10.12


Start by making a copy of template.docker-env to .env in the source directory.

Launch the configured server as a daemon with:

    $ docker-compose up -d


You can view the output of the service with:

    $ docker-compose logs -f

