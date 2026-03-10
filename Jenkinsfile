pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        REPORT_DIR = 'reports'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Selenium Tests (Headless Chrome)') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    if not exist %REPORT_DIR% mkdir %REPORT_DIR%
                    pytest --junitxml=%REPORT_DIR%\\results.xml ^
                           --html=%REPORT_DIR%\\report.html --self-contained-html
                """
            }
        }

        stage('Publish Reports') {
            steps {
                junit "%REPORT_DIR%\\results.xml"
                archiveArtifacts artifacts: "%REPORT_DIR%\\report.html", fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
        failure {
            echo 'Build failed. Check reports for details.'
        }
    }
}
