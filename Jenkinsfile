pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vsk1005/vskiris.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
            }
        }
    }
}