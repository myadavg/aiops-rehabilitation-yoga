pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-2'
        ECR_REPOSITORY = '603571288927.dkr.ecr.eu-west-2.amazonaws.com/aiops-rehabilitation-yoga'
    }

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

        stage('Push to ECR') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'aws-ecr',
                        usernameVariable: 'AWS_ACCESS_KEY_ID',
                        passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                    )
                ]) {
                    sh '''
                        aws ecr get-login-password --region ${AWS_REGION} | \
                        docker login --username AWS --password-stdin ${ECR_REPOSITORY}

                        docker tag rehabilitation-yoga:${BUILD_NUMBER} \
                        ${ECR_REPOSITORY}:${BUILD_NUMBER}

                        docker tag rehabilitation-yoga:${BUILD_NUMBER} \
                        ${ECR_REPOSITORY}:latest

                        docker push ${ECR_REPOSITORY}:${BUILD_NUMBER}

                        docker push ${ECR_REPOSITORY}:latest
                    '''
                }
            }
        }
    }
}
