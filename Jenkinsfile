pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir '.'
            additionalBuildArgs ''
        }
    }

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

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests (Headless Chrome)') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    mkdir -p $REPORT_DIR
                    pytest --junitxml=$REPORT_DIR/results.xml \
                           --html=$REPORT_DIR/report.html --self-contained-html
                '''
            }
        }

        stage('Publish Reports') {
            steps {
                junit "$REPORT_DIR/results.xml"
                archiveArtifacts artifacts: "$REPORT_DIR/report.html", fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            deleteDir()
        }
    }
}
