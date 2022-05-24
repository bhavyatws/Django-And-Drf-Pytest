![example workflow](https://github.com/bhavyatws/Django-And-Drf-Pytest/actions/workflows/django.yaml/badge.svg)

<!-- This is source syntax for putting github badges -->
<!-- source: https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge -->
<!-- ![example workflow](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE>/badge.svg) -->
#####################################################################################################
This project is about django and drf test cases and for CI/CD =>Continues Integrations / Continous Deployment
We have also used github action badges
We can also used custom settings by --ds=<settingsfilename> eg:--ds=github_settings.py
 - name: Run tests
        run: |
            pytest --ds= github_settings.py -v  --nomigrations
      - name: Run tests for api
        run: |
            pytest --ds= github_settings.py -v  api/tests/test_views.py --nomigrations
