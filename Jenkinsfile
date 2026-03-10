pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        REPORT_DIR = 'reports'
        DRIVER_DIR = 'drivers'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo '✅ Checkout complete'
            }
        }

        stage('Environment Info') {
            steps {
                bat 'ver'
                bat 'where python'
                bat 'python --version'
                bat 'where chromedriver'
                bat 'where chrome'
            }
        }

        stage('PowerShell Test') {
            steps {
                powershell '''
                    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
                    Write-Host "✅ PowerShell is working"
                '''
            }
        }
    }
}
