pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.selenium'
            dir '.'
            additionalBuildArgs ''
        }
    }

    environment {
        REPORT_DIR = 'reports'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    mkdir -p $REPORT_DIR
                    pytest --junitxml=$REPORT_DIR/results.xml \
                           --html=$REPORT_DIR/report.html \
                           --self-contained-html
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
