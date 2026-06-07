pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
            }
        }
    }
}
