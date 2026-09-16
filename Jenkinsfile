pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t rehabilitation-yoga:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Test Docker Image') {
            steps {
                sh '''
                    docker images rehabilitation-yoga
                '''
            }
        }
    }
}
