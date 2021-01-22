pipeline {
    agent any
    environment {
    IMAGE_NAME = 'flask-app'
    IMAGE_VERSION = '0.1'
    DOCKER_REPO_NAME = 'pankaj2934'
    }
    stages {
        stage('docker-Build') {
        steps {
            sh '''
            env
            docker build . -t $DOCKER_REPO_NAME/$IMAGE_NAME:$IMAGE_VERSION.$BUILD_NUMBER
            '''

        }
        }
        stage('docker-Push') {
            steps {

            sh '''
            env
            docker push $DOCKER_REPO_NAME/$IMAGE_NAME:$IMAGE_VERSION.$BUILD_NUMBER
            '''

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
