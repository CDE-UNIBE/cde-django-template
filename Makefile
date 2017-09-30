default: env-vars cleanup

env-vars:
	# Create the necessary env vars and set default values.
	echo "postgres://db_user:password@localhost:5432/db_name" > envs/DATABASE_URL
	echo "localhost, 127.0.0.1" > envs/DJANGO_ALLOWED_HOSTS
	echo "DevConfig" > envs/DJANGO_CONFIGURATION
	echo "True" > envs/DJANGO_DEBUG
	echo "{{ secret_key }}" > envs/DJANGO_SECRET_KEY
	echo "apps.{{ project_name }}.settings" > envs/DJANGO_SETTINGS_MODULE
	@echo "Env vars set with default values, you may need to adapt them."

cleanup:
	rm Makefile
	@echo "Makefile was removed as it contains sensible data (e.g. the SECRET_KEY)"
